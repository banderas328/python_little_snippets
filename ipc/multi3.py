import os
from multiprocessing import Process, Value , Array

procs = 3
count = 0

def showdata(label, val ,  arr):
    """
    output data values in this process
    """
    msq = '%-12s: pid:%4s , global:%s, value:%s , array:%s'
    print(msq % (label, os.getpid(), count , val.value, list(arr)))

def updater(val,arr):
    """
    exchange data between memory
    """
    global count
    count += 1
    val.value += 1
    for i in range(3): arr[i] += 1

if __name__ == '__main__':
    scalar = Value('i', 0)

    vector = Array('d' , procs)

    showdata('parent start' , scalar, vector)

    p = Process(target=showdata , args=('child' , scalar , vector))
    p.start(); p.join()

    print('\n loop1(updates in parent , serial children) ...')
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(('process %s % i'),
                                           scalar, vector))
        p.start(); p.join()

    print('\n loop2 (updates in parent , paralel children)...')
    ps = []
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(('process %s % i'),
                                           scalar, vector))
        p.start()
        ps.append(p)

    for p in ps : p.join()

    print('\n loop3 (updates in serial children)...')
    for i in range(procs):
        p = Process(target=updater,args=(scalar, vector))
        p.start()
        p.join()
        showdata('parent temp', scalar, vector)

    ps = []
    print('\nloop4 (updates in parallel children)...')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        ps.append(p)

    for p in ps: p.join()

    showdata('parent end' ,scalar, vector)

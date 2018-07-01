import sys,os
syslen  = len(dir(sys))
print(syslen)

oslen = len(dir(os))
print(oslen)
print(len(dir(os.path)))
print(dir(sys))
print(sys.__doc__)
help(sys)
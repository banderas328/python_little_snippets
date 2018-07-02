class Node:

    def __init__(self,val):
        self.val = val
        self.next = None

class List:
    list = []
    def __init__(self,list):
        self.list = list

    def init(self, list):
        self.list = list

    def append(self , node):
        lastElement = len(self.list)
        print(lastElement)
        lastElement = int(lastElement)
        print(lastElement)
        i = 1
        for element in self.list:
            if i != lastElement:
                i += 1
            else:
                element.next = node
                self.list.append(node)
                return True
            print(i)

    def prepend(self, node):
        newList = []
        oldList = self.list
        oldFistNode = self.list[0]
        node.next = oldFistNode
        newList.append(node)
        for element in oldList:
            newList.append(element)
        self.list = newList




    def traverse(self):
          # start from the head node
        for element in self.list:
            print(element.val)  # access the node value
            element = element.next



        # for element in self.list:


if __name__ == "__main__":
    node1 = Node(12)
    node2 = Node(99)
    node3 = Node(37)
    node1.next = node2 # 12->99
    node2.next = node3
    nodesList = [node1,node2,node3]

    listNodes = List(nodesList)

    nodelast = Node(777)
    listNodes.append(nodelast)
    listNodes.traverse()
    nodeFirst = Node(111)
    listNodes.prepend(nodeFirst)
    listNodes.traverse()

    # print(listNodes)
    # for element in listNodes.list:
    #     print(element)
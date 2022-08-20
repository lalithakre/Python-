class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def __init__(self):
      self.headval = None
   def listprint(self):
        printval = self.headval
        while printval is not None:
             print (printval.dataval)
             printval = printval.nextval
list1 = SLinkedList()
list1.headval = Node("Mon")
a2 = Node("Tue")
a3 = Node("Wed")
a4 = Node("Thurs")
list1.headval.nextval = a2
a2.nextval = a3
a3.nextval = a4
list1.listprint()
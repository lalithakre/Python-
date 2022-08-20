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
   def AtBegining(self,newdata):
      NewNode = Node(newdata)
      NewNode.nextval = self.headval
      self.headval = NewNode
list = SLinkedList()
list.headval = Node("Mon")
a2 = Node("Tue")
a3 = Node("Wed")
list.headval.nextval = a2
a2.nextval = a3
list.AtBegining("Sun")
list.listprint()
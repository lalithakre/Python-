class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def __init__(self):
      self.headval = None
   def Inbetween(self,middle_node,newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return
      NewNode = Node(newdata)
      NewNode.nextval = middle_node.nextval
      middle_node.nextval = NewNode
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
list = SLinkedList()
list.headval = Node("Mon")
a2 = Node("Tue")
a3 = Node("Thu")
list.headval.nextval = a2
a2.nextval = a3
list.Inbetween(list.headval.nextval,"wed")
list.listprint()
import random
import time
import matplotlib.pyplot as plt
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
    def __init__(self): # Create it upon calling
      self.headval = None

    def listprint(self): #Printing the list
      printval = self.headval # Set initial value as the head
      while printval != None: # Iterate through the list until the last item
         print (printval.dataval) 
         printval = printval.nextval #jump to the next value

    def addNewValue(self, newNode):
        if self.headval == None: #If the list is empty
            newNode.nextval = self.headval
            self.headval = newNode
        elif self.headval.dataval > newNode.dataval: # Changing out the head in case there is a smaller value
            newNode.nextval = self.headval
            self.headval = newNode
        else:
            current = self.headval
            while (current.nextval != None and current.nextval.dataval < newNode.dataval): #Iterate the list until either the end of the list or we find the right spot for it
                current = current.nextval
            newNode.nextval = current.nextval
            current.nextval = newNode
list1 = SLinkedList()
def addRandomNumbers(n): 
    for i in range(1,n+1):
        newValue = random.randint(1,n)
        newNode = Node(newValue)
        list1.addNewValue(newNode)
        
runTimeStorage = []
nStorage = []
for i in range(100, 501, 50):
    nStorage.append(i)
    start = time.time()
    addRandomNumbers(i)
    end = time.time()
    runTime = end - start
    print(i)
    print(runTime)
    runTimeStorage.append(runTime)
plt.plot(nStorage, runTimeStorage)
plt.xlabel('Number of Items in Sorted Linked List')
plt.ylabel('Run Time (seconds)')
plt.title('Run Time vs Number of Items')
print(runTimeStorage)

# def newHead(newValue, list):
#     #function to insert a new node at the beginning of the linked list
#     newNode = Node(newValue)
#     newNode.nextval = self.head
# def findLocationToInsert(newValue, list):
    
#     checkval = list.headval
#     if newValue < checkval.dataval: #special case if the new value is less than the head value
#         newHead(newValue)
#     while checkval is not None:
#         if newValue <= listPosition.dataval:
#             return listPosition
#         else:
#             listPositionOld = listPosition
#             listPosition = listPosition.nextval
#             # If it is at the very end of the list 
#             if listPosition == None:
#                 return listPositionOld


# def addValues(n, startNode, list1):
#     valueStorage = [] # Storage of random numbers in order of generation
#     for i in range(1,n):
#         value = random.randint(1,n)
#         valueStorage.append(value)

def newValuePositionInList(newValue, list):
    currentValue = list.headval
    while currentValue.nextval != None and currentValue.nextval.dataval < newValue:
        currentValue = currentValue.nextval #  Iterate through the loop until we find that the currentValue in the list is greater than or equal to newValue     
    return currentValue


# def addNewValue(n, list):
#     list.headval = Node(random.randint(1,n))
#     for i in range(1,n):
#         newValue = random.randint(1,n)
#         newNode = Node(newValue)
        
#         if newValue < list.headval.dataval: # special case if the new value is less than the head value
#             # print((newValue, list.headval.dataval))
#             list.listprint()
#             newNode.next = list.headval
#             list.headval = newNode
#         else:
#             previousValue = newValuePositionInList(newValue, list)
#             newNode.nextval = previousValue.nextval
#             previousValue.nextval = newNode


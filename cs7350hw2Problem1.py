"""
Created on Fri Mar 11 14:20:03 2022

@author: Max
"""
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
            
# Adjascency List representation in Python

class AdjNode: # Taken from: https://www.programiz.com/dsa/graph-adjacency-list
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:# Taken from: https://www.programiz.com/dsa/graph-adjacency-list
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

class CompleteGraph: 
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V
    
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node
    
    def all_edges(self):
        for i in range(self.V):
            remainingEdges = range(i+1, self.V)
            for k in remainingEdges:
                self.add_edge(i, k)

    def print_agraph(self): # Need to modify this to fit the desired format
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

class CycleGraph: 
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V
    
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node
    
    def allEdgesInCycle(self):
        for i in range(0,self.V):
            if i >= self.V -1:
                self.add_edge(0, self.V -1)
            else:
                
                self.add_edge(i, i+1)
    def print_agraph(self): # Need to modify this to fit the desired format
        print(self.V)
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
                print(" \n")       
            
if __name__ == "__main__": # Taken from: https://www.programiz.com/dsa/graph-adjacency-list
    

    # Create graph and edges
    # graph = Graph(V)
    # graph.add_edge(0, 1)
    # graph.add_edge(0, 2)
    # graph.add_edge(0, 3)
    # graph.add_edge(1, 2)
    # graph.print_agraph()
    runtimeStorage = []
    vStorage = []
    #
    
    for V in range(5): # For complete graph, it looks like n^2
        start = time.time()
        # completeGraph = CompleteGraph(V)
        # completeGraph.all_edges()
        cycle = CycleGraph(V)
        cycle.allEdgesInCycle()
        end = time.time()
        runtime = end - start
        runtimeStorage.append(runtime)
        vStorage.append(V)
        print(runtime)
    # completeGraph.print_agraph()
    cycle.print_agraph()
    plt.plot(vStorage, runtimeStorage)
    plt.xlabel('Number of Items in Complete Graph')
    plt.ylabel('Run Time (seconds)')
    plt.title('Run Time vs Number of Items')

    

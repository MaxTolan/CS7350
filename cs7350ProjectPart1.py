# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:20:03 2022

@author: Max
"""
import time
import matplotlib.pyplot as plt #Can be reimplemented by uncommenting lines 152-160
import numpy as np
import scipy.stats as stats
import math



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
    def __init__(self, num):# Taken from: https://www.programiz.com/dsa/graph-adjacency-list
        self.V = num
        self.graph = [None] * self.V
    
    def add_edge(self, s, d):# Taken from: https://www.programiz.com/dsa/graph-adjacency-list
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

    def print_agraph(self): 
        print(self.V)
        print(self.V + 1) # Location of first node's edges
        weight = self.V -1
        numberOfCountedNodes = 0
        for i in range(self.V -1):
            print(self.V + 1 + weight + (numberOfCountedNodes * weight))
            numberOfCountedNodes += 1
            
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                # print(" -> {}".format(temp.vertex), end="")
                print(temp.vertex)
                temp = temp.next
                
class CycleGraph: 
    def __init__(self, num):# Taken from: https://www.programiz.com/dsa/graph-adjacency-list
        self.V = num
        self.graph = [None] * self.V
    
    def add_edge(self, s, d):# Taken from: https://www.programiz.com/dsa/graph-adjacency-list
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
        print(self.V + 1) # Location of first node's edges
        weight = 2
        numberOfCountedNodes = 0
        for i in range(self.V -1):
            print(self.V + 1 + weight + (numberOfCountedNodes * weight))
            numberOfCountedNodes += 1
            
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                # print(" -> {}".format(temp.vertex), end="")
                print(temp.vertex)
                temp = temp.next            
class UniformRandomGraph: 
    def __init__(self, vertices, edges):# Taken from: https://www.programiz.com/dsa/graph-adjacency-list
        self.V = vertices
        self.E = edges
        self.graph = [None] * self.V
    
    def add_edge(self, s, d):# Taken from: https://www.programiz.com/dsa/graph-adjacency-list

        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node
        
    def printUniformDistribution(self):
        h = plt.hist(np.random.uniform(0, self.V, 10000), bins = 30, density= True)
        plt.show(h)
        
    def generateUniformRandomGraph(self):
        # Create dictionary to prevent duplicate values
        existingEdges = {}
        for i in range (0, self.V): # Populate all vertices with empty arrays to signify no edges created 
            existingEdges[i] = []
        for i in range(0, self.E): 

            source = math.floor(np.random.uniform(0, self.V))
            dest =  math.floor(np.random.uniform(0, self.V))

            checkExisting = existingEdges.get(source, [-1]) # Get array of edges from that source
            
                
            while (source == dest) or (dest in checkExisting): # Re-roll if we have a duplicate edge or edge going nowhere
                source = math.floor(np.random.uniform(0, self.V))
                dest =  math.floor(np.random.uniform(0, self.V))
                checkExisting = existingEdges.get(source, -1)
            self.add_edge(source, dest)
            existingEdges[source] += [dest]#Add source and destination to existing edges
            existingEdges[dest] += [source]
        print(existingEdges)
        return existingEdges
    
    def print_agraph(self): # Need to modify this to fit the desired format
        edgeDictionary = self.generateUniformRandomGraph()    
        print(self.V)
        print(self.V + 1) # Location of first node's edges
        
        # Commented section below handles the intro for the pointers
        
        totalWeight = 0
        for i in range(self.V -1):
            weight = len(edgeDictionary[i])
            totalWeight += weight
            print(self.V + 1 + totalWeight)
            
            
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                # print(" -> {}".format(temp.vertex), end="")
                print(temp.vertex)
                temp = temp.next  

class SkewedRandomGraph: 
    def __init__(self, vertices, edges):# Taken from: https://www.programiz.com/dsa/graph-adjacency-list
        self.V = vertices
        self.E = edges
        self.graph = [None] * self.V
    
    def add_edge(self, s, d):# Taken from: https://www.programiz.com/dsa/graph-adjacency-list
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node
    def generateSkewedRandomGraph(self):
        # Create dictionary to prevent duplicate values
        existingEdges = {}
        for i in range (0, self.V): # Populate all vertices with empty arrays to signify no edges created 
            existingEdges[i] = []
        for i in range(0, self.E): 
            source = math.floor(np.random.triangular(0, 0, self.V))
            dest =  math.floor(np.random.triangular(0, 0, self.V))
            checkExisting = existingEdges.get(source, [-1]) # Get array of edges from that source
            while (source == dest) or (dest in checkExisting): # Re-roll if we have a duplicate edge or edge going nowhere
                source = math.floor(np.random.triangular(0, 0, self.V))
                dest =  math.floor(np.random.triangular(0, 0, self.V))
                checkExisting = existingEdges.get(source, -1)
            self.add_edge(source, dest)
            existingEdges[source] += [dest]#Add source and destination to existing edges
            existingEdges[dest] += [source]
        print(existingEdges)
        return existingEdges
                
    def printSkewedDistribution(self):
         h = plt.hist(np.random.triangular(0, 0, self.V,10000), bins = 30, density= True)
         plt.show(h)        
                
    def print_agraph(self): # Need to modify this to fit the desired format
       edgeDictionary = self.generateSkewedRandomGraph()    
       print(self.V)
       print(self.V + 1) # Location of first node's edges
       
       # Commented section below handles the intro for the pointers
       
       totalWeight = 0
       for i in range(self.V -1):
           weight = len(edgeDictionary[i])
           totalWeight += weight
           print(self.V + 1 + totalWeight)
           
           
       for i in range(self.V):
           temp = self.graph[i]
           while temp:
               # print(" -> {}".format(temp.vertex), end="")
               print(temp.vertex)
               temp = temp.next              

class GaussianDistributionRandomGraph:
    def __init__(self, vertices, edges):# Taken from: https://www.programiz.com/dsa/graph-adjacency-list
        self.V = vertices
        self.E = edges
        self.graph = [None] * self.V
     
    def add_edge(self, s, d):# Taken from: https://www.programiz.com/dsa/graph-adjacency-list
         node = AdjNode(d)
         node.next = self.graph[s]
         self.graph[s] = node
    
         node = AdjNode(s)
         node.next = self.graph[d]
         self.graph[d] = node
     
    def gaussianDistribution(self): # Based on: https://stackoverflow.com/questions/18441779/how-to-specify-upper-and-lower-limits-when-using-numpy-random-normal
        # Swapping to stats for the truncated normal distribution    
        lower, upper = 0, self.V
        mu, sigma = self.V/2, self.V/6
        X = stats.truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma) 
        return X
        
    def generateGaussianRandomGraph(self):
        # Create dictionary to prevent duplicate values
        existingEdges = {}
        lower, upper = 0, self.V
        mu, sigma = self.V/2, self.V/6
        for i in range (0, self.V): # Populate all vertices with empty arrays to signify no edges created 
            existingEdges[i] = []
        for i in range(0, self.E): 
            source = math.floor(stats.truncnorm.rvs((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size = 1 ))
            dest =  math.floor(stats.truncnorm.rvs((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size = 1))

            checkExisting = existingEdges.get(source, [-1]) # Get array of edges from that source
            
                
            while (source == dest) or (dest in checkExisting): # Re-roll if we have a duplicate edge or edge going nowhere
                source = math.floor(stats.truncnorm.rvs((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size = 1 ))
                dest =  math.floor(stats.truncnorm.rvs((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size = 1 ))
                checkExisting = existingEdges.get(source, -1)
            self.add_edge(source, dest)
            existingEdges[source] += [dest]#Add source and destination to existing edges
            existingEdges[dest] += [source]
        print(existingEdges)
        return existingEdges
    
    def print_agraph(self): # Need to modify this to fit the desired format
        edgeDictionary = self.generateGaussianRandomGraph()    
        print(self.V)
        print(self.V + 1) # Location of first node's edges
        
        # Commented section below handles the intro for the pointers
        
        totalWeight = 0
        for i in range(self.V -1):
            weight = len(edgeDictionary[i])
            totalWeight += weight
            print(self.V + 1 + totalWeight)
            
            
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                # print(" -> {}".format(temp.vertex), end="")
                print(temp.vertex)
                temp = temp.next          
if __name__ == "__main__": 

    vertexNumber = 5
    edgeNumber = 8
    runtimeCompleteStorage = []
    runtimeCycleStorage = []
    vStorage = []
    uniformRandomGraph = UniformRandomGraph(vertexNumber, edgeNumber)
    # uniformRandomGraph.print_agraph()
    
    skewedRandomGraph = SkewedRandomGraph(vertexNumber,edgeNumber)
    # skewedRandomGraph.print_agraph()
    
    gaussDistributionGraph = GaussianDistributionRandomGraph(vertexNumber, edgeNumber)
    gaussDistributionGraph.print_agraph()
    # for V in range(5,100): # For complete graph, it looks like n^2
    #     startComplete = time.time()
    #     completeGraph = CompleteGraph(V)
    #     completeGraph.all_edges()
    #     endComplete = time.time()
    #     runtimeComplete = endComplete - startComplete
        
    #     startCycle = time.time()
    #     cycle = CycleGraph(V)
    #     cycle.allEdgesInCycle()
    #     endCycle = time.time()
    #     runtimeCycle = endCycle - startCycle
        
    #     runtimeCompleteStorage.append(runtimeComplete)
    #     runtimeCycleStorage.append(runtimeCycle)
    #     vStorage.append(V)
        
        
        # print(runtime)
        
    # print("Output for Complete Graph with 5 Vertices:")
    # forCompletePrintTesting = CompleteGraph(5)
    # forCompletePrintTesting.all_edges()
    # forCompletePrintTesting.print_agraph()
    
    # print("\n")
    
    # print("Output for Cycle Graph with 5 Vertices:")
    # forCyclePrintTesting = CycleGraph(5)
    # forCyclePrintTesting.allEdgesInCycle()
    # forCyclePrintTesting.print_agraph()
        

    # plt.plot(vStorage, runtimeCompleteStorage)
    # plt.xlabel('Number of Items in Complete Graph')
    # plt.ylabel('Run Time (seconds)')
    # plt.title('Run Time vs Number of Items')
    
    # plt.plot(vStorage, runtimeCycleStorage)
    # plt.xlabel('Number of Items in Cycle')
    # plt.ylabel('Run Time (seconds)')
    # plt.title('Run Time vs Number of Items')
    

    

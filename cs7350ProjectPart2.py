# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:01:32 2022

@author: Max
"""
import numpy as np


class SLVO:
    def __init__(self, adjacencyList):
        self.List = adjacencyList
   
    def adjacencyListStringToDict(self): 
        listAsList = self.List.split('\t')
        numberVertices = int(listAsList[0])
        startPoints = listAsList[1 : numberVertices+1]
        edgesDict = {}
        edgeQuantityDict = {}
        for i in range(numberVertices -1) : 
            edgesDict[i] = listAsList[int(startPoints[i]) : int(startPoints[i+1])]
            edgeQuantityDict[i] = len(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
        edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] )-1 :-1]
        edgeQuantityDict[numberVertices -1] = len(listAsList[ int(startPoints[-1] )-1 :-1])
        # print(edgesDict)
        return edgesDict, edgeQuantityDict, numberVertices

    def minValueFromDict(self, d):
        minValue = min(d.values())
        minList = [key for key, value in d.items() if value == minValue]
        return minList[0] # For multiple acceptable items, just pick the first one 

    def removeMin(self, edgeList, edgeQuantity):
        keyForMinValue = self.minValueFromDict(edgeQuantity)
        smallestVertexEdges = edgeList.pop(keyForMinValue)
        edgeQuantity.pop(keyForMinValue) # Need to update edgeQuantity for next iteration

        for i in smallestVertexEdges:
            vertexEdge = edgeList[int(i)]
            # Is there a way for me to add 1 to the color value each time it is called? 
            vertexEdge.remove(str(keyForMinValue))
        return edgeList, edgeQuantity, keyForMinValue
    
    def organizeOutput(self):
        edges, edgeQuantity, numberVertices = self.adjacencyListStringToDict()
        originalEdges = edges
        keyOrder = []
        finalColor = {}
        currentColor = 0
        for i in range(numberVertices):
            edges, edgeQuantity, keyForMinValue = self.removeMin(edges, edgeQuantity)
            finalColor[keyForMinValue] = currentColor
            currentColor += 1
            keyOrder.insert(0, keyForMinValue)
            
        return keyOrder, finalColor
        
class SmallestOriginalDegreeLast:
    def __init__(self, adjacencyList):
        self.List = adjacencyList
   
    def adjacencyListStringToDictAndArray(self): 
        listAsList = self.List.split('\t')
        numberVertices = int(listAsList[0])
        startPoints = listAsList[1 : numberVertices+1]
        edges = []
        edgeQuantity = []
        edgesDict = {}
        edgeQuantityDict = {}
        for i in range(numberVertices -1) : 
            edges.append(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
            edgeQuantity.append(len(listAsList[int(startPoints[i]) : int(startPoints[i+1])]))
            edgesDict[i] = listAsList[int(startPoints[i]) : int(startPoints[i+1])]
            edgeQuantityDict[i] = len(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
        edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] )-1 :-1]
        edgeQuantityDict[numberVertices -1] = len(listAsList[ int(startPoints[-1] )-1 :-1])
        # print(edgesDict)
        return edgesDict, edgeQuantityDict, numberVertices, edges, edgeQuantity
    
    def dictionaryKeysToSortedArray(self, d):
        array = []
        for k in sorted(d, key=lambda k: len(d[k]), reverse=True):
            array.append(k)
        return array

class RandomOrder:
    def __init__(self, adjacencyList):
        self.List = adjacencyList
   
    def adjacencyListStringToDictAndArray(self): 
        listAsList = self.List.split('\t')
        numberVertices = int(listAsList[0])
        startPoints = listAsList[1 : numberVertices+1]
        edges = []
        edgeQuantity = []
        edgesDict = {}
        edgeQuantityDict = {}
        for i in range(numberVertices -1) : 
            edges.append(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
            edgeQuantity.append(len(listAsList[int(startPoints[i]) : int(startPoints[i+1])]))
            edgesDict[i] = listAsList[int(startPoints[i]) : int(startPoints[i+1])]
            edgeQuantityDict[i] = len(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
        edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] )-1 :-1]
        edgeQuantityDict[numberVertices -1] = len(listAsList[ int(startPoints[-1] )-1 :-1])
        return edgesDict, edgeQuantityDict, numberVertices, edges, edgeQuantity
    
    def takeKeysFromDictAndPutInArrayRandomly(self, dictionary):
        array = [-1] # need to insert a -1 into it so that randint doesn't get irritated that it needs to pick a number between 0 and 0 
        for k in dictionary:
            array.insert(np.random.randint(0, len(array)), k)
        array.remove(-1)
        return array
    
    
    
if __name__ == "__main__": 

    testCase1 = '5	6	9	11	15	19	3	2	4	3	2	0	1	3	4	0	1	4	2	3	0	2'
    testCase2 = '5	6	10	14	17	20	3	2	4	1	4	3	2	0	3	0	1	2	0	1	1	0'
    testCase3 = '5	6	9	13	17	20	1	2	3	4	0	3	2	0	3	4	1	1	2	0	1	2'
    testCase4 = '5	6	8	10	12	14	4	1	2	0	3	1	4	2	0	3'
    testCase5 = '5	6	10	14	18	22	4	3	2	1	4	3	2	0	4	3	1	0	4	2	1	0	3	2	1	0'
    
    slvo = SLVO(testCase1)
    keyorder, finalcolor = slvo.organizeOutput()
    
    smallestOriginalDegreeLast = SmallestOriginalDegreeLast(testCase1)
    edgesDict, edgesQuantityDict, numberVertices, edges, edgeQuantity = smallestOriginalDegreeLast.adjacencyListStringToDictAndArray()
    sortedEdges = smallestOriginalDegreeLast.dictionaryKeysToSortedArray(edgesDict)
    
    randomOrder = RandomOrder(testCase1)
    edgesDict, edgeQuantityDict, numberVertices, edges, edgeQuantity = randomOrder.adjacencyListStringToDictAndArray()
    print(randomOrder.takeKeysFromDictAndPutInArrayRandomly(edgesDict))
    # print(edges)
    # print(edgeQuantity)
    # print(edges)
    # print(edgeQuantity)

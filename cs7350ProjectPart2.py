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
    
class BiggestLastVertexOrdering:
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

    def maxValueFromDict(self, d):
        maxValue = max(d.values())
        maxList = [key for key, value in d.items() if value == maxValue]
        return maxList[0] # For multiple acceptable items, just pick the first one 

    def removeMax(self, edgeList, edgeQuantity):
        keyForMaxValue = self.maxValueFromDict(edgeQuantity)
        largestVertexEdges = edgeList.pop(keyForMaxValue)
        edgeQuantity.pop(keyForMaxValue) # Need to update edgeQuantity for next iteration

        for i in largestVertexEdges:
            vertexEdge = edgeList[int(i)]
            # Is there a way for me to add 1 to the color value each time it is called? 
            vertexEdge.remove(str(keyForMaxValue))
        return edgeList, edgeQuantity, keyForMaxValue
    
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
class BiggestOriginalDegreeLast:
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
        for k in sorted(d, key=lambda k: len(d[k]), reverse=False):
            array.append(k)
        return array
class VerticesOrganizedAlphabetically:
    def __init__(self, adjacencyList):
        self.List = adjacencyList

"""Given an int32 number, print it in English."""
def int_to_en(num): # Taken from https://stackoverflow.com/questions/8982163/how-do-i-tell-python-to-convert-integers-into-words
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' thousand'
        else: return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' million'
        else: return int_to_en(num // m) + ' million, ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' billion'
        else: return int_to_en(num // b) + ' billion, ' + int_to_en(num % b)

    if (num % t == 0): return int_to_en(num // t) + ' trillion'
    else: return int_to_en(num // t) + ' trillion, ' + int_to_en(num % t)

    raise AssertionError('num is too large: %s' % str(num))
    
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

    biggestLastVertexOrder = BiggestLastVertexOrdering(testCase1)
    keyOrderBLVO, finalcolor = biggestLastVertexOrder.organizeOutput()
    print(keyOrderBLVO)
    # print(edges)
    # print(edgeQuantity)
    # print(edges)
    # print(edgeQuantity)

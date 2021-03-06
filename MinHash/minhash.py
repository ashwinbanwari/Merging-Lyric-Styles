from __future__ import division

import pickle
from heapq import heapify,heappop,heappush
import random

random.seed(0)

totalShingles = 2400
pklHandler = open("docShingleDict.pkl", 'rb')
docShingleDict= pickle.load(pklHandler)
pklHandler.close()

def findRandomNos(k):
  randList = []
  randIndex = random.randint(0, totalShingles -1) 
  randList.append(randIndex)
  while k>0:
    while randIndex in randList:
      randIndex = random.randint(0, totalShingles-1) 
      
    randList.append(randIndex)
    k = k-1
    
  return randList
  
randomNoA = findRandomNos(25)
randomNoB = findRandomNos(25)

docLowestShingleID = {}
for doc in docShingleDict:
  shingleIDSet = docShingleDict[doc]
  lowestShingleID = []
  for x in range(0,25):
    listFx = []
    for shingleID in shingleIDSet:
      temp = (randomNoA[x] * shingleID + randomNoB[x]) % totalShingles 
      listFx.append(temp)
    heapify(listFx)
    lowestShingleID.append(heappop(listFx))
  docLowestShingleID[doc] = lowestShingleID

#for doc in docLowestShingleID:
#  print doc, docLowestShingleID[doc]

def getFileNo(x):
  if x<10:
    x = "0" + str(x)
  else:
    x = str(x)
  
  return x

estimateMatrix = []
for x in range(0,16):
  doc1 = "file"+getFileNo(x)
  doc1LowestShingles = docLowestShingleID[doc1]
  col = []
  for y in range(0,16):
    doc2 = "file"+getFileNo(y)
    doc2LowestShingles = docLowestShingleID[doc2]
    count = 0
    for i in range(0,25):
      if doc1LowestShingles[i] == doc2LowestShingles[i]:
        count = count + 1
        
    col.append(count/25)
  estimateMatrix.append(col)
  
print("\nList of Documents with J(d1,d2) more than 0.45")
for x in range(0,16):
  file1 = "file" + getFileNo(x)
  for y in range(x,16):
    if estimateMatrix[x][y] > 0.45:
      file2 = "file" + getFileNo(y)
      if file1 != file2:
        shinglesSet1 = docShingleDict[file1]
        shinglesSet2 = docShingleDict[file2]
        print("d1: " + file1 + " and d2: " + file2)
        print("J(d1,d2): " + str(estimateMatrix[x][y]))
        jaccard = (len(shinglesSet1.intersection(shinglesSet2)) / len(shinglesSet1.union(shinglesSet2)))
        print("Jaccard coefficient: ", str(jaccard))
        print()

docJaccard = {}

def pop(jaccardList):
  estimatedJaccardC, fileX = heappop(jaccardList)
  print((estimatedJaccardC, fileX))

print("Nearest neighbors for the generated lyrics")

for x in range(0,1):
  file1 = "file" + getFileNo(x)
  estimatedJaccardList = []
  for y in range(0,16):
    file2 = "file" + getFileNo(y)
    if file1 != file2:
      heappush(estimatedJaccardList, (-estimateMatrix[x][y], file2))
  
  #print estimatedJaccardList
  print("\n" + file1 + ":",)
  for x in range(0,5):
    pop(estimatedJaccardList)
    
  



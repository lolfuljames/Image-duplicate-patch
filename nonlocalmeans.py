from scipy import misc
from PIL import Image as img
import numpy as np
import time
start_time = time.time()

nameOfFile = "panda.JPG"
original = misc.imread(nameOfFile)
imageSize = original.shape
patchSize = 5
windowSize = 3
patchArray = []
global counter #counter for debugging, counts number of comparisons
counter = 0
MODE = 0
THRESHOLD = 0.2

class Patch:
	def __init__(self, X=0, Y=0, mode=MODE, threshold=THRESHOLD, patchSize=5, windowSize=5): #mode = 0 is normal threshold, mode = 1 is minimum patch number
		self.patchSize = patchSize
		self.windowSize = windowSize
		self.X = X
		self.Y = Y
		self.threshold = threshold
		self.mode = mode
		self.array = np.zeros((patchSize,patchSize,3)) #3 for RGB, 4 for RGB+intensity

	def setX(self,X):
		self.X = X

	def setY(self,Y):
		self.Y = Y

	def setArray(self,array):
		self.array = np.copy(array)


def generateArrays(original,patchArray,patchSize): #converts images and organise them into an matrix of patches
	for i in range(0,imageSize[0],patchSize):
		patchArray.append([])
		for j in range(0,imageSize[1],patchSize):
			patchArray[(i+1)/patchSize].append(np.copy(original[i:i+patchSize,j:j+patchSize]))

def checkMeanMode0(patchArray, patch, cloneArray): #sliding window patch nl mean checking hits minimum threshold
	global counter
	for i in range(max(0,patch.X-patch.windowSize),min(patch.X+patch.windowSize+1,len(patchArray))):

		for j in range(max(0,patch.Y-patch.windowSize),min(patch.Y+patch.windowSize+1,len(patchArray))):
			counter += 1
			if(i==patch.X and j==patch.Y):
				continue
			else:
				differenceArray = np.subtract(patchArray[i][j],patch.array)
				if (np.linalg.norm(differenceArray)/255<patch.threshold):
					cloneArray[patch.X][patch.Y].append(np.copy(patchArray[i][j]))

def checkMeanMode1(patchArray, patch, cloneArray,thresholdArray): #sliding window patch nl mean checking
	global counter
	for i in range(max(0,patch.X-patch.windowSize),min(patch.X+patch.windowSize+1,len(patchArray))):
		for j in range(max(0,patch.Y-patch.windowSize),min(patch.Y+patch.windowSize+1,len(patchArray))):
			counter += 1
			if(i==patch.X and j==patch.Y):
				continue
			else:
				differenceArray = np.subtract(patchArray[i][j],patch.array)
				difference = np.linalg.norm(differenceArray)
				thresholdArray[patch.X][patch.Y].append(difference)
				thresholdArray[patch.X][patch.Y].sort()
				index = thresholdArray[patch.X][patch.Y].index(difference)
				if(index<patch.threshold):
					cloneArray[patch.X][patch.Y].insert(index, patchArray[i][j])#either can try compare if >10 then don't add, or just add anythow

patch = Patch(patchSize)
generateArrays(original,patchArray,patchSize)
cloneArray = [[[] for x in range(len(patchArray))] for y in range(len(patchArray[0]))] #array to see which arrays meet minimum threshold
thresholdArray = [[[] for x in range(len(patchArray))]for y in range(len(patchArray[0]))]

if(patch.mode==0):
	for i in range(64):
		for j in range(64):
			patch = Patch()
			patch.setX(i)
			patch.setY(j)
			# print(patch.X,patch.Y)
			patch.setArray(patchArray[i][j])
			checkMeanMode0(patchArray,patch,cloneArray)

else:
	for i in range(64):
		for j in range(64):
			patch = Patch()
			patch.setX(i)
			patch.setY(j)
			# print(patch.X,patch.Y)
			patch.setArray(patchArray[i][j])
			checkMeanMode1(patchArray,patch,cloneArray,thresholdArray)

print("--- %s seconds ---" % (time.time() - start_time))
while(1):
	pass
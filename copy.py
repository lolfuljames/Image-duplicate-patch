from scipy import misc
from PIL import Image as img
import numpy as np

def main(nameOfFile,patchSize,duplicatePixelCount):
	if(patchSize==duplicatePixelCount):
		return
	if(patchSize<=0 or duplicatePixelCount<0):
		return
	original = misc.imread(nameOfFile)
	matrixSize = original.shape
	originalImage = img.fromarray(original,'RGB')
	patch(original,matrixSize,patchSize,duplicatePixelCount)
	########################
	# INITIAL TESTING CODE #
	# if (input("1 for pixel,2 for patch\n")==1):
	# 	pixel1(original,matrixSize)
	# else:
	# 	patch(original,matrixSize,patchSize,duplicatePixelCount)
	########################

def pixel1(original,matrixSize):

	############# pixel by pixel no patch ##############
	cloneArray = np.zeros(matrixSize)

	for i in range (0,matrixSize[0],1):
		for j in range(0,matrixSize[1],1):
				cloneArray[i][j]=original[i][j]

	printImage(cloneArray)
	#############

def patch(original,matrixSize,patchSize,duplicatePixelCount):

	if(matrixSize[0]%(patchSize-duplicatePixelCount)!=0):
		return
	newSize =(matrixSize[0]/(patchSize-duplicatePixelCount)*patchSize, matrixSize[1]/(patchSize-duplicatePixelCount)*patchSize, matrixSize[2])
	cloneArray = np.zeros(newSize)
	patchArray = np.zeros((patchSize,patchSize,matrixSize[2]))
	patchArray = np.uint8(patchArray)

	cloneX = 0;
	cloneY = 0;

	############# matrixSize-patchSize+duplicatePixelCount would make it end so that the borders aren't copied twice ###########

	for i in range(0,matrixSize[0]-patchSize+duplicatePixelCount,patchSize-duplicatePixelCount): #looping  outer patch x
		for j in range(0,matrixSize[1]-patchSize+duplicatePixelCount,patchSize-duplicatePixelCount):#looping outer patch y 
			# print("i: " + str(i) + "j: " + str(j) + "cloneX: " + str(cloneX) + "cloneY: "+ str(cloneY))
			patchArray=np.copy(original[i:i+patchSize,j:j+patchSize])#copy into patch from original
			cloneArray[cloneX:cloneX+patchSize,cloneY:cloneY+patchSize]=np.copy(patchArray)#copy into clone from patch
			cloneY += patchSize
		cloneX += patchSize
		cloneY = 0
	cloneX = 0
	printImage(cloneArray) #cloneX and Y are additional counters for new cloned coordinates

def printImage(array):
	array = np.uint8(array)
	image = img.fromarray(array,'RGB')
	image.show()
	return image


					
while(1):
	patchSize = input("Enter patching size: (-1 to exit) \n")
	if(patchSize == -1):
		print("Good stuff mate")
		break
	nameOfFile = "panda.JPG"
	duplicatePixelCount = input("Enter duplicate count: \n")
	main(nameOfFile,patchSize,duplicatePixelCount)
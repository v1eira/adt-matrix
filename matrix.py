def createMatrix(lines, columns, value = 0):
	matrix = []
	for i in range(lines):
		line = []
		for j in range(columns):
			line.append(value)
		matrix.append(line)
	
	return matrix
#end createMatrix


def checkIsMatrix(matrix):
	for i in range(len(matrix)):
		if len(matrix[i]) != len(matrix[0]):
			return False
	
	return True
#end checkIsMatrix


def printMatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print("%.d " % matrix[i][j], end="")
		print("\n")
#end printMatrix


def multiplyMatrix(matrixA, matrixB):
	if checkIsMatrix(matrixA) == checkIsMatrix(matrixB) == True:
		if len(matrixA[0]) == len(matrixB):				
			matrix = createMatrix(len(matrixA), len(matrixB[0]))
			for i in range(len(matrixA)):
				for j in range(len(matrixB[i])):
					for k in range(len(matrixB[i])):
						matrix[i][j] += matrixA[i][k] * matrixB[k][j]
		
	return matrix
#end multiplyMatrix


# ~ def sumMatrix(matrixA, matrixB):
# ~ #end sumMatrix


# ~ def divideMatrix(matrixA, matrixB):
# ~ #end divideMatrix


def rotateColumnLeft(matrix, times = 1):
	for x in range(times):
		for i in range(len(matrix)):
			for j in range(len(matrix[i])-1):
				original = matrix[i][j]
				matrix[i][j] = matrix[i][j+1]
				matrix[i][j+1] = original
	
	return matrix
#end rotateColumnLeft


def rotateColumnRight(matrix, times = 1):
	for x in range(times):
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				original = matrix[i][j]
				matrix[i][j] = matrix[i][len(matrix[i])-1]
				matrix[i][len(matrix[i])-1] = original
	
	return matrix
#end rotateColumnRight

def rotateLineUp(matrix, times = 1):
	for x in range(times):
		for i in range(len(matrix)-1):
			original = matrix[i]
			matrix[i] = matrix[i+1]
			matrix[i+1] = original
	
	return matrix

#end rotateLineUp


def rotateLineDown(matrix, times = 1):
	for x in range(times):
		for i in range(len(matrix)-1):
			original = matrix[i]
			matrix[i] = matrix[len(matrix)-1]
			matrix[len(matrix)-1] = original

	return matrix
#end rotateLineDown


def sumElements(matrix):
	total = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			total += matrix[i][j]
	
	return total
#end sumElements


def multiplyElements(matrix, value):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			matrix[i][j] *= value
	
	return matrix
#end multiplyElements


def divideElements(matrix, value):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			matrix[i][j] /= value
	
	return matrix
#end divideElements


def sqrtElements(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			matrix[i][j] = matrix[i][j]**(1/2)

	return matrix
#end sqrtElements


def addToElements(matrix, value):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			matrix[i][j] += value
	
	return matrix
#end addToElements


def minValue(matrix):
	minimum = matrix[0][0]
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] < minimum:
				minimum = matrix[i][j]
	
	return minimum
#end minValue


def maxValue(matrix):
	maximum = matrix[0][0]
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] > maximum:
				maximum = matrix[i][j]
	
	return maximum
#end maxValue


def meanValue(matrix):
	total = sumElements(matrix)
	
	return (total/(len(matrix)*len(matrix[0])))
#end meanValue


def main():
	matrix = [[1,4,2,4,4], [2,1,4,4,9], [9,4,4,1,25], [2,4,9,9,36]]

	printMatrix(matrix)

	print("- - - - - - - - - -\n")

	matrix = rotateColumnLeft(matrix)
	printMatrix(matrix)

	print("- - - - - - - - - -\n")

	matrix = rotateColumnRight(matrix)
	printMatrix(matrix)

	print("- - - - - - - - - -\n")

	matrix = rotateLineUp(matrix)
	printMatrix(matrix)

	print("- - - - - - - - - -\n")
	matrix = rotateLineDown(matrix)
	printMatrix(matrix)

	print("- - - - - - - - - -\n")
	matrix = divideElements(matrix, 2)
	printMatrix(matrix)


if __name__ == '__main__':
    import sys
    sys.exit(main())

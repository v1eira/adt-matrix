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
			print("%d " % matrix[i][j], end="")
		print("\n")
#end printMatrix


def multiplyElements(matrix, num):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			matrix[i][j] *= num
	
	return matrix
#end multiplyElements


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


def rotateColumnLeft(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])-1):
			original = matrix[i][j]
			matrix[i][j] = matrix[i][j+1]
			matrix[i][j+1] = original
	
	return matrix
#end rotateColumnLeft


def rotateColumnRight(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			original = matrix[i][j]
			matrix[i][j] = matrix[i][len(matrix[i])-1]
			matrix[i][len(matrix[i])-1] = original
	
	return matrix
#end rotateColumnRight


def sumElements(matrix):
	total = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			total += matrix[i][j]
	
	return total
#end sumElements


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
			

# ~ def sqrtElements(matrix):
# ~ #end sqrtElements


# ~ def sumMatrix(matrixA, matrixB):
# ~ #end sumMatrix


# ~ def divideMatrix(matrixA, matrixB):
# ~ #end divideMatrix

# ~ def rotateLineUp(matrix):
# ~ #end rotateLineUp


# ~ def rotateLineDown(matrix):
# ~ #end rotateLineDown


def main():
    mat = [[1,2], [3,4]]
    mat2 = [[-1,3], [4,2]]
    
    matrix = multiplyMatrix(mat, mat2)
    
    printMatrix(matrix)
    
    print("- - -")
    
    matrix = multiplyElements(mat, 2)
    
    printMatrix(matrix)
    
    print("- - -")
    
    matrix = [[1,2,2,3,7], [2,1,3,4,3], [4,3,3,1,5], [2,4,3,3,6]]
    
    printMatrix(matrix)
    
    print("\n\n")
    
    matrix = rotateColumnLeft(matrix)
    
    printMatrix(matrix)
    
    matrix = addToElements(matrix, 1)
    
    print("\n\n")
    
    printMatrix(matrix)
    
    print(sumElements(matrix))
    print(minValue(matrix))
    print(maxValue(matrix))
    print(meanValue(matrix))
    

if __name__ == '__main__':
    import sys
    sys.exit(main())

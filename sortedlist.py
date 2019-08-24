class SortedList:
	def __init__(self, L = [], cmpIn = None):
		self._L = L
		self._cmp = cmpIn
		self.ctComparisons = 0
		self.selectionSort()

	# Selection sort provided to you
	def selectionSort(self):
		self.ctComparisons = 0
		for i in range(len(self._L)):
			min_idx = i
			for j in range(i+1, len(self._L)):
				if self._compare(self._L[min_idx], self._L[j]) == 1:
					min_idx = j
			self._L[i], self._L[min_idx] = self._L[min_idx], self._L[i]

	def add(self, item):
		self.ctComparisons = 0
		if len(self._L) == 0:
			self._L.append(item)
		else:
			for index in range(len(self._L)):
				if self._compare(item, self._L[index]) == -1: #The item is smaller than the current value
					self._L.insert(index, item)
					break
				elif index+1 == len(self._L):
					self._L.append(item)

	def _compare(self, i, j):
		self.ctComparisons += 1
		if self._cmp != None:
			return self._cmp(i, j)
		else:
			if i > j:
				return 1
			elif i == j:
				return 0
			else:
				return -1

	def setComparison(self, cmpFunction):
		self._cmp = cmpFunction
		self.selectionSort()

	def mergeSort(self, L, zeroFlag = True):
		if zeroFlag:
			self.ctComparisons = 0
			zeroFlag = False
		if len(L) < 2:
			return L
		else:
			half = len(L)//2
			L1 = L[half:]
			L2 = L[:half]
			self.mergeSort(L1, zeroFlag)
			self.mergeSort(L2, zeroFlag)
			self.merge(L1, L2, L)
		# if self.ctComparisons == 17:
		# 	self.ctComparisons += 1

	def merge(self, A, B, L):
		i = 0
		j = 0
		while i < len(A) and j < len(B):
			if self._compare(A[i], B[j]) == 1: #If A[i] > B[i]
				L[i+j] = B[j]
				j += 1
			else:
				L[i+j] = A[i]
				i += 1
		L[i+j:] = A[i:] + B[j:]

	def __contains__(self, item):
		found = False
		self.ctComparisons = 0
		trueStart = 0
		trueEnd = len(self._L) -1
		start = 0
		end = len(self._L) -1 #End = 4 - 1 = 3
		while not found and start <= end:
			mid = int((start + end)/2) #Mid = (0+3)/2 = 3/2 = 1
			x = self._compare(self._L[mid], item)
			if x == 0: #Found the item
				found = True
			elif x == -1: #Item in upper half of the list
				start = mid+1
			else:
				end = mid-1
		return found

	def __str__(self):
		return str(self._L)

## DO NOT modify these functions. They are the comparison functions for testing purposes.

def cmpBySum(i, j):
	sum1 = 0
	sum2 = 0
	while i > 0:
		d = i%10
		i = i//10
		sum1 += d
	while j > 0:
		d = j%10
		j = j//10
		sum2 += d
	if sum1 < sum2:
		return -1
	elif sum1 == sum2:
		return 0
	else:
		return 1

def ageCmp(i, j):
	i = i[2]
	j = j[2]
	if i < j:
		return -1
	elif i == j:
		return 0
	else:
		return 1

def nameCmp(x, y):
	x = x[1]
	y = y[1]
	n = min(len(x), len(y))
	for i in range(n):
		if x[i] < y[i]:
			return -1
		elif x[i] > y[i]:
			return 1
		elif i == n-1 and x[i] == y[i]:
			return 0

def stringLenCmp(x, y):
	if len(x) < len(y):
		return -1
	elif len(x) == len(y):
		return 0
	else:
		return 1

sl = SortedList([22, 20, 12, 2, 4, 6, 4, 2, 0, -1, -3])
print(sl.ctComparisons, 55)

sl.mergeSort(sl._L)
print(sl.ctComparisons, 18)

sl = SortedList([6, 8, -2, 0, 1, -6])
print(sl.ctComparisons, 15)

sl.mergeSort(sl._L)
print(sl.ctComparisons, 7)

sl = SortedList([4, 10, -20, -3, 5, 8, 2, 2])
print(sl.ctComparisons, 28)

sl.mergeSort(sl._L)
print(sl.ctComparisons, 12)

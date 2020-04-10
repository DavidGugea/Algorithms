import random
import pprint 
import time
import sys # sys.setrecursionlimit() | We will use it to avoid RecursionError for quick sort 


def spaceUp(n):
	for i in range(n):
		print()

class QuickSort(object):
	def __init__(self, arr):
		self.arr = arr
	def medianOfThree(self, arr, low, high):
		if len(arr) >= 3:
			# Create the Start Middle End array
			start_middle_end = [ arr[low], arr[ ( low + high ) // 2 ], arr[high] ]
			# Sort it
			start_middle_end.sort()

			# Return the index of the middle value
			return arr.index(start_middle_end[1])
		else:
			return random.randint(low, high)
	def partitionStandard(self, arr, low, high):
		# For the standrad quick sort, pick the pivot as the last element of the array
		pivot = arr[high]
		
		# Create memory value ( i ) and set it to low - 1 | Create scan value ( j ) and set it to low
		i, j = low - 1, low
		
		# Scan through all the values of the array
		while j < high:
			if arr[j] < pivot:
				# Increment memory value
				i += 1
				# Swap [i] with [j]
				arr[i], arr[j] = arr[j], arr[i]

			# Increment scan value
			j += 1

		# Swap [i + 1] with the pivot ( pivot index is the last index from the array -- > high )
		arr[i + 1], arr[high] = arr[high], arr[i + 1]
	
		# Return border split index value ( i + 1, where the pivot was placed )
		return i + 1
	def partitionStrategy(self, arr, low, high, strategy):
		'''
		~ Get the pivot index
			# strategy == 'random' => random pivot strategy ( pick a random index for the pivot )
			# strategy == 'medianOfThree' => median of three strategy ( pick the index for the pivot using self.medianOfThree(*args) 
		'''
		if strategy == 'random':
			pivotIndex = random.randint(low, high)
		elif strategy == 'medianOfThree':
			pivotIndex = self.medianOfThree(arr, low, high)
		
		# Get the pivot value
		pivot = arr[pivotIndex]

		# Swap the pivot with the last value from the array to get the pivot from our way
		arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]
		# Update the pivot index
		pivotIndex = high

		# Create the scan values ( LS & RS )
		LS = low	# Left scan value  ( > pivot ) 
		RS = high - 1   # Right scan value ( < pivot )

		while LS <= RS:
			if arr[LS] > pivot and arr[RS] < pivot:
				# Swap [LS] with [RS]
				arr[LS], arr[RS] = arr[RS], arr[LS]
				
				# Increment left scan value
				LS += 1
				# Decrement right scan value
				RS -= 1
			else:
				if arr[LS] < pivot:
					# Increment left scan value
					LS += 1
				if arr[RS] > pivot:
					# Decrement right scan value
					RS -= 1

		# Swap [LS] with pivot value
		arr[LS], arr[pivotIndex] = arr[pivotIndex], arr[LS]
		
		# Return border split value 
		return LS
	def quickSort(self, arr, low, high, strategy):
		if low < high:
			if strategy == "standard":
				partitionBorderSplit_IndexValue = self.partitionStandard(arr, low, high)
			else:	
				partitionBorderSplit_IndexValue = self.partitionStrategy(arr, low, high, strategy)
			
			self.quickSort(arr, partitionBorderSplit_IndexValue + 1, high, strategy)
			self.quickSort(arr, low, partitionBorderSplit_IndexValue - 1, strategy) 
	
def analyseBehaviorAndRuntime():
	# Arrays to analyse 
	array0 = None  # Standard strategy
	array1 = None  # Random pivot strategy
	array2 = None  # The median of three strategy

	while True:
		# Ask the user if he wants to give an array or the amount of elements that will be completly unsorted ( [::-1] )
		print("1. Give an array that you want to sort")
		print("2. Give a number of elements that will be completely unsorted in an array")

		userChoice = input("> ")

		try:
			# Check user input
			userChoice = eval(userChoice)

			if userChoice not in list(range(1, 3)):
				raise Exception
			else:
				if userChoice == 1:
					# Given array	
					while True:
						userGivenArray = input("Write here the array that you want to sort with all different strategies ( e. g : [3, 2, 1] ) -- > ")
						
						try:
							# Check user input for the given array
							userGivenArray = eval(userGivenArray)

							# Try to see if the ".append()" method is in the userGivenArray, if that is the case then we know the user gave us a list as input
							if userGivenArray.append:
								# The user gave us a list, so all the arrays ( 0 1 and 2 ) will be this list
								array0 = userGivenArray.copy()
								array1 = userGivenArray.copy() 
								array2 = userGivenArray.copy()
								break
							raise Exception
						except Exception:
							print("The input must be an array ( e. g : [3, 2, 1] )")
							spaceUp(2)
							continue
				elif userChoice == 2:
					# Amount of items
					while True:
						amountOfItems = input("Write here the amount of items that you want your array to have that will be completely unsorted -- > ")

						try:
							# Check user input
							amountOfItems = int(amountOfItems)

							if amountOfItems <= 0:
								raise Exception
							else:
								array0 = list(range(1, amountOfItems + 1, 1))[::-1]
								array1 = array0.copy()
								array2 = array0.copy()

								break
						except Exception:
							print("Your amount of items must be a positive integer bigger than 0")
							spaceUp(2)
							continue

			break
		except Exception:
			print("Choose something between 1 and 2")
			spaceUp(2)

	# See if the user wants to see the sorted arrays
	seeArrays = None
	while True:
		userInput = input("Do you want to see the sorted arrays ( y | n ) -- > ")

		if userInput.lower() == "y" or userInput.lower() == "yes":
			seeArrays = True
		elif userInput.lower() == "n" or userInput.lower() == "no":
			seeArrays = False
		else:
			print("Choose something between y ( yes ) or n ( no )")
			spaceUp(2)
			continue

		break

	spaceUp(5)

	# Create the quick sort objects
	QuickSort_StandardAlgorithm = QuickSort(array0)
	QuickSort_RandomPivot_Strategy = QuickSort(array1)
	QuickSort_TheMedianOfThree_Strategy = QuickSort(array2)

	sys.setrecursionlimit(pow(len(array0), 2)) # Set the recursion limit to another number in order to avoid RecursionError for quick sort

	if seeArrays:
		print("***** STANDARD ALGORITHM *****")
		spaceUp(3)

		print("Array before quick sort -- > ")
		pprint.pprint(array0, indent = 20)

		startTime_QuickSort_StandardAlgorithm = time.perf_counter()
		QuickSort_StandardAlgorithm.quickSort(array0, 0, len(array0) - 1, 'standard')
		timeNeeded_QuickSort_StandardAlgorithm = time.perf_counter() - startTime_QuickSort_StandardAlgorithm

		print("Array after quick sort -- > ")
		pprint.pprint(array0, indent = 20)

		spaceUp(3)
		print("***** STANDARD ALGORITHM *****")
		spaceUp(5)
		print("***** RANDOM PIVOT STRATEGY *****")
		spaceUp(3)

		print("Array before quick sort -- > ")
		pprint.pprint(array1, indent = 20)

		startTime_QuickSort_RandomPivotStrategy = time.perf_counter()
		QuickSort_RandomPivot_Strategy.quickSort(array1, 0, len(array1) - 1, 'random')
		timeNeeded_QuickSort_RandomPivot_Strategy = time.perf_counter() - startTime_QuickSort_RandomPivotStrategy

		print("Array after quick sort -- > ")
		pprint.pprint(array1, indent = 20)

		spaceUp(3)
		print("***** RANDOM PIVOT STRATEGY *****")
		spaceUp(5)
		print("***** THE MEDIAN OF THREE STRATEGY *****")
		spaceUp(3)
		
		print("Array before quick sort -- >")
		pprint.pprint(array2, indent = 20)

		startTime_QuickSort_TheMedianOfThreeStrategy = time.perf_counter()
		QuickSort_TheMedianOfThree_Strategy.quickSort(array2, 0, len(array2) - 1, 'medianOfThree')
		timeNeeded_QuickSort_TheMedianOfThree_Strategy = time.perf_counter() - startTime_QuickSort_TheMedianOfThreeStrategy

		print("Array after quick sort -- > ")
		pprint.pprint(array2, indent = 20)

		spaceUp(3)
		print("***** THE MEDIAN OF THREE STRATEGY *****")
		
		spaceUp(15)
		print("Runtime behavior for : ")
		print(" ~ Standard algorithm           -- > {0}".format(timeNeeded_QuickSort_StandardAlgorithm))
		print(" ~ Random pivot strategy        -- > {0}".format(timeNeeded_QuickSort_RandomPivot_Strategy))
		print(" ~ The Median Of Three strategy -- > {0}".format(timeNeeded_QuickSort_TheMedianOfThree_Strategy))
	elif not seeArrays:
		startTime_QuickSort_StandardAlgorithm = time.perf_counter()
		QuickSort_StandardAlgorithm.quickSort(array0, 0, len(array0) - 1, 'standard')
		timeNeeded_QuickSort_StandardAlgorithm = time.perf_counter() - startTime_QuickSort_StandardAlgorithm

		startTime_QuickSort_RandomPivot_Strategy = time.perf_counter()
		QuickSort_RandomPivot_Strategy.quickSort(array1, 0, len(array1) - 1, 'random')
		timeNeeded_QuickSort_RandomPivot_Strategy = time.perf_counter() - startTime_QuickSort_RandomPivot_Strategy

		startTime_QuickSort_TheMedianOfThree_Strategy = time.perf_counter()
		QuickSort_TheMedianOfThree_Strategy.quickSort(array2, 0, len(array2) - 1, 'medianOfThree')
		timeNeeded_QuickSort_TheMedianOfThree_Strategy = time.perf_counter() - startTime_QuickSort_TheMedianOfThree_Strategy


		print("Runtime behavior for : ")
		print(" ~ Standard algorithm           -- > {0}".format(timeNeeded_QuickSort_StandardAlgorithm))
		print(" ~ Random pivot strategy        -- > {0}".format(timeNeeded_QuickSort_RandomPivot_Strategy))
		print(" ~ The Median Of Three strategy -- > {0}".format(timeNeeded_QuickSort_TheMedianOfThree_Strategy))


while True:
	spaceUp(10)

	print("Choose something : ")
	print("1. Analyse runtime and behavior for the quick sort strategies")
	print("2. Exit")

	userChoice = input("> ")
	
	try:
		# Check user input
		userChoice = eval(userChoice)

		if userChoice not in list(range(1, 3)):
			raise Exception	
	
		if userChoice == 1:
			spaceUp(10)
			analyseBehaviorAndRuntime()
			spaceUp(5)
		elif userChoice == 2:
			break
	except Exception as _e_:
		print("Error -- > {0}".format(str(_e_)))
		print("Choose something between 1 and 2")
		continue
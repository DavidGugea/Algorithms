import random
import pprint

def medianOfThree(arr, low, high):
	if len(arr) >= 3:
		# Get the first-, middle- and end value from the array
		stop_middle_end = [ arr[low], arr[ ( low + high ) // 2 ], arr[high] ]
		# Sort the array
		stop_middle_end.sort()

		# Return the index of middle value
		return arr.index(stop_middle_end[1])
	else:
		return random.randint(low, high)
def partition(arr, low, high):
	# Get the pivot index ( index of the median of three in the array )
	pivotIndex = medianOfThree(arr, low, high)
	# Get the pivot
	pivot = arr[pivotIndex]

	# Swap the pivot with the last element from the array to get it from our way
	arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]
	# Update the pivot index
	pivotIndex = high

	# Create scan values
	LC = low 	# Left scan value   ( > pivot )
	RC = high - 1	# Right scan value  ( < pivot )

	while LC <= RC:
		if arr[LC] > pivot and arr[RC] < pivot:
			# Swap [LC] with [RC]
			arr[LC], arr[RC] = arr[RC], arr[LC]
			
			# Increment left scan value
			LC += 1
			# Decrement right scan value
			RC -= 1
		else:
			if arr[LC] < pivot:
				# Increment left scan value
				LC += 1
			if arr[RC] > pivot:
				# Decrement right scan value
				RC -= 1

	# Swap [LC] with the [pivotIndex] ( pivot )
	arr[LC], arr[pivotIndex] = arr[pivotIndex], arr[LC]
	
	# Return pivot border value ( LC )
	return LC
def quickSort(arr, low, high):
	if low < high:
		pivotSplitBorder_IndexValue = partition(arr, low, high)
		
		quickSort(arr, pivotSplitBorder_IndexValue + 1, high)
		quickSort(arr, low, pivotSplitBorder_IndexValue - 1)

# Create array
array = list(range(1, 11))[::-1]
print("Array before sort: ")
pprint.pprint(array, indent=10)

for i in range(10):
	print()

print("Array after sort : ")
quickSort(array, 0, len(array) - 1)
pprint.pprint(array, indent = 10)

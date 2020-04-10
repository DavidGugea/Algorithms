import random
import pprint

def partition(arr, low, high):
	# Get the pivot index
	pivotIndex = random.randint(low, high)
	# Get the pivot value
	pivot = arr[pivotIndex]

	# Swap the pivot value with the last value from the array to get it from our way
	arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]
	# Update the pivotIndex
	pivotIndex = high

	# Create the scan values ( LS & RS )
	LS = low	# Left scan value   ( > pivot )
	RS = high - 1	# Right scan value  ( < pivot )

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

	# Return the pivot border value
	return LS
def quickSort(arr, low, high):
	if low < high:
		# Get the pivot border split index value	
		pivotBorderSplit_IndexValue = partition(arr, low, high)
		
		# Call quicksort on each halves of the pivot border index value
		quickSort(arr, pivotBorderSplit_IndexValue + 1, high)
		quickSort(arr, low, pivotBorderSplit_IndexValue - 1)

# Create an array
array = list(range(1, 11))[::-1] 

print("Before quick sort -- > ")
pprint.pprint(array, indent=10)

for i in range(10):
	print()

print("After quick sort -- > ")
quickSort(array, 0, len(array) - 1)
pprint.pprint(array, indent=10)
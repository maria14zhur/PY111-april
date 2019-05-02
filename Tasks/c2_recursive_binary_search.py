def sub_bin_s(arr, elem, left_b, right_b):
	middle_ind = (left_b + right_b) // 2
	if arr[middle_ind] == elem:
		return middle_ind
	elif (right_b - left_b) == 1:
		return None
	else:
		if arr[middle_ind] > elem:
			middle = sub_bin_s(arr, elem, 0, middle_ind+1)
		elif arr[middle_ind] < elem:
			middle = sub_bin_s(arr, elem, middle_ind, len(arr))
		return middle


def binary_search(elem, arr):
	"""
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
	return sub_bin_s(arr, elem, 0, len(arr))


print(binary_search(5, [1, 2, 3, 5]))
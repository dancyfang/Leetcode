def partition(a,first,last):
	"""
	let pivot = a[first]
	put values smaller than pivot on the left. larger on the right

	parameters:
	a: LIst
	first: start index
	last: end index
	pivot = a[first]

	return:
	index to put pivot
	"""
	print("begin sorting: ", a[first:(last+1)])
	pv = a[first]

	i = first + 1
	j = last

	# print(first)
	done = False
	while not done:
		while a[i] <= pv and i <= j:
			i+=1
		print("i: ",i)
		while a[j] >= pv and j >= i:
			j-=1
		print("j: ",j)
		if j < i:
			done = True
		else:
			temp = a[i]
			a[i] = a[j]
			a[j] = temp
			print(a[first:(last+1)])
	# put pivot inplace
	temp = a[first]
	a[first] = a[j]
	a[j] = temp
	print(a[first:(last+1)])
	return j

def quickSort(arr,i,j):
	"""
	parameters:
	arr: List

	return:

	"""
	if i < j:
		idx = partition(arr,i,j)
		quickSort(arr,i,idx-1)
		quickSort(arr,idx+1,j)
		print("current array is: ",arr)

a = [5,1,8,2,7,4,0,0,10,9,3]
# a = [10,9,8]
quickSort(a,0,len(a)-1)
print(a)



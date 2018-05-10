def number_generator(x,n):

	list1=[]
	j=x
	for i in range(n):
		list1.append(x)
		x += j
	return list1
	#return [i*x+x for i in range(n)

print(number_generator(3,5))

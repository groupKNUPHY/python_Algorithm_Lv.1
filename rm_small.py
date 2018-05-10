def rm_small(mylist):
	return [i for i in mylist if i > min(mylist)]

my_list = [4,3,2,1]
print("result : {}".format(rm_small(my_list)))

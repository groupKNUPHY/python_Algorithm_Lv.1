def sum_digit(number):
	return sum([int(i) for i in str(number)])

print("result : {}".format(sum_digit(123)))

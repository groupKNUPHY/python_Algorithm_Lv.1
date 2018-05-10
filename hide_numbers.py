def hide_numbers(s):
	c = list(s)
	for i in range(len(c)-4):
		c[i]='*'
		j="".join(c)
	return j
	#return "*"*(len(s)-4) + s[-4:]
print("결과 : " + hide_numbers('01033334444'));

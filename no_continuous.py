def no_continuous(s):

	if len(s)>0:
		return [s[0]]+[s[i+1] for i in range(len(s)-1) if s[i]!=s[i+1]]
	else:
		return[]

a = input()
print(no_continuous(a)) 

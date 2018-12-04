############################################################
# Code for reading a textfile and calculating mean values  #
#	Useful when calcualte the mean cross-section  		   #	
############################################################


# --data file
f1name='xsec.dat'

# --read file
f = open(f1name,'r')
lines = f.readlines()
f.close()

result=0

# --mean the values in each line
for i in lines:
   result+=float(i)
print f1name
print result/len(lines)


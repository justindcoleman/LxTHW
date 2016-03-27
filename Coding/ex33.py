numbers = []
def afunc(f1, f2, rip):
	print "f1 is %d and f2 is %d and increment is %d" % (f1, f2, rip)
	
	while f1 < f2:
		print "At the top f1 is %d" % f1
		numbers.append(f1)
		
		f1 = f1+rip
		print "Numbers now: ", numbers
		print "At the bottom f1 is %d" % f1

afunc(int(raw_input("1: ")), int(raw_input("2: ")), int(raw_input("3: ")))
#rip(int(raw_input("3: ")))
print afunc
print "The numbers: "

for num in numbers:
	print num
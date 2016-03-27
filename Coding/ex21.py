def add(a, b):
	#print "ADDING %d + %d" % (a, b)
	return a + b
#define function called 'subtract' with variables 'a' & 'b'
# "gives" the function's variables to the program
def subtract(a, b):
	#print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	#print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	#print "DIVIDING %d / %d" % (a, b)
	return a /b


#print "Let's do some math with just functions!"

#age = add(30, 5)
#height = subtract(78, 4)
#weight = multiply(90, 2)
#iq = divide(100, 2)

#print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A Puzzle for extra credit, type it in anyway
#print "Here is a puzzle."

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#print "That becomes: ", what, "Can you do it by hand?"

#print "Some more stuffs"
a1 = add(1, 2)
a2 = subtract(3, 5)
a3 = multiply(8, 13)
a4 = divide(21, 34)

big = add(a1, subtract(a2, multiply(a3, divide(a4,21)))) 
print "\nAddition: %r\nSubtraction: %r\nMultiplication: %r\nDivision: %r\n\n%r" % (a1, a2, a3, a4, big) 

#print "\n\n%d", big
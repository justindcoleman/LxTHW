print "Answer all questions with true or false."
correct = 0
# Question 1
one = raw_input('True and True: ').title()
if one == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 2
two = raw_input('False and True: ').title()
if two == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 3
three = raw_input('1 == 1 and 2 == 1: ').title()
if three == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 4
four = raw_input('\"test\" == \"test\": ').title()
if four == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 5
five = raw_input('1 == 1 or 2 != 1: ').title()
if five == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 6
six = raw_input('True and 1 == 1: ').title()
if six == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 7
seven = raw_input('False and 0 != 0: ').title()
if seven == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 8
eight = raw_input('True or 1 == 1: ').title()
if eight == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 9
nine = raw_input('\"test\" != \"testing\": ').title()
if nine == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 10
ten = raw_input('1 != 0 and 2 == 1: ').title()
if ten == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 11
eleven = raw_input('\"test\" != \"testing\": ').title()
if eleven == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 12
twelve = raw_input('\"test\" == 1: ').title()
if twelve == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 13
thirteen = raw_input('not (True and False): ').title()
if thirteen == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 14
fourteen = raw_input('not (1 == 1 and 0 != 1): ').title()
if fourteen == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 15
fifteen = raw_input('not (10 == 1 or 1000 == 1000): ').title()
if fifteen == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 16
sixteen = raw_input('1 != 10 or 3 == 4: ').title()
if sixteen == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 17
seventeen = raw_input('not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\"): ').title()
if seventeen == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 18
eighteen = raw_input('1 == 1 and not (\"testing\" == 1 or 1 == 0): ').title()
if eighteen == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 19
nineteen = raw_input('\"chunk\" == \"bacon\" and not (3 == 4 or 3 == 3): ').title()
if nineteen == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'

# Question 20
twenty = raw_input('3 == 3 and not (\"testing\" == \"testing\" or \"Python\" == \"Fun\"): ').title()
if twenty == 'False':
	correct += 1
	print 'False!' 
else:
	print 'Wrong!'

# Tally
print "You got %d questions correct!" % (correct)
if correct >= 20:
	print "You're pretty good."
elif correct < 20: #and > 15:
	print "Not bad, but keep studying."
elif correct < 15: #and > 10
	print "This is not good, are you even studying?"
elif correct < 10: #and > 1
	print "Are you mistyping?  Please only use \'true\' and \'false\' for answers."
else:
	"You are either super dumb or mistyping.  Please only use \'true\' and \'false\' for answers."

# print one
# print two
# print three
# print four
# print five
# print six
# print seven
# print eight
# print nine
# print ten
# print eleven
# print twelve
# print thirteen
# print fourteen
# print fifteen
# print sixteen
# print seventeen
# print eighteen
# print nineteen
# print twenty
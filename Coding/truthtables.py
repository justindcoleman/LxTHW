print "Answer all questions with true or false."
correct = 0
#
q1 = raw_input('not False: ').title()
if q1 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q1 = False

#
q2 = raw_input('not True: ').title()
if q2 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q2 = False
#
q3 = raw_input('True or False: ').title()
if q3 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q3 = False	
#
q4 = raw_input('True or True: ').title()
if q4 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q4 = False	
#
q5 = raw_input('False or True: ').title()
if q5 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q5 = False	
#
q6 = raw_input('False or False: ').title()
if q6 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q6 = False	
#
q7 = raw_input('True and False: ').title()
if q7 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q7 = False	
#
q8 = raw_input('True and True: ').title()
if q8 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q8 = False	
#
q9 = raw_input('False and True: ').title()
if q9 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q9 = False	
#
q10 = raw_input('False and False: ').title()
if q10 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q10 = False	
#
q11 = raw_input('not (True or False): ').title()
if q11 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q11 = False	
#
q12 = raw_input('not (True or True): ').title()
if q12 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q12 = False
#
q13 = raw_input('not (False or True): ').title()
if q13 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q13 = False	
#
q14 = raw_input('not (False or False): ').title()
if q14 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q14 = False	
#
q15 = raw_input('not (True and False): ').title()
if q15 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q15 = False
#
q16 = raw_input('not (True and True): ').title()
if q16 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q16 = False
#
q17 = raw_input('not (False and True): ').title()
if q17 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q17 = False
#
q18 = raw_input('not (False and False): ').title()
if q18 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q18 = False
#
q19 = raw_input('1 != 0: ').title()
if q19 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q19 = False
#
q20 = raw_input('1 != 1: ').title()
if q20 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q20 = False
#
q21 = raw_input('0 != 1: ').title()
if q21 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q21 = False
#
q22 = raw_input('0 != 0: ').title()
if q22 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q22 = False
#
q23 = raw_input('1 == 0: ').title()
if q23 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q23 = False
#
q24 = raw_input('1 == 1: ').title()
if q24 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q24 = False
#
q25 = raw_input('0 == 1: ').title()
if q25 == 'False':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q25 = False
#
q26 = raw_input('0 == 0: ').title()
if q26 == 'True':
	correct += 1
	print 'Correct!' 
else:
	print 'Wrong!'
	q26 = False
print correct

print "You missed these questions, idiot: \n"
if q1 == False:
	print "1"
if q2 == False:
	print "2"
if q3 == False:
	print "3"
if q4 == False:
	print "4"
if q5 == False:
	print "5"
if q6 == False:
	print "6"
if q7 == False:
	print "7"
if q8 == False:
	print "8"
if q9 == False:
	print "9"
if q10 == False:
	print "10"
if q11 == False:
	print "11"
if q12 == False:
	print "12"
if q13 == False:
	print "13"
if q14 == False:
	print "14"
if q15 == False:
	print "15"
if q16 == False:
	print "16"
if q17 == False:
	print "17"
if q18 == False:
	print "18"
if q19 == False:
	print "19"
if q20 == False:
	print "20"
if q21 == False:
	print "21"
if q22 == False:
	print "22"
if q23 == False:
	print "23"
if q24 == False:
	print "24"
if q25 == False:
	print "25"
if q25 == False:
	print "26"
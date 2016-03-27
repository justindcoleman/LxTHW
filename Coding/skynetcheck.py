from random import randint
#initial variables
SNMP = 'SkyNet Mobile Platform'
first = randint(0,8)
second = randint(0,8)
third = randint(0,8)
alarm = 0

#make_em_strangz
#first= first
#second = second
#third = third

#puzzle key
print 'determined value is: %s-%d%d%d' % (SNMP, first, second, third)

#first question

a = raw_input('Abbreviated alpha designation? ')
#print "here is what you typed %r" % (a)
if a != 'SNMP':
	alarm += 1
else:
	alarm += 0 

#second question
b = int(raw_input('inital numeric value in detected serial number? '))
if b != first:
	alarm += 1
else:
	alarm += 0

#third question
c = int(raw_input('secondary numeric value in detected serial number? '))
if c != second:
	alarm += 1
else:
	alarm += 0

#fourth question
d = int(raw_input('Final numeric value in detected serial number? '))
if d != third:
	alarm += 1
else:
	alarm += 0

#tally
if alarm >= 1:
	print "Meatbag detected, sending terminators."
else:
	print "Welcome home %s-%d%d%d, prepare for processing." % (SNMP, first, second, third)
	
raw_input("Press Enter to close") 
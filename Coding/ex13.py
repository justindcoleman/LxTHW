from sys import argv

script, one, two, three = argv

#print "The script is called: ", script
#print "Your first variable is: ", first
#print "Your second variable is: ", second
#print "Your third variable is: ", third

print "What's your name?"
name = raw_input()
print "Name a person..."
first = raw_input()
print "Name a different person..."
second = raw_input()
print "Name a third person..."
third = raw_input()
print "%s named %s, %s, and %s" % (name, first, second, third)


print "%s wants to %s %s," % (name, one, first),
print "%s %s," % (two, second),
print "and %s %s!" % (three, third)
print "GROSS"
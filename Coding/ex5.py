name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 # ~188 CM
weight = 180 * .453 # ~81 KG
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s.." % name
print "He's %d centimeters tall." % height
print "He's %d kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

#trying to get down to one target.write start
newline = "\n"
adjusted = line1 + newline + line2 + newline + line3 + newline
#end
target.write(adjusted)

#for reading the file

print "And finally, we close it."
target.close()

print "Type your filename:"
file = raw_input("> ")

txt = open(file)

print txt.read()
txt.close()
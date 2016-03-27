from sys import argv

script, input_file = argv
#define a function called 'print_all' with the variable 'f'
# prints the output of f (reads to EOF)
def print_all(f):
	print f.read()
#defines a function called 'rewind' with the variable 'f'
# sets the 'read' to the beginning of a file, like rewinding a tape
def rewind(f):
	f.seek(0)
#'print_a_line' function, w/ variables 'line_count' & 'f'
# prints the output of 'line_count' & 'f', reads the line that f is set to (see above)
def print_a_line(line_count, f):
	print line_count, f.readline()
# creates variable 'current_file' which is assigned to open the file specified by argv
current_file = open(input_file)
#prints the output of the print_all function on current_file variable
print "First let's print the whole file:\n"
print_all(current_file)
# 'seeks' to the beginning of the file called by variable 'current_file'
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
#sets the variable 'current_line' to 1
# runs function 'print_a_line' on the named variables
current_line = 1
print_a_line(current_line, current_file)
#adds +1 variable 'current_line'
# runs function 'print_a_line' on the named variables
current_line += 1
print_a_line(current_line, current_file)
#same as 32-33
current_line += 1
print_a_line(current_line, current_file)
#same as 32-33
#current_line += 1
#print_a_line(current_line, current_file)
#print current_line
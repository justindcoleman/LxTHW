#from_file = raw_input()
#open(from_file)

#to_file = raw_input()
#open(to_file, 'w')

#from_file.close()
#to_file.close()

from_file = raw_input()
to_file = raw_input()

in_file = open(from_file)
indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()
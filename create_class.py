#!/usr/bin/python

import sys
import os

if len(sys.argv) < 2:
	raise Exception('Not enough parameters')

class_name = sys.argv[1]
attributes_list = sys.argv[2:]

# TODO list:
# -  Be aware of constructor parameters;
# -  Receive the constructor with all the typed 'specified', parse it and 
#    create subsref.m and subsasgn.m files with type checks

# create directory
dir_name = '@' + class_name
if not os.path.exists(dir_name):
	os.makedirs(dir_name)

# constructor
begin = "\
function object = {0}()\n"

attr_clause = "\
object.{} = [];\n"

end = "\
object = class(object, '{}');\n\
end"

with open(dir_name + '/' + class_name + '.m', 'w') as out:
	out.write(begin.format(class_name))
	for attr in attributes_list:
		out.write(attr_clause.format(attr))
	out.write(end.format(class_name))
	
# subsref
begin = "\
function ret = subsref(obj, sub)\n\
if isempty(sub)\n\
	error('@{0}/subsref: missing index');\n\
end\n\n\
switch sub.type\n\
case '.'\n\
	attribute = sub.subs;\n\
	switch attribute\n"

case_clause = "\
	case '{0}'\n\
		ret = obj.{0};\n"

end = "\
	otherwise\n\
		error(\"@{0}/subsref: invalid property '%s'\", attribute);\n\
	end\n\
otherwise\n\
	error(\"@{0}/subsref: invalid property '%s'\", attribute);\n\
end\n\n\
end"

with open(dir_name + '/subsref.m','w') as out:
	out.write(begin.format(class_name))
	for attr in attributes_list:
		out.write(case_clause.format(attr))
	out.write(end.format(class_name))
	
# subsasgn
begin = "\
function ret = subsasgn(obj, sub, rhs)\n\
if isempty(sub)\n\
	error('@{0}/subsasgn: missing index');\n\
end\n\n\
ret = obj;\n\n\
switch sub.type\n\
case '.'\n\
	attribute = sub.subs;\n\
	switch attribute\n"

case_clause = "\
	case '{0}'\n\
		ret.{0} = rhs;\n"

end = "\
	otherwise\n\
		error(\"@{0}/subsasgn: invalid property '%s'\", attribute);\n\
	end\n\
otherwise\n\
	error(\"@{0}/subsasgn: invalid property '%s'\", attribute);\n\
end\n\n\
end"

with open(dir_name + '/subsasgn.m','w') as out:
	out.write(begin.format(class_name))
	for attr in attributes_list:
		out.write(case_clause.format(attr))
	out.write(end.format(class_name))

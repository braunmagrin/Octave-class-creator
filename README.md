Octave-class-creator
====================

Creates a Octave class and its files to achieve a nice initial behaviour.
The script creates the directory to contain the class files, in which it then
creates the class constructor and functions to allow subscripted references and
subscripted assignments.

Usage:

    create_class.py <CLASS_NAME> <ATTR_NAME> [<ATTR_NANE> ...]

Example:  
To create a class called 'car' which have the following attributes:  

*    make;  
*    color;  
*    year.  

One may execute: 
 
    ./create_class.py car make color year

Result:
The script will create a directory named @car and will create inside
of it three files:

*    `car.m` - the constructor;
*    `subsref.m` - to allow subscripted references like `c.make`;
*    `subsasgn.m` - to allow subscripted assignments like `c.make = 'make-name'`

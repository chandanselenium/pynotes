'''Constructor Concept:
☕	Constructor is a special method in python.
☕	The name of the constructor should be __init__(self)
☕	Constructor will be executed automatically at the time of object creation.
☕	The main purpose of constructor is to declare and initialize instance variables.
☕	Per object constructor will be exeucted only once.
☕	Constructor can take atleast one argument(atleast self)
☕	Constructor is optional and if we are not providing any constructor then python
    will provide default constructor.

Example:
	def __init__(self,name,rollno,marks):
	    self.name=name
	    self.rollno=rollno
	    self.marks=marks'''
########################################################################################################################
'''Difference Method and Constructor
1. Name of method can be any name	            1. Constructor name should be always __init__
2. Method will be executed if we call that	    2. Constructor will be executed automatically at
   method                                          the time of object creation.
3. Per object, method can be called any number	3. Per object, Constructor will be executed only
   of times.	                                   once
4. Inside method we can write business logic	4. Inside Constructor we have to declare and
                                                   initialize instance variables'''

########################################################################################################################

'''Types of Variables:
     Inside Python class 3 types of variables are allowed.
1.	Instance Variables (Object Level Variables)
2.	Static Variables (Class Level Variables)
3.	Local variables (Method Level Variables)

1. Instance Variables:
     If the value of a variable is varied from object to object, 
     then such type of variables are called instance variables.
     For every object a separate copy of instance variables will be created.

Where we can declare Instance variables:
1.	Inside Constructor by using self variable
2.	Inside Instance Method by using self variable
3.	Outside of the class by using object reference variable

how to access
1.  Inside class by using self variable
2.  outside class by usin referance veriable'''

########################################################################################################################

'''Static variables:
        1. If the value of a variable is not varied from object to object, such type of 
           variables we have to declare with in the class directly but outside of methods.
           Such type of variables are called Static variables.
        2. For total class only one copy of static variable will be created and shared by all objects of that class.
           We can access static variables either by class name or by object reference. 
           But recommended to use class name.
           
Various places to declare static variables:
1.	In general we can declare within the class directly but from out side of any method
2.	Inside constructor by using class name
3.	Inside instance method by using class name
4.	Inside classmethod by using either class name or cls variable
5.	Inside static method by using class name

How to access static variables:
1.	inside constructor: by using either self or classname
2.	inside instance method: by using either self or classname
3.	inside class method: by using either cls variable or classname
4.	inside static method: by using classname
5.	From outside of class: by using either object reference or classnmae

NOTE:If we change the value of static variable by using either self or object reference variable, 
     then the value of static variable won't be changed,just a new instance variable with that 
     name will be added to that particular object.'''

###################################################################################################################

'''Local variables:
      Sometimes to meet temporary requirements of programmer,we can declare variables inside a method directly,
      such type of variables are called local variable or temporary variables.
      Local variables will be created at the time of method execution and destroyed once method completes.
      Local variables of a method cannot be accessed from outside of method.
'''

###################################################################################################################
'''Types of Methods:
          Inside Python class 3 types of methods are allowed
1.	Instance Methods
2.	Class Methods
3.	Static Methods

1.	Instance Methods:
      1.Inside method implementation if we are using instance variables then such type of methods are 
        called instance methods.
      2.Inside instance method declaration,we have to pass self variable.
      
   def m1(self):
      
      By using self variable inside method we can able to access instance variables.
      Within the class we can call instance method by using self variable and from outside of the 
      class we can call by using object reference.
      
2. Class Methods:
       1.Inside method implementation if we are using only class variables (static variables), 
         then such type of methods we should declare as class method.
       2.We can declare class method explicitly by using @classmethod decorator.
         For class method we should provide cls variable at the time of declaration
       3.We can call classmethod by using classname or object reference variable.  
      


'''



           


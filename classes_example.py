class hello :
	def __init__(self):
		"""
		documentation for the method goes in here
		"""
		self.y=5
	
	def print_ham(self,arg1):
		self.name=arg1


example=hello()
example.print_ham("hello")
print(example.name)
print(example.y)
		
"""
class and an instance of a class , class iss blue prit for creating instances

"""


class Employee : 
	raise_amount = 1.04
	no_of_employees = 0 
	def __init__(self,first_name,last_name,pay) :
		self.first_name = first_name
		self.last_name = last_name
		self.email = self.first_name+"."+self.last_name+"@company.com"		
		self.pay = pay
		Employee.no_of_employees += 1
		
	def print_details(self) : 
		print("First name : {0}".format(self.first_name))
		print("Last name : {0}".format(self.last_name))
		print("Email : {0}\n".format(self.email))
		
	def print_fullname(self) :
		print(self.first_name+" "+self.last_name,end="\n")
		
	def say_hello_to(self,person) :
		print(self.first_name+" says hello to "+person)
		
	def get_raise_amount(self) :
		#id Employee.raise_amount is called then class's variable will be called if self.raise_amount is called then it will check for instance variable, if instance variable is not present then class variable will be called. 
		return int(self.pay * self.raise_amount)
		
	def set_class_raise_amount(cls,amt) : 
		Employee.raise_amount = amt
	
	
print("Total number of employees before list creation {0}".format(Employee.no_of_employees))
emp1 = Employee("bala","rajan",6000)
emp2 = Employee("hari","hara",6000)
emp3 = Employee("caren","josh",6000)
emp1.print_details()
emp2.print_details()
emp2.print_fullname()
emp1.print_fullname()
print("Total number of employees after list creation {0}".format(Employee.no_of_employees))


#class's methods can be invoked with the help of class names but the argument self has to be passed, when the class's instance calls a method it passes the instance but when it iis called using class itself python woudn't be able to figure out which instance to pass

Employee.say_hello_to(emp1,"jeff")
emp1.raise_amount  = 1.05
print(emp1.get_raise_amount())
print(emp2.get_raise_amount())
print(emp3.get_raise_amount())
print(emp1.__dict__)
print(Employee.__dict__)
print(emp2.__dict__)


"""

Regular method hass instance as the first argument.
class method has a class variable as first argument.
to use class method use r @classmethod decorator.
class method can also be called from instance method, even then the first argument will the class.
static methods doesn't pass anything as first argument

Three method is classes 
 	Instance method  : instance as first argument, doesn't need any decorator
 	Class method : Class as the first argumen , @classmethod as decorator
 	static method : Doesn't need any mandatory first parameter, uses @staticmethod as decorator
 	
 	
Default arguments 
	Dont set mutable objects as default values
	Create class developer 
	and developer inheriting from employee
	transfer employees to new manager 
	add employees under manager
	see the class definition using help()
	remove employee from managers list
	isinstance - if an object is an instance of a class- check for base calsses too if the class is inherited
	isSubbclass - tells us if a class is subclass of another 
	
	
"""

class Developer(Employee) :
	raise_amount = 1.50
	
	def __init__(self,first_name,last_name,pay,language) :
	 	super().__init__(first_name,last_name,pay)
	 	self.language = language

	def print_details(self) :
	 	super().print_details()
	 	print("Programming language")
	 	
dev1 = Developer("anil","kumble",6000,"python")

dev1.print_details()
print("the raise amount :: {0}".format(dev1.get_raise_amount()))

"""
function overriding is acheived in a different way in python, can call any super class functions from inherited class using super(). then functionname
"""

print("\n")
# print(help(Developer))


class Manager(Employee) :
	def __init__(self, first_name, last_name, pay, employees=None) :
		super().__init__(first_name,last_name,pay)
		if employees is None :
			print("inside none")
			self.employees = []
		else : 
			self.employees = employees
			
	def print_details(self) : 
		super().print_details()
		if not self.employees : 
			print("Sorry, there are no employees below "+self.first_name)
		else :
			print("The employees below "+self.first_name)
			for element in self.employees :
				print(element)
		print("\n")
			
	def add_employee(self,employee_name) :
		self.employees.append(employee_name)
		
	def transfer_employee(self,manager) :
		manager.employees.extend(self.employees)
		del self.employees[:]
		# print("after transfer the list contains {0}".format(self.employees))
		
m1 = Manager("kumaran","balan",9000,["partha"])
m2 = Manager("ram","nathan",1000,["bala","hari","thulasi"])

m1.print_details()
m2.print_details()

m2.transfer_employee(m1)

print("After transfer of employees ")
m1.print_details()
m2.print_details()

"""
operator over loading in python
speciak methods in python 
special methods starts with __ 
repr is the minimun if str is defined repr should be defingd for sure - for a class object 
NotImplemented constant in python 
Property decorators - getter setters and deleters
@property
@fullname.setter
@fullname.deleter
"""
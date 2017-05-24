import threading
import time

class SquaringAndCubingTuple :

	def __init__(self,processData) :
		self.processData = processData

	def square_data(self) :
		for data in self.processData : 
			time.sleep(0.2)
			print(data*data)

	def cube_data(self) :
		for data in self.processData :
			time.sleep(0.2)
			print(data*data*data)


sq_cb_object = SquaringAndCubingTuple((1,3,5,6,8,11))

start_time = time.time()

sq_cb_object.square_data()
sq_cb_object.cube_data()

end_time = time.time()

print("the total time taken for execution of both methods is : {0:.3f}".format(end_time-start_time))

''' Threading in python will wont be that effecient as in java, this is due to GIL - Global Interpreter Lock. This allows multiple threads to run one after the other '''



class Employee(threading.Thread) : 

	thread_counter = 1

	def __init__(self,threadName,name,dept) :
		threading.Thread.__init__(self)
		self.thread_id = Employee.thread_counter
		self.employee_name = name
		self.dept = dept
		Employee.thread_counter += 1
		self.setName(threadName)

	def run(self) : 
		self.print_details()
		
	def print_details(self) :
		time.sleep(0.2)
		with threadLock :
			for i in range(5) : 
			  	employee_counter = Employee.thread_counter
			  	Employee.thread_counter =  Employee.thread_counter + 1;
		  		print(Employee.thread_counter)
			print("The details of thread {0} are : ".format(self.thread_id))
			print("Employee Name : {0}".format(self.employee_name))
			print("Employee dept : {0}".format(self.dept))
			print("The thread name is  : {0}".format(self.getName()),end = "\n\n")

threadLock = threading.Lock()

empl_1 = Employee("emp-1", "John", "sales")
empl_2 = Employee("emp-2", "Smith", "support")

#dir of any object displays the methods and variables inside that object 
print(dir(empl_1))


'''start_time = time.time()

empl_1.print_details()
empl_2.print_details()

end_time = time.time()

print("The time taken for execution of pring details of employyes : {0}".format(end_time-start_time))'''

start_time = time.time()

empl_1.start()
empl_2.start()

print("Start of thread special methods")
print(threading.active_count())
print(threading.activeCount())

#Enumerate displays the list of all threads present in the system
print(threading.enumerate())

print(threading.currentThread())
print("End of thread special methods")

empl_1.join()
empl_2.join()

end_time = time.time()

print("The time taken for execution through threads : {0}".format(end_time-start_time))
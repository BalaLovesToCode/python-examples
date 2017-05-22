from collections import deque
element="hello"
print(element[0])
print(element[-1])
print(element[4])
print(element[-5])
# [2:4] the element at 4 is excluded
print(element[2:4])
print(element[2:9])
print(element[77:99])

#List Implementation 
print("\n\nLIST IMPLEMENTATION")
sampleList=[0,1,2,3,4,5,6,7]
print("This is the sample list {0}".format(sampleList))
#Slicing returns new list
childList=sampleList[2:4]
print("this is the child List {0}".format(childList))
childList[0]=10
print("the New parent list is {0}".format(sampleList))
print("Modified child list {0}".format(childList))
sampleList[4:]=[]
print("emptying 4,5,6,7 {0}".format(sampleList))
#slicing can also be used to append the list
sampleList[4:]=[4,5,6,7,8,9,10,11,12,13,14]
lenghtOfsample=len(sampleList)
sampleList[lenghtOfsample:]=[15,16,17,18,19,20]
print("assinging 4,5, {0}".format(sampleList))
sampleList.append([1,2,3,4])
sampleList.extend([0,8,6,[3,4,5,6,7]])
print("List after useing append and extend :: {0}".format(sampleList))



#Multiple assinggments
print("\n\nMultiple Assignments implementation")
a, b=0,1
print("Values of a and b are ::{0}, {1}".format(a,b))
#Evaluation on right hand side is done before any assingments and the evaluation is from left to right
a,b=b,a+b
print("Values of a and b after further computations :: {0},{1}".format(a,b))


#For Loop
#This loop can be used to iterate over lists
print("\n\n For loop Implementation")
words=["apple","orange","beautiful"]
# dummy list is created using slicing to stop infinite looping
for item in words[:] :
	if len(item)>6 :
		print(item)
		words.insert(0,"extraElementInList")
		break
#Else clause of loop runs only when loop exits, it also doesn't get called when break statement is used inside for.
else :
	#pass statement does nothing it can be used to define a dummy function where u syntactically need an statement but don't want any code to execute
	pass
	print("The loop condition over")
print("The loop is over and the list is {0}".format(words))



#MORE ON FUNCTIONS 
#DEFAULT ARGUMENT VALUES 
#The default argument values are initialized only once
def dummyFunction(arg1="hello",arg2=None) :
	if arg2==None :
		arg2=[]
	arg2.append(arg1)
	print(arg2)
	
dummyFunction("hi")
dummyFunction("hello")
dummyFunction("how are you")
dummyFunction("kiss",["i","hate","you"])
dummyString="dfklkfd"



#LISTS IN PYTHON
#LISTS AS QUEUES
dummy_queue=deque(["harry","tom","keil"])
dummy_queue.append("bala")
print(dummy_queue)
print(dummy_queue.popleft())
print(dummy_queue)
dummy_queue=list(dummy_queue)
print(dummy_queue)
dummy_queue="hello hai brother"
print(dummy_queue)



#TUPLES
tuple_element=("naveen","mohana","hari","muthu")
#unpacking of tuple done 
nave, moh, har, muth =tuple_element
print(nave , moh , har, muth)
#item assignments is not possible for tuples
#Tuples are immutable

#sets 
set_element=set()
set_element.add("hello")
set_element.add("hanuman")
print(set_element)
set_element.add('mano')
print(set_element)


#str() and repr()
str_dummy="hlllo dude \n"
print(str(str_dummy))
print(repr(str_dummy))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + str(x) + ', and y is ' + str(y) + '...'
rr = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
print(rr)
var1="hello {} i amd the {dude}".format('red','lese',dude="hari")
print(var1)
jack_detail="hello {0:10} am the {1:10d} ".format("01234569604jdkd",32434950934504534534)
print(jack_detail)


#File Reading 
print("\n\nFile Operations")
file_sample=open('quickWorkouts.py')
# print(file_sample.read())
line_from_file=file_sample.readline()
while line_from_file!="\n" :
	print(repr(line_from_file))
	line_from_file=file_sample.readline()
print("\nThis is after while loop\n")
for line in file_sample :
	print(line,end='')
print()
file_sample.close()
with open("quickWorkouts.py","r") as f :
	read_sample=f.read()
	print(read_sample.index("print"))
print (f.closed)
with open("quickWorkouts.py","a") as f : 
	print("inside loop")
	f.write("print(\"How is every-thing going ? \")")	
with open("quickWorkouts.py","r") as f :
	print("\n\n ",f.read())
print(f)


#Exception handling 
	# IT is similar to other languages, there can be multiple except classess when there are both base class and derived classes in the except the class which is matched first will called irrespective of the original exception class.
	# There is an else segment in the exception handling which gets called when no exception is raised.
	# raise exception is similar to throw exception
	
try :
	raise Exception("arg1","arg2")
except Exception as inst :
	print(inst.args)
	x,y=inst.args
	print(x,y)
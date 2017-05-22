import sys
import modules.py
print(sys.argv);
#commandLineArgs=sys.argv 
# for i in sys.argv
	# print(i)
# for item in sys.argv	
	# print(i)
print(type(sys.argv));
argList=sys.argv
print(argList)
argList.insert(1,'kjdsjd')
print(argList)
print(sys.argv)
for i in argList:
	print(i)
else:
	print("the list conten is over")
	
	
	
'''import copy

class Foo(object):
    def __init__(self, val):
         self.val = val

    def __repr__(self):
        return str(self.val)

foo = Foo(1)

a = ['foo', foo]
b = a[:]
c = list(a)
d = copy.copy(a)
# deep copy copies the every content in the object how it it was prior to copying
e = copy.deepcopy(a)

# edit orignal list and instance 
a.append('baz')
foo.val = 5

print(' original: %r\n slice: %r\n list(): %r\n copy: %r\n deepcopy: %r'
      % (a, b, c, d, e))'''

elem=10
har=elem
har=15
print("elem {0} \n har {1}".format(elem,har))      

list1=['jers',har,elem]
har=20
print(list1)
      
welcomeMsg=modules.helloMember("Rickey pointing")
print(welcomeMsg)

from modules import helloMember
import modules
# Recursive function to print the total combinations
def printCombinations(combArr,totalSum) :
	sumDummy=0
	global combGlobal
	# if combGlobal>30 : 
	# 	return 
	b=7
	for i in combArr : 
		sumDummy=sumDummy+i
	if sumDummy==totalSum :
		combGlobal=combGlobal+1
		for i in combArr : 
			print(i,end=' ')
		print("\n")
		return
	else :
		newCombList=list(combArr)
		if(combArr[len(combArr)-1]<9) :
			combArr[len(combArr)-1]=combArr[len(combArr)-1]+1
			printCombinations(combArr,totalSum)
		newCombList.extend([1])
		printCombinations(newCombList,totalSum)
		return	
		
print("Welcome to Combinations\n")
userData=input("Enter the number for which combinations has to printed :: \n")
print("Just for confirmation, you have entered {0}".format(userData))
combGlobal=0
theCombArr=[1]
printCombinations(theCombArr,int(userData))
helloMember("harish")
print("There are {0} number of combinations".format(combGlobal))		
print(__name__)
print(dir())
print(dir(modules))
	

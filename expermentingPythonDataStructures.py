zooTuple=('zebra','lion','tiger')
animalsTuple=zooTuple
# animalsTuple[2]='elephant'
print(zooTuple)
print(animalsTuple)

# Bytes
elementList=[1,2,3,4]
print(type(elementList))
byteElements=bytes(elementList)
print(type(byteElements))
# byteElements[0]=6
print(byteElements)

# List functions
alphabetList=['apple','ball','cat','dog']
# append adds the entore element in list
alphabetList.append(('elaphant','fire','god','hat')) 
alphabetList.extend((['ink','hellle'],'jack','kill',['lemon','hkjfldf',2]))
print(alphabetList)
lastVariable=alphabetList.pop()
print("thee popped out element is {0}".format(lastVariable))
print("the modified list is :: {0}".format(alphabetList))
ithElement=alphabetList.pop(1)
print("the i'th element is "+ithElement)
print("the list after ith element is removed :: {0}".format(alphabetList))





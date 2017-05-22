with open("listOfFiles.txt","r") as file_1 :
	for line in file_1 :
		for word in line.split() : 
			print ("git add {0}".format(word))
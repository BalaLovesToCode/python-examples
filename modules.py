def helloMember(userName) : 
	helloString='Welcome {0} !'.format(userName)
	print(helloString)
	print(__name__)
	print(dir())
	return helloString

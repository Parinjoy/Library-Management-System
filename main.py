import book
c='y'
while c.lower()=='y':
	print('1. Add User')
	print('2. Login')
	print('3. Exit')
	ch=int(input('Enter your choice : '))
	if ch==1:
		book.add_user()
	if ch==2:
		if book.login():
			print("Library Management System".center(89 , '='))
			c='y'
			while c.lower()=='y':
				print('Function 1')
				print('Function 2')
				print('Function 3')
				c=input('Do you want to continue:(y/n) ')

	if ch==3:
		print('Thank You')
		break
	c=input('Do you want to continue:(y/n) ')
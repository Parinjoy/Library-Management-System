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
		try:
			cond,user=book.login()
		except:
			print('Wrong Credentials')
			cond=False
		if cond:
			print("Library Management System".center(89 , '='))
			c='y'
			while c.lower()=='y':
				if user=='admin':
					print('1. Add Books')
					print('2. Delete Books')
					print('3. View Books')
					print('0. Exit')
				else:
					print('3. View Books')
					print('4. Issue Book')
					print('5. Return Book')
					print('0. Exit')
				ch=int(input('Enter your choice : '))
				if ch==1:
					book.add_books()
				elif ch==2:
					book.delete_books()
				elif ch==3:
					book.viewbook()
				elif ch==4:
					book.issue_books(user)
				elif ch==5:
					book.return_book()
				elif ch==0:
					break
				else:
					print('Invalid Choice')
				c=input('Do you want to continue:(y/n) ')

	if ch==3:
		print('Thank You')
		break
	c=input('Do you want to continue:(y/n) ')
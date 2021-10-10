import pickle
def add_user():
	usr=input('Enter your username : ')
	pwd=input('Enter a password : ')
	pwd1=input('Enter password to confirm : ')
	if pwd==pwd1:
		d={'user':usr,'password':pwd}
		f=open('users.dat','ab')
		pickle.dump(d,f)
		f.close()
		print('Account created')
	else:
		print('Passwords do not match')

def login():
	usr=input('Enter your username : ')
	pwd=input('Enter your password : ')
	f=open('users.dat','rb')
	try:
		while True:
			m=pickle.load(f)
			if m['user']==usr and m['password']==pwd:
				print('Welcome')
				return True
	except:
		f.close()



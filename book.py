import pickle
import csv
from datetime import date
from datetime import timedelta

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
				return True,usr
	except:
		f.close()

def viewbook():
    print("1. view all books")
    print("2. view issued book")
    ch=int(input("Enter your choice:"))
    if ch==1:
        with open("book_details.csv","r",newline='') as fh:
            booklst=csv.reader(fh)
            for rec in booklst:
                print(rec)
    if ch==2:
        with open("issued.csv","r",newline='') as fh:
            issuelst=csv.reader(fh)
            for rec in issuelst:
                print(rec)

def delete_books():
	slno=input('Enter Serial Number of book to delete : ')
	name=input('Enter name of the book to delete : ')
	with open('issued.csv') as f:
		rdr=csv.reader(f)
		for i in rdr:
			if i[0]==slno and i[1]==name:
				print('Book not in Library')
				return
	f=open('book_details.csv')
	rdr=csv.reader(f)
	l=[]
	for i in rdr:
		if i[0]==slno and i[1]==name:
			continue
		else:
			l.append(i)
	f.close()
	f=open('book_details.csv','w',newline='')
	wtr=csv.writer(f)
	wtr.writerows(l)
	f.close()
	print('Book',slno,name,'deleted')

def issue_books(user):
	slno=input('Enter serial No. of the book to issue : ')
	name=input('Enter the name of book to issue : ')
	issued_date=date.today()
	return_date=issued_date+timedelta(days=7)
	f1=open('book_details.csv')
	f2=open('issued.csv','a',newline='')
	rdr=csv.reader(f1)
	wtr=csv.writer(f2)
	for i in rdr:
		if i[0]==slno and i[1]==name:
			wtr.writerow([i[0],i[1],user,issued_date,return_date])
	f1.close()
	f2.close()
	print('Book issued :',slno,name)

def unique_book_no():
    l1 = []
    import random
    for j in range(1000):
        a = random.randint(100, 9999)
        l1.append(a)
    s = sorted(set(l1))
    return s

def add_books():
    with open('book_details.csv', 'a',newline='') as f:
        writer = csv.writer(f)
        rec = []
        x = unique_book_no()
        sl_no = x[0]
        x.pop(0)
        book_name = input('enter the book name')
        author = input('enter the author')
        availability = 'yes'
        rec.extend([sl_no, book_name, author, availability])
        writer.writerow(rec)

def return_book():
    l = []
    with open('issued.csv', 'r+') as f1:
        reader = csv.reader(f1)
        for row in reader:
            l.append(row)
            for i in l:
                if i[4] == date.today():
                    a = i[1]
                    with open('book_details.csv', 'r+') as f2:
                        reader1 = csv.reader(f2)
                        writer1 = csv.writer(f2)
                        for row1 in reader1:
                            if row1[1] == i[1]:
                                writer1.writerow([i[0]], i[1], i[2], 'yes')
                                
                    l.remove(i)

        writer = csv.writer(f1)
        writer.writerows(l)
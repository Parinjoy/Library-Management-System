import csv
#with open('book_details.csv', 'w',newline='') as f:
#    writer = csv.writer(f)
#    writer.writerow(['Sl No.', 'Book name', 'Author', 'Availability'])
with open('issued.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Sl No.','Book name','Issued by','Date of issuing','Date of Return'])
#with open('users.dat','w') as f:
#    pass
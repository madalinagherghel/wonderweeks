import datetime
import sys
import MySQLdb
from tabulate import tabulate
kid_name=input('Please input your kid name: ')
while True:
    DOB = input('Date of Birth is:  ')
    try:
        DOB = datetime.datetime.strptime(DOB, "%d/%m/%Y")
        break
    except ValueError:
        print("Error: must be format dd/mm/yyyy ")
        userkey = input("press 1 to try again or 0 to exit:")
        if userkey == "0":
            sys.exit()
print(f'Date of birth is: {DOB}')

current_date = datetime.datetime.now()
print(f'Current day is: {current_date}')

days = abs(DOB-current_date).days

wonderweeks = [5, 8, 12, 19, 26, 37, 46, 55, 64, 75]
weeks = days//7
print("Your child age in weeks is:", weeks)
if weeks in wonderweeks:
    db = MySQLdb.connect(host="localhost",    
                         user="root",         
                         passwd="Y0uSh@llNotPass",
                         db="wonder_weeks")        
    cursor = db.cursor()
    print("Calculating you wonder week for", kid_name)
    sql = ("SELECT mental_leap,development_info FROM wonderweeks WHERE approximate_age=%s")
    aprage = (weeks,)
    cursor.execute(sql, aprage)
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['Mental Leap', 'Development Info'], tablefmt='psql'))
    db.close()
else:
    print("The resulted week is not a wonder week but just a regular one, week:", weeks)

import mysql.connector
from utilities import *
from utilities.configurations import getConnection
# arguments : host, database, user, password
# conn = mysql.connector.connect(host='localhost', database='APIDevelop',
#                               user='root', password='12061996KacperB')

conn = getConnection()
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
#row = cursor.fetchone()
#print(row) # returns tuple 
# print(row[3])
# rowAll = cursor.fetchall() # skips first row because cursor moved to second one
# print(rowAll) # returns list of tupples

rows = cursor.fetchall()
print(rows)
sum = 0
for row in rows:
    sum = sum + row[2]

print(sum)
assert sum == 220

query = 'update customerInfo set Location = %s where CourseName = %s'
data = ('Poland','Jmeter')
cursor.execute(query, data)
conn.commit()

queryDelete = 'delete from customerInfo where CourseName = %s'
data2 = ('selenium',) # to make tuple with 1 item you need to add ,
cursor.execute(queryDelete, data2)
conn.commit()

conn.close()



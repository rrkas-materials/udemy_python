#pip3 install mysql-connector-python
import mysql.connector

conn = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database',
)

cursor = conn.cursor()

word = input("Enter a word: ")
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}' ".format(word))

results = cursor.fetchall()  #list of tuple

if results:
    count = 1
    for result in results:
        print(count,result[1])
        count = count + 1
else:
    print('Nothing found!')
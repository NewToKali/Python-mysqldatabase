# pip install mysql-connector-python
import mysql.connector
mydb= mysql.connector.connect (
    host= "127.0.0.1",
    user="root",
    passwd="admin",
    database="files"
)
# print (mydb)
#Create a cursor 
my_cursor= mydb.cursor()

#create a database 'once you create a database add the "database" to mydb'
# my_cursor.execute("CREATE DATABASE files")
# my_cursor.execute("SHOW DATABASES")

# add a table to database
# my_cursor.execute("CREATE TABLE filename (name VARCHAR(255), uid INTEGER PRIMARY KEY)")
# my_cursor.execute("SHOW TABLES")

#add item to table
# testfile="ewbfile"
# testuid=355
# sql_insert=f"INSERT INTO filename (name, uid) VALUES ({testfile}, {testuid}) "
# my_cursor.execute(sql_insert)
# mydb.commit()

#add items to table
# sql_insert="INSERT INTO filename (name, uid) VALUES (%s, %s) "
# records=[("someting", 523), ("somet", 524)]
# my_cursor.executemany(sql_insert, records)
# mydb.commit()

# add select from table
my_cursor.execute("SELECT * FROM filename")
result = my_cursor.fetchall()
for row in result:
    print(row)
# for db in my_cursor:
#     print(db[0])
print("workedd") 
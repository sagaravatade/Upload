import mysql.connector as connection
mydb=connection.connect(host="localhost",port="3307",user="root",password="12345")
cursor =mydb.cursor()

#cursor.execute("insert into sagar123.ineuron values(101,'sagar avatade','sagar.avatade99@gmail.com',100,30)")
#mydb.commit()
cursor.execute("select * from sagar123.ineuron")
for i in cursor.fetchall():
    print(i)
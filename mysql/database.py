import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="919503", database="testdb"
)
my_cursor = mydb.cursor()
# my_cursor.execute("CREATE DATABASE testdb")

# my_cursor.execute("SHOW DATABASES")

# print(my_cursor)
# for db in my_cursor:
#     print(db)

# my_cursor.execute(
#     "CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(3), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)"
# )
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table)

# sql_cmd = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record1 = ("Filip", "filipjasic8@gmail.com", 28)
# my_cursor.execute(sql_cmd, record1)
# mydb.commit()


# sql_cmd = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# records = [
#     ("John", "john@john.com", 33),
#     ("Mary", "mary@mary.com", 25),
#     ("Steve", "steve@steve.com", 56),
# ]
# my_cursor.executemany(sql_cmd, records)
# mydb.commit()

# my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i%' AND age = 28")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)

# my_sql = "UPDATE users SET age = 42 WHERE user_id = 1"
# my_cursor.execute(my_sql)
# mydb.commit()
# my_cursor.execute("SELECT * FROM users")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)
my_cursor.execute("SELECT * FROM users LIMIT 2")
result = my_cursor.fetchall()
for row in result:
    print(row)

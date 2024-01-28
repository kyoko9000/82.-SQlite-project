import sqlite3

# 1 create the database name test
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# 2 create the table name COMPANY
# conn.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME            TEXT    NOT NULL,
#          AGE             INT     NOT NULL,
#          ADDRESS         CHAR(50),
#          SALARY          REAL);''')
# print("Table created successfully")
# conn.close()

# 3 insert values into table name COMPANY
value = "32"
conn.execute(f"INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', {value}, 'California', 123.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

conn.commit()
print("Records created successfully")
conn.close()

# 4 read data form table name COMPANY
# cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
# for row in cursor:
#     print("ID = ", row[0])
#     print("NAME = ", row[1])
#     print("ADDRESS = ", row[2])
#     print("SALARY = ", row[3]), "\n"
#
# print("Operation done successfully")
# conn.close()

# 5 update values of database name COMPANY
# value = "5"
# conn.execute(f"UPDATE COMPANY set SALARY = 100.00 where ID = {value}")
# conn.commit()
# print("Total number of rows updated :", conn.total_changes)

# cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
# for row in cursor:
#     print("ID = ", row[0])
#     print("NAME = ", row[1])
#     print("ADDRESS = ", row[2])
#     print("SALARY = ", row[3]), "\n"
#
# print("Operation done successfully")
# conn.close()

# 6 delete values
# conn.execute("DELETE from COMPANY where ID = 6;")
# conn.commit()
# print("Total number of rows deleted :", conn.total_changes)
#
# cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
# for row in cursor:
#     print("ID = ", row[0])
#     print("NAME = ", row[1])
#     print("ADDRESS = ", row[2])
#     print("SALARY = ", row[3]), "\n"
#
# print("Operation done successfully")
# conn.close()

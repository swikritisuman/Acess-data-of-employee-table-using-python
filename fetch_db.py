import sqlite3
conn = sqlite3.connect('employees.db')
cursor =conn.cursor()
cursor.execute('SELECT *FROM employees')
rows=cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]},Name:{row[1]},Department:{row[2]},Salary:{row[3]}")
conn.close()
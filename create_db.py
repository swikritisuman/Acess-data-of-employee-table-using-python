import sqlite3
conn =sqlite3.connect('employees.db')
cursor =conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS employees (
               id INTEGER PRIMARY KEY,
               name TEXT,
               department TEXT,
               salary REAL
               )
            ''' )

cursor.execute('INSERT INTO employees(name,department,salary) VALUES (?,?,?)',('Swikriti Suman','Engineering',79000))
cursor.execute('INSERT INTO employees(name,department,salary) VALUES (?,?,?)',('Shreya Kumari','Marketing',65000))
cursor.execute('INSERT INTO employees(name,department,salary) VALUES (?,?,?)',('sweta Tiwari','Sales',56000))
cursor.execute('INSERT INTO employees(name,department,salary) VALUES (?,?,?)',('Nayan Raj','Stock',79000))
cursor.execute('INSERT INTO employees(name,department,salary) VALUES (?,?,?)',('Sangeeta Raj','Pharmacy',98000))
conn.commit()
conn.close()
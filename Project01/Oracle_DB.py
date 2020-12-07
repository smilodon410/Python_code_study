
import cx_Oracle as ora

connection = ora.connect('hhj', '1234', 'localhost:1521/orcl')

cur = connection.cursor()

cur.execute("""
    SELECT * FROM P01""")

for name, age, salary in cur:
    print(name, age, salary)


import mysql.connector
import math
from DBEDAssign2 import DBEDAssign2

student_id = 'a1904209'
d1 = DBEDAssign2(student_id)
print("Setting up")
d1.setUp()

print("Reading data")
d1.readData('aust_trim_code.csv')
print("Data read complete")

d1.show_all()
for i in d1.select_by_pcode("0200"):
    print(i)

locstor = d1.entropyCalc()
print('{:2.3f}'.format(locstor))

d1.tearDown()

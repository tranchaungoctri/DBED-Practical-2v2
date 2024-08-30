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

locstor = d1.entropyCalc()
print(locstor)

d1.tearDown()

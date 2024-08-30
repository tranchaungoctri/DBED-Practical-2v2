import mysql.connector
import math
from DBEDAssign2 import DBEDAssign2

student_id = 'a1904209'

d1 = DBEDAssign2(student_id)

def check_row_count(fname):
    with open(fname, 'r') as file:
        rows = file.readlines()
        return len(rows) - 1
total_rows = check_row_count('aust_trim_code.csv')
print(total_rows)

print("Setting up")
d1.setUp()

print("Reading data")

d1.readData('aust_trim_code.csv')
print("Data read complete")

locstor = d1.entropyCalc()
print(locstor)

d1.tearDown()

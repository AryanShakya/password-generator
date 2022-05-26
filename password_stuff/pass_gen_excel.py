#! python3
import openpyxl# library to work with excel
from openpyxl import workbook
import secrets
import strings

workbook = Workbook()
workbook.save(filename="credentials.xlsx")
wb = openpyxl.Workbook() 

def generator():
    length = int(input('Enter the length of password: '))                      

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols


    password = ''.join(secrets.choice(all) for i in range(length))

    purpose = (input("Intention:"))

    
    pseudonym= (input("Pseudonym used:"))

sheet = wb.active

data = (
    (password, purpose, pseudonym)
)


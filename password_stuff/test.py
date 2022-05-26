#! python3
import openpyxl# library to work with excel
from openpyxl import Workbook

password = 8672
pseudonym = "none"
purpose = "test"

workbook = Workbook()
workbook.save(filename="credentials.xlsx")

print("opening worksheet")

wb = openpyxl.load_workbook("credentials.xlsx")
Workbook.write( data =(
    (password, purpose, pseudonym)
))

workbook.save(filename="credentials.xlsx")

print("done")

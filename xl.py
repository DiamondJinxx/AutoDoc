#!/usr/bin/python3

import openpyxl as opx
from openpyxl.styles.borders import Border, Side


workbook_path = "/home/jinxx/myWork/AutoDoc/test.xlsx"
workbook = opx.load_workbook(workbook_path)

bold_border = Border(left=Side(style='thin'),
                     right = Side(style='hair'),
                     top=Side(style='medium'),
                     bottom=Side(style='thick'))

ws = workbook.worksheets[0]
ws.cell(row=3,column=2).border = bold_border
workbook.save(workbook_path)

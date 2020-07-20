#!/usr/bin/python3

import openpyxl as opx
from openpyxl.styles.borders import Border, Side

#need font-style type A

workbook_path = "/home/jinxx/myWork/AutoDoc/test.xlsx"
workbook = opx.load_workbook(workbook_path)

bold_border = Border(left=Side(style='thin'),
                     right = Side(style='hair'),
                     top=Side(style='medium'),
                     bottom=Side(style='thick'))

ws = workbook.worksheets[0]
ws.cell(row=2,column=2).border = bold_border
ws.merge_cells('A2:D2')





#close file with save
workbook.save(workbook_path)

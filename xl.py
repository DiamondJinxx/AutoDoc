#!/usr/bin/python3

import openpyxl as opx
from openpyxl.styles.borders import Border, Side

#need font-style type A

workbook_path = "test.xlsx"
workbook = opx.load_workbook(workbook_path)
worksheet = workbook.active

#border style
border_style = Side(border_style="medium") #bold border lines
bold_border = Border(left=border_style,
                     right=border_style,
                     top=border_style,
                     bottom=border_style)

worksheet = workbook.worksheets[0]
worksheet.cell(row=2, column=2).border = bold_border
worksheet.merge_cells('A2:D2')
worksheet.merge_cells('C2:C8')
worksheet.merge_cells('B2:B8')

#need set this field for top and bot cell, don't know why not work with top cell like in write in documentations
top_left_cell = worksheet['B2']
bot_left_cell = worksheet['B8']
top_left_cell.border = bold_border
bot_left_cell.border = bold_border

#set width
worksheet.column_dimensions['A'].width = 2.016 # 2.016 in this lib is 1 cm
worksheet.column_dimensions['b'].width = 2.822

#close file with save
workbook.save(workbook_path)

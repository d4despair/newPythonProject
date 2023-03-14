# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/10 16:02
import math

import openpyxl
from openpyxl import Workbook
path = 'value_var.xlsx'
wb = openpyxl.load_workbook(path)
ws = wb.worksheets[0]
firstRowFlag = 1
offset = 0
previousType = ''
dOffsets = {'Bool': 0.1, 'Int': 2, 'Real': 4}
lTypes = ['Bool', 'Int', 'Real']
for r in ws.rows:
    if r[0].value == '偏移量':
        continue
    tagType = r[2].value
    if firstRowFlag == 1:
        firstRowFlag = 0
    else:
        # 布尔型特殊处理
        if previousType == 'Bool':
            if tagType == 'Bool':
                if offset * 10 % 10 > 7:
                    offset = math.floor(offset) + 1
            else:
                offset = math.floor(offset)
                if offset % 2 == 1:
                    offset += 1
                else:
                    offset += 2
    r[0].value = offset
    offset += dOffsets[tagType]
    previousType = tagType
wb.save("text.xlsx")

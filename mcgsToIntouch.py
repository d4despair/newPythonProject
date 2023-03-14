# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/13 10:00
import csv

from openpyxl import Workbook

file_path = 'Siemens_1200.csv'

csvData = []
with open(file_path, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num > 5:
            csvData.append(row)

intouchData = []

# 读写定义
tagReadTypes = {'只读': 'RO', '读写': 'R/W'}
# 类型定义
siemensDataTypes = {'Bool': 'Bool', 'Int': 'Int', 'Real': 'Real'}
intouchDataTypes = {'Bool': 'Boolean', 'Int': 'Short', 'Real': 'Float'}
intouchAddrTypes = {'Bool': 'X', 'Int': 'INT', 'Real': 'REAL'}
tagDataTypes = {'siemens': siemensDataTypes, 'intouch': intouchDataTypes}

for row in csvData:
    # 变量名
    tagName = row[1]
    # 变量类型
    targetName = 'intouch'
    if row[2] == 'INTEGER':
        rawTagType = 'Bool'
    elif row[6] == '16位 无符号二进制':
        rawTagType = 'Int'
    else:
        rawTagType = 'Real'
    tagType = tagDataTypes[targetName][rawTagType]
    # 读写类型
    tagRW = tagReadTypes[row[4]]
    # 变量地址
    tagDB = row[3].lstrip(row[4])[0:row[3].find(':')-2]

    rawTagOffset = row[3][row[3].find(':')+1:len(row[3])]
    match rawTagType:
        case 'Bool':
            tagOffset = float(rawTagOffset)
        case 'Int':
            tagOffset = int(rawTagOffset[3:len(rawTagOffset)])
        case 'Real':
            tagOffset = int(rawTagOffset[2:len(rawTagOffset)])

    tagAddr = tagDB + ',' + intouchAddrTypes[rawTagType] + str(tagOffset)
    tag = [tagName, tagType, tagRW, tagAddr]
    intouchData.append(tag)

wb = Workbook()
ws = wb.active
for row in intouchData:
    ws.append(row)
wb.save('intouchData.xlsx')



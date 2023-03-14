# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/10 15:28
import csv

from openpyxl import Workbook

wb = Workbook()
ws = wb.active

header = ['名称', '时间', '注释']
data = [['test1', '2022/3/10', '测试1'],['test2', '2022/3/13', '测试2']]
ws.append(header)
for row in data:
    ws.append(row)
wb.save('new.xlsx')

with open('test.csv', 'w', newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    dataFromXl = []
    for row in ws.rows:
        rowData = []
        for c in row:
            rowData.append(c.value)
        dataFromXl.append(rowData)
    writer.writerows(dataFromXl)



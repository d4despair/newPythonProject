# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/10 11:13

import csv

# 读取csv文件最简单的例子
# with open('D:\\Siemens_1200.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         if reader.line_num > 4:
#             print(row)

pathData = 'D:\\Siemens_1200.csv'
pathHeader = 'D:\\Siemens_1500.csv'
l = []
# 读取设备类型
with open(pathHeader, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num > 4:
            break
        l.append(row)
print('read header finished')

# 读取变量列表
with open(pathData, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num > 4:
            l.append(row)
print('read data finished')

# for r in l:
#     print(r)

import datetime

filename = datetime.datetime.now().strftime('%Y%m%d%H%M')

pathOutput = 'D:\\new_' + filename + '.csv'
with open(pathOutput, 'w', newline='') as f:
    writer = csv.writer(f)
    for row in l:
        writer.writerow(row)

print('output file: ' + pathOutput)

# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/13 15:51
import csv
import datetime

import datetime as datetime
import openpyxl
# 模板地址
template_path = '模板.csv'

template_other = {}
template_maint_cd = {}
template_tag_names = []
template = {}
header = []
with open(template_path, 'r') as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    # print(reader.fieldnames)
    for r in reader:
        temp = r[':MemoryInt']
        name = temp[temp.find('\\') + 1:len(temp)]
        template_tag_names.append(name)
        template[name] = r
        if name == 'MAINT_CD':
            for i in reader.fieldnames:
                template_maint_cd[i] = r[i]
        else:
            for i in reader.fieldnames:
                template_other[i] = r[i]

# print(template)
print('r in template')

wb = openpyxl.load_workbook('202202026-4变量生成器 20230114.xlsx', read_only=1, data_only=1)
ws = wb['编号名称索引']
maintTags = {}
for r in ws:
    if ('_M' in r[0].value and 'Spare' not in r[3].value):
        maintTags[r[0].value] = r[3].value
# print(maintTags)

# newline='' 非常重要
maint_db_path = 'maint_intouch_db' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.csv'

with open(maint_db_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for tag in maintTags:
        for field in template:
            template[field][':MemoryInt'] = tag + '\\' + field
            template[field]['Comment'] = maintTags[tag] + ' ' + field
            template[field]['AlarmComment'] = maintTags[tag] + ' 维护时间到'
            template[field]['InitialValue'] = 1234
            writer.writerow(template[field])

print(maint_db_path + '生成完毕')

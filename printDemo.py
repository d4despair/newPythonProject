# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/6 14:38

# 输出数字
print(520)
print(98.5)

# 输出字符串
print('helloworld')
print("helloworld")

# 输出含有运算符的表达式
print(3+1)

# 输出到文件中, 注意点，1. 所制定的盘符存在， 2.使用file=fp
fp = open('D:/text.txt', 'a+') # 如果文件不存在就创建， 存在就在文件内容后面继续追加
print('helloworld', file=fp)
fp.close

# 不进行换行输出
print('hello', 'world', 'python')

# 测试excel
fp = open('D:/test.xlsx', 'a+')
print('helloworld', file=fp)
fp.close



# @AUTHOR: DIOCAI
# DEVELOP TIME: 22/6/18 11:12

# 贪心算法案例1 求几个小孩能吃饱
# 每个小孩各自有饥饿度，每个饼干各自有饱腹度，只有当饱腹度大于等于饥饿度时，小孩才能吃饱

# 小孩的饥饿度
children = [1, 9, 3, 5]
# 饼干的饱腹度
cookies = [10, 2, 3, 4, 6, 1]

# 喂之前先集合排序，先满足最小的需求
children.sort()
cookies.sort()

# 集合指针
child = 0
cookie = 0


while (child < len(children)) and (cookie < len(cookies)):  # 越界判断
    if children[child] <= cookies[cookie]:  # 将最小的饼干喂给最不饿的小孩
        child += 1  # 小孩饱了就换下一个
    cookie += 1 # 无论饼干是否被吃掉，都得拿下一个饼干进行尝试

print(child)

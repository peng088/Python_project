# 3-4  嘉宾名单
guest_list = ['张三', '李四', '王二']
print('I will invite:')
print(guest_list)

# 3-5 修改列表
print(guest_list[1]+'无法参加聚会')
guest_list[1] = '麻子'
print('新的邀请名单')
print(guest_list)

# 3-6 添加嘉宾
print('聚会会场变大了，可以邀请更多人')
guest_list.insert(0, '新嘉宾1')
guest_list.insert(2, '新嘉宾2')
guest_list.append('新嘉宾3')
print(guest_list)

# 3-7 缩减名单
print('餐桌不能即时到，有人不能参与聚会了')
print('很抱歉'+ guest_list.pop())
print('很抱歉'+ guest_list.pop())
print('很抱歉'+ guest_list.pop())
print('很抱歉'+ guest_list.pop())
print('请你们来聚会'+guest_list[0])
print('请你们来聚会'+guest_list[1])

del guest_list[0]
del guest_list[0]
print(guest_list)
# 3-1姓名

name_list = ['zhangsan', 'lisi', 'waner', 'mazi']
print(name_list[0])
print(name_list[1])
print(name_list[2])
print(name_list[3])

# 3-2  问候语
print(name_list[0]+', hello, 吃了吗？')
print(name_list[1]+', hello, 吃了吗？')
print(name_list[2]+'，hello, 吃了吗？')
print(name_list[3]+'，hello, 吃了吗？')

# 3-3 自己的列表
message = ' I would like to own a '
vehicle = ['moto', 'car', 'electrocar']
for i in vehicle:
    print(message+i)
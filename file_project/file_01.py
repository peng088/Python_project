# 10-1 学习笔记
# play one
filename = '/home/peng/Desktop/Python_project/file_project/learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)

# play two 
with open(filename) as file_object:
    file_read = file_object.read()
    print(file_read)

# play three

with open(filename) as t:
    line = t.readlines()
lines = []

lines += line

print(lines)

# 10-2 c语言学习笔记
filename = '/home/peng/Desktop/Python_project/file_project/learning_python.txt'
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    newline = line.replace('python', 'C')
    print(newline.rstrip())
filename = '/home/peng/Desktop/Python_project/file_project/sunm.txt'
while True:
    s = input('你喜欢编程的原因:')
    if s == 'q':
        break
    with open(filename, 'a') as f:
        f.write(s+'\n')

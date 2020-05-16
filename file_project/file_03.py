filename = '/home/peng/Desktop/Python_project/file_project/guest_book.txt'
with open(filename, 'a') as f:
    while True:
        s = input('输入名字：')
        
        if s == 'q':
            break
        else:
            print('hello '+s)
            f.write(s + '访问了！\n')

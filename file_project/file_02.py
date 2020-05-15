filename = 'file_project/guest.txt'
with open(filename, 'a') as f:
    while True:
        s = input('输入用户名：')
        if s == 'q':
            break
        f.write(s)
    f.close()

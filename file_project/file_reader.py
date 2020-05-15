filename = '/home/peng/Desktop/Python_project/file_project/pi_digits.txt'
with open(filename) as file_project:
    lines = file_project.readlines()
for line in lines:
    print(line.rstrip())
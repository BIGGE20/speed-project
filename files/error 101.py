# file = 'nofilehere.txt'
# readfile = open(file, 'r')
# print(readfile.read())
try:
    filename = 'nofilehere.txt'
    readfile = open(filename, 'r')
except IsADirectoryError:
    print(f"sorry, {filename} is a directory")
except FileExistsError:
    print(f"sorry, {filename} does not exist")
except FileNotFoundError:
    print(f"sorry {filename}was not found")
else:
    print("everything's cool.")
    readfile.close()
finally:
    print(f"thanks for stopping by")
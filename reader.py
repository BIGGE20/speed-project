import time
my_file = open('files/bio.txt','r')

# text = my_file.readline()
# print(text)
# text2 = my_file.readline()
# print(text2)
# while True:
#     line = my_file.readline()
#     if line !='':
#         print(line)
#         time.sleep(1)
#     else:
#         break

for line in my_file:
    if('gun'in line and 'gun' in line) :
        print("Bad word encountered...")
        break
    else:
        print(line)
        time.sleep(1)


my_file.close() 
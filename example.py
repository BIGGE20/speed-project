# create a file for our placeholder
placeholders = ['NOUN','VERB_ING','ADJECTIVE']

# create a function that reads files line by line
def read_files(filename):
    file = open(filename,'r')

    text = ''
    for line in file:
        text = text + process_line(line)

    file.close()
    return text

# create a function that processes each line to spot a placeholder and prompt the user
def process_line(line):
    global placeholders # mark the placeholder variable

    processed_line = ''
    words = line.split()

    for word in words:
        if word in placeholders:
            answer = input(f"Enter a {word}: ")
            processed_line = processed_line + answer +' '
        else:
            processed_line = processed_line + word + ' '

    return processed_line + '\n'



# create a function that calls the other fuction reading a particular file
def main():
    file = read_files('files/lib.txt')
    print(file)

if __name__== '__main__':
     main()

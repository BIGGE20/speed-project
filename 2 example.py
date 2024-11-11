# create a file for our placeholder
placeholders = ['NOUN','VERB_ING','ADJECTIVE']

# create a function that reads files line by line
def read_files(filename):
    try:
       file = open(filename,'r')
       text = ''
       for line in file:
               text = text + process_line(line)

       file.close()
       return text
    except IsADirectoryError:
            print(f"sorry, {filename} is a directory")
    except FileExistsError:
            print(f"sorry, {filename} does not exist")
    except FileNotFoundError:
            print(f"sorry {filename} was not found")
    
# create a function that re-writesthe file with our text
def write_file(filename,text):
     file = open(filename,'w')
     file.write(text)
     file.close()






# create a function that processes each line to spot a placeholder and prompt the user
def process_line(line):
    global placeholders # mark the placeholder variable

    processed_line = ''
    words = line.split()

    for word in words:
        stripped = word.strip(',?!;.')
        if stripped in placeholders:
            answer = input(f"Enter a {stripped}: ")
            processed_line = processed_line + answer +' '
            if word[-1] in ',?;.':
                processed_line = processed_line + word[-1] + ' '
            else:
                processed_line + ' '
        else:
            processed_line = processed_line + word+ ' '

    return processed_line + '\n'




# create a function that calls the other fuction reading a particular file
def main():
    filename = 'files/lib.txt'
    lib = read_files(filename)
    if (lib!=None):
        write_file(filename,lib)

if __name__== '__main__':
     main()
     
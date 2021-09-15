import sys

# Exercise 1. a)
# python3 paste.py names.txt numbers.txt
def paste(file1, file2):
    first_file = []
    second_file = []
    longest_string = ''
    try:
        with open(file1, 'r') as file1:
            for lineOfFile1 in file1.readlines():
                first_file.append(lineOfFile1)
                if len(lineOfFile1) > len(longest_string):
                    longest_string = lineOfFile1
            with open(file2, 'r') as file2:
                for lineOfFile2 in file2.readlines():
                    second_file.append(lineOfFile2)

        if len(first_file) == len(second_file):
            for i in range(0, len(first_file)):
                offset = len(longest_string) - len(first_file[i])
                print(first_file[i].strip() + ' ' * offset, second_file[i].strip())
        else:
            print('[!!] Number of lines in file must be equal.')

    except FileNotFoundError:
        print('[!!] File not Found')
    except:
        e = sys.exc_info()[0]
        print('[!!] Unhandeld Error ', e)


# Exercise 1. b)
# python3 paste.py -d : names.txt numbers.txt
def paste_d(seperator, file1, file2):
    first_file = []
    second_file = []
    try:
        with open(file1, 'r') as file1:
            for lineOfFile1 in file1.readlines():
                first_file.append(lineOfFile1)
            with open(file2, 'r') as file2:
                for lineOfFile2 in file2.readlines():
                    second_file.append(lineOfFile2)

        if len(first_file) == len(second_file):
            for i in range(0, len(first_file)):
                print(first_file[i].strip() + seperator + second_file[i].strip())
        else:
            print('[!!] Number of lines in file must be equal.')

    except FileNotFoundError:
        print('[!!] File not Found')
    except:
        e = sys.exc_info()[0]
        print('[!!] Unhandeld Error ', e)


# Exercise 1. c)
# python3 paste.py -s  names.txt numbers.txt
def paste_s(file1, file2):
    first_file = []
    first_line = ''

    second_file = []
    second_line = ''
    try:
        with open(file1, 'r') as file1:
            for lineOfFile1 in file1.readlines():
                first_file.append(lineOfFile1)
                if len(first_line) == 0:
                    first_line = first_line + str(lineOfFile1).strip()
                else:
                    first_line = first_line + " " + str(lineOfFile1).strip()
            with open(file2, 'r') as file2:
                for lineOfFile2 in file2.readlines():
                    second_file.append(lineOfFile2)
                    if len(second_line) == 0:
                        second_line = second_line + str(lineOfFile2).strip()
                    else:
                        if len(first_file) == len(second_file):
                            for i in range(1, len(first_file)):
                                offset = (len(first_file[i - 1]) - len(second_file[i - 1])) + 1
                                second_line = second_line + " " * offset + str(second_file[i]).strip()

        print(first_line)
        print(second_line)

    except FileNotFoundError:
        print('[!!] File not Found')
    except:
        e = sys.exc_info()[0]
        print('[!!] Unhandeld Error: ', e)


# Main
if __name__ == "__main__":
    if len(sys.argv) == 3:
        # python3 paste.py names.txt numbers.txt
        file1 = str(sys.argv[1])
        file2 = str(sys.argv[2])
        paste(file1, file2)
    elif len(sys.argv) == 5:
        # python3 paste.py -d : names.txt numbers.txt
        if (sys.argv[1] == '-d'):
            seperator = str(sys.argv[2])
            file1 = str(sys.argv[3])
            file2 = str(sys.argv[4])
            paste_d(seperator, file1, file2)
        else:
            print('[!!] Operator ' + sys.argv[1] + ' can not be used with seperator ' + sys.argv[2])
    elif len(sys.argv) == 4:
        # python3 paste.py -s names.txt numbers.txt
        if (sys.argv[1] == '-s'):
            file1 = str(sys.argv[2])
            file2 = str(sys.argv[3])
            paste_s(file1, file2)
        else:
            print('[!!] Operator ' + sys.argv[1] + ' is not supported')
    else:
        print('[!!] Must have at least 2 Arguments.')
        exit(1)

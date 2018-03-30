__author__='goldy'

def main():
 try:
    for line in readFile('file1.txt'):
        print(line.strip())
 except IOError as e:
    print('No such file exists:',e)
 except ValueError as e:
     print('Wrong file extension',e)

def readFile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('Filename must ends with .txt')

main()
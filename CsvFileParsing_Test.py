__author__='goldy'

import csv

csv_file='/home/585933/StudentMarks.csv'
fields = []
rows = []
lines= [line for line in open(csv_file)]
#print(lines[0].split())
#rint(lines[1].split())
# reading csv file
file=open(csv_file)
reader=csv.reader(file)
header=next(reader)
data=[]

for row in reader:
    #print(row)
    sem_1st = int(row[2])
    sem_2nd = int(row[3])
    sem_3rd = int(row[4])
    sem_4th = int(row[5])
    sem_5th = int(row[6])
    sem_6th = int(row[7])
    sem_7th = int(row[8])
    sem_8th = int(row[9])

    data.append([sem_1st,sem_2nd,sem_3rd,sem_4th,sem_5th,sem_6th,sem_7th,sem_8th])
print(data)
print(header)




import csv
import random

def rand_gen(k):
    k=float(k)
    k = k + random.normalvariate(0,1)
    k = k * random.randint(100,200)
    return k

def convert_pass(id):
    s=''
    #for i in range(1, len(id)):
    #    s = s + str('*')
    s = s + str('***')
    return  s

def age_convert(age):
    age=int(age)
    lower=age/10
    lower=lower*10

    upper=lower+10

    return str(lower)+'-'+str(upper)



fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'bank-data.csv'

fp=open('test.csv', 'wb')
writer = csv.writer(fp, delimiter=',')

fp2=open('dataWithAge.csv', 'wb')
writer2 = csv.writer(fp2, delimiter=',')

fp3=open('dataWithoutAge.csv', 'wb')
writer3 = csv.writer(fp3, delimiter=',')

csvFile= open(fname,'rb')
reader=csv.reader(csvFile)

header=next(reader)
writer.writerow(header)

for row in reader:
    data_bank=list()
    data_bank.append(rand_gen(row[0]))
    data_bank.append(age_convert(row[1]))
    data_bank.append(convert_pass(row[2]))
    data_bank.append(convert_pass(row[3]))
    data_bank.append(rand_gen(row[4]))
    data_bank.append(convert_pass(row[5]))
    data_bank.append(rand_gen(row[6]))
    data_bank.append(row[7])
    data_bank.append(row[8])

    writer.writerow(data_bank)
    writer2.writerow([age_convert(row[1]),row[7],row[8]])
    writer3.writerow([row[7],row[8]])

fp.close()

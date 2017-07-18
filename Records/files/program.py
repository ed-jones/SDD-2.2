import csv #import library
import random #import random library
from productrecord import ProductRecord


'''def swapData(data, index): #1st algorithm from course specification
    temp = data[index]
    if index+1 >= len(data):
        data[index] = data[0]
        data[0] = temp
    else:
        data[index] = data[index+1]
        data[index+1] = temp'''
        
def loadData(fName): #standard code for loading data.csv from csv.
    d = None #data currently set to none
    with open(fName, newline='') as csvf: #open csv file 
        reader = csv.reader(csvf, delimiter=',') #specify reader using csv. library
        d = [row for row in reader] #reads through each row and creates array
    if d: #will only execute if d exists
        print("There are {} product records read in from the file".format(len(d)))
    return d

# @arg fName - name of file relative to this 
# @arg data - list of the data we want to write
# @arg method - append or write?

def writeData(fName, data, method='a'): #access filename, list data we want to write, append method - add to list
    with open(fName, method, newline='') as csvf:#open csv file
        csw = csv.writer(csvf, delimiter=',')
        for row in data:
            csw.writerow(row)
    print ("Successfully wrote data")

def parse(data):
    return [ProductRecord(d[0],d[1],d[2],d[3]) for d in data]

#[99, "testing", 50, 1000]


#print("Is record equal to record2?: {}".format(record == record2))#string formatting {} - record2 will appear
#print("Is record equal to record3?: {}".format(record == record3))

data = loadData("data.csv")#parsed as argument during loadData
records = parse(data)

print(records[-1])
print(records[-2])
swapData(records, -2)
print("---------------------------------------")
print(records[-1])
print(records[-2])
#print(records)
#for r in records:
#    print(r)


# #record = records[-1]
# #print("Record product number: {}".format(record._prodNum))
# #print("Record desc: {}".format(record._desc))
# #print("Record quantity: {}".format(record._quantity))
# #print("Record price: {}".format(record._price))

for i in range (100):
    writeData("data.csv",[[0,"hello world",50,100]])



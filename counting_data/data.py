'''import csv
with open("counting_data\languages_data.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    count={}
    for row in reader:
        favourite=row[0]
        if favourite not in count:
            count[favourite]=0
        count[favourite]+=1
for favourite in count:
    print(favourite,count[favourite])'''
    
from collections import Counter
import csv
data=[]
with open("counting_data\languages_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row["Language"]) 
count = Counter(data)

print(count)
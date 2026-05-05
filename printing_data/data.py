'''# By using CSV library
import csv 
with open("C:/Users/Kurak/OneDrive/Documents/sql/printing_data/sample_data.csv","r") as  file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        print(row[1])'''
        
        
#By using Pandas Library
import pandas as pd
file=pd.read_csv("C:/Users/Kurak/OneDrive/Documents/sql/printing_data/sample_data.csv")
print(file)

# printing with index values
print(file.Age)

#for printing without index values
for age in file["Age"]:
    print(age)
    
    
    
    

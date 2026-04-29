'''list=['ru','pe','sh']
list.append('ri')
list.insert(1,'hi')
print(list)'''


'''my_tuple=(1,2,3,4,5)
print(type(my_tuple))
c=my_tuple[2:5]
print(c)
b=len(my_tuple)
print(b)

print(my_tuple.count(2))

list=list(my_tuple)
print(type(list))'''

'''serial_number=[1,2,3]
city=['hindupur','anantapur','hyderabad']
short_form=['hdp','atp','hyd']

data=zip(serial_number,city,short_form)
print(type(data))

data_1=list(data)
print(data_1)'''

'''dict={'hi':'rupesh','hello':'umesh'}
a=dict['hi']
print(a)
b=dict.keys()
print(b)
c=dict.values()
print(c)'''

'''x=31
if x>=30:
    print(f"{x} is greather than 30")
print(x==31)'''

'''list=[10,20,30,40,50,60]
if 10 in list:
    print(list[1])
if  enumerate(list):
    print(list)

list=[10,20,30,40,50]
list_1=[60,70,80,90]
list_3=zip(list_1,list)
print(list_3)
print(type(list_3))
dict=dict(list_3)
print(dict)
set=set(list_3) #zip is not converted into set
print(set)
tuple=tuple(list_3) #tuple is not converted into tuple
print(tuple)



for i in range (0,21,2):#starting index , stoping index {stoping index is always represent the [index-1]},increment
    print(i)

sum_squares=[]
for i in range(0,10,1):
    sum_squares=i**2
    print(sum_squares)
sum=0
for i in range(0,10,1):
    sum_of_numbers=sum+i
    print(sum_of_numbers)

for i in range(0,10,1):
    sum=sum+i
    print(sum)'''
'''squared_of_even_numbers=[]
for number in range(0,20,1):
    if number%2==0:
        squared_of_even_numbers=number**2
        print(squared_of_even_numbers)'''
'''character="i am rupesh"
for variable in character:
    print(f"the charter is :{variable}")
    #a=character["am"] it throughs an error because the str is print index only when we use the dictionary

for index,variable in enumerate(character):
    print(f"index of a character is {index} and the corresponding charcter is {variable}")

for variable in character:
    if variable not in 'rupesh':
    #if variable not in ['rupesh']: it will not used for string ,it will used for list
        print(variable)
list=['r','u','p','e','s','h']
for variable in list:
    if variable not in ['s','h']:
        print(variable)'''





'''import numpy as np
import random
import pandas as pd
a=np.array([1,2,3,4])
print(type(a))
print(a)

b=np.array([1,2,3,"10"]) # it will convert all list values into string type
print(type(b))
print(b)

#creating of 2d array
array=np.array([[1,2],[3,4]])
print(array)
print(type(array))

#creating of lists
list=[[1,2],[3,4]] #based on first type of braces it will decide the type.
print(list)
print(type(list))
tuple=([1,2],[3,4])
print(tuple)
print(type(tuple))
#method in numpy library
shape_of_array=np.array([[[1,2,3],[4,5,6]],
                         [[1,2,3],[4,5,6]],
                         [[1,2,3],[4,5,6]]]
                        )
print(shape_of_array)
print(shape_of_array.shape)
print(shape_of_array.size)
print(shape_of_array.ndim)
print(shape_of_array.dtype)
# it will prints the float values 
c=np.zeros((3,4))
print(c)
d=np.ones((4,3))
print(d)   
e=np.ones((4,6),dtype=int) # it will print only integer values 
print(e) 
e.shape=(12,2)# it will reshape the array
print(e)
f=np.arange(100)
print(f)
g=np.arange(0,100,2)
print(g)
h=np.random.normal(1,10)
print(h)
i=np.random.normal(1,10,(3,4)) # (3,4) is declared as a size of array it will represent as rows and coloums
print(i)
print()
j=np.random.normal(1,10,size=(3,5))
print(j)
print()'''

'''number_series=pd.Series([1,2,3])
print(number_series)
print()
number_series1=pd.Series([4,5,6,7],index=["a","b","c","d"],name='number')
print(number_series1)

k=number_series[0]
print(k)
l=number_series1['a']
print(l)

#creating a data frame using pandas
some_data=np.random.randint(1,5,(3,4))
print(some_data)
print()
data_set=pd.DataFrame(some_data,columns=['rupesh','rajesh','raju','umesh'])
print(data_set)
#creating a indexes
another_data_set=pd.DataFrame(some_data,columns=['rupesh','rajesh','raju','umesh'],index=["a","b","c"])
print(another_data_set)

#store the data in list_in_lists
my_list=[['rupesh',10],['rajesh',20],['raju',30]]
print(my_list)
df=pd.DataFrame(my_list,columns=['NAME','AGE'])
print(df)

#store the data in dictionary
employee={"employee_name":["rupesh","rajesh","raju","umesh"],"income":[10000,20000,30000,40000]}
df_1=pd.DataFrame(employee)
print(df_1)


series_dict={'first_series':pd.Series([10,20,30,40]),
             'second_series':pd.Series([50,60,70,80])}
df_2=pd.DataFrame(series_dict)
print(df_2)'''




'''numbers=np.random.randint(1,100,(10,5))
df_3=pd.DataFrame(numbers,columns=['a','b','c','d','e'])
print(df_3.index)
print(df_3)
print(type(df_3))
print()
print(df_3.head(5))
print()

print(df_3.tail(2))
print(df_3.columns)
print(df_3.info)
#renaming the columns temperoary
df_4=df_3.rename(columns={'a':'rup','b':'raj'})
print(df_4)
#renaming the columns permenantely
df_5=df_3.rename(columns={'a':'rup','b':'raj'},inplace=True)
print(df_5)
array=np.zeros((2,4),dtype=int)
print(array)

numbers=np.random.randint(1,100,(4,5))
print(numbers)
print()
df=pd.DataFrame(numbers,columns=["a","b","c","d","e"])
print(df)'''


filename="javastring"
suffix="ing"
if suffix in filename:
    print(f"{suffix} is valid")
else:
    print(f"{suffix} is  invalid")

filename="string"
suffix="NG"
if suffix in filename:
    print(f"{suffix} is valid")
else:
    print(f"{suffix} is invalid")
    
filename="placement"
suffix="cement"
if suffix in filename:
    print(f"{suffix} is valid")
else:
    print(f"{suffix} is invalid")

filename="sri ramachandra eng"
suffix="aeng"
if suffix in filename:
    print(f"{suffix} is vaild")
else:
    print(f"{suffix} is  invalid")

filename="java.x"
suffix=".x"
if suffix in filename:
    print(f"{suffix} is valid")
else:
    print(f"{suffix} is invalid")


filename="document.exe"
suffix=".exe"
if suffix in filename:
    print(f"{suffix} is valid")
else:
    print(f"{suffix} is invalid")
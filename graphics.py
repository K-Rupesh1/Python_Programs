'''from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color('red')
timmy.forward(200)

my_screen = Screen()
my_screen.onkeypress(timmy.left,"a")
#my_screen.exitonclick()'''

'''from prettytable import PrettyTable
table= PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Bulbasaur", "Charmander"])
table.add_column("Type", ["Electric", "Grass", "Fire"])
table.add_row(["Squirtle", "Water"])
table.align = "c"  
print(table) '''

from prettytable import PrettyTable
table=PrettyTable()


students=int(input("enter number of students : "))
subjects=int(input("enter number of subjects : "))
subject_name=["telugu","english","hindi"][:subjects]
table.field_names = ["Student Name"] + subject_name

for student in range (students):
    name:str=input(f"enter a student name {student +1} : ")
    mark=[]
    for subject in range(subjects):
        marks=int(input(f"enter a {name} marks in {subject_name[subject]} :"))
        mark.append(marks)
    table.add_row([name]+mark)  
print(table)
    
#print(names)
#print(mark)
    



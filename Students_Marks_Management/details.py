class Students:
    def __init__(self,students_name,roll_number):
        self.students_name=students_name
        self.roll_number=roll_number
        self.marks={}
        self.total_marks=0
        self.result=""
        self.grade=""
    def add_marks(self,subject,marks):
        self.marks[subject]=marks
    def get_report(self):
        return{
            "students_name":self.students_name,
            "roll_number":self.roll_number,
            "marks":self.marks,
            "total_marks":self.total_marks,
            "result":self.result,
            "grade":self.grade
            
        }


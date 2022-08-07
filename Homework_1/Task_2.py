import random

# ######Task two #######
# Write a base class to represent a student. Below is a starter code.
# Feel free to add any more new features to your class.
# As a minimum a student has a name and age and a unique ID.


class Student:

    def __init__(self, name, age, unique_id):
        self.name = name
        self.age = age
        self.unique_id = unique_id
        self.subjects = {}

    def introduction(self):
        print(f"Hi, my name is {self.name} , I am {self.age}, my student id is {self.unique_id}")


person_1 = Student("Chinelo", "21", "1234")

person_1.introduction()

# Create a new subclass from student to represent a concrete student doing a specialization, for example:
# exampleSoftware Student and Data Science student.


class Specialisation(Student):
    def __init__(self, name, age, unique_id):
        super().__init__(name, age, unique_id)
        self.subjects = random.choice(['Software', 'Data', 'Full Stack'])

    def subject_name(self):
        print(f"I am a {self.subjects} student")


person_2 = Specialisation("Elizabeth", "90", "1926")
person_2.subject_name()


class CFGStudent(Student):

    def __init__(self, name, age, unique_id):
        super().__init__(name, age, unique_id)

    def add_subject_and_score(self, subject_and_score):
        self.subjects.update(subject_and_score)

    def remove_subject(self, subject):
        self.subjects.pop(subject)

    def view_subjects(self):
        for subject, score in self.subjects.items():
            print(f"{subject}:  Grade: {score}")

    def overall_marks(self):
        sum_scores = 0
        for i in self.subjects.values():
            sum_scores = sum_scores + i

        avg = sum_scores / len(self.subjects.values())
        return avg


person_3 = CFGStudent("Michael", "30", "3441")

# INTRODUCTION
person_3.introduction()

# ADD SUBJECT
person_3.add_subject_and_score({"Maths": 85})
person_3.add_subject_and_score({"Science": 47})
person_3.add_subject_and_score({"French": 66})
person_3.add_subject_and_score({"History": 100})
person_3.add_subject_and_score({"English": 67})

# REMOVE SUBJECTS
person_3.remove_subject("Maths")

# VIEW SUBJECTS
person_3.view_subjects()

# OVERALL MARKS
print("The average score is", person_3.overall_marks())

# ---------------- Assignment 1: MedicalStudent ----------------

class MedicalStudent:
    def __init__(self, name, year, school, specialty_interest, gpa, sleep_hours):
        self.name = name
        self.year = year
        self.school = school
        self.specialty_interest = specialty_interest
        self.gpa = gpa
        self.sleep_hours = sleep_hours
        self.mood = "tired" if sleep_hours < 6 else "okay"

    def introduce(self):
        print(f"I'm {self.name}, a {self.year} medical student at {self.school}.")
        print(f"I want to specialize in {self.specialty_interest}. My GPA is {self.gpa}.")

    def study(self, subject, hours):
        print(f"{self.name} is studying {subject} for {hours} hours.")
        self.sleep_hours -= 1
        self.update_mood()

    def attend_class(self):
        print(f"{self.name} is attending lectures and clinicals.")

    def take_exam(self, subject):
        print(f"{self.name} is taking an exam in {subject}.")

    def update_mood(self):
        self.mood = "tired" if self.sleep_hours < 6 else "okay"

    def check_status(self):
        print(f"{self.name}'s mood is '{self.mood}' with {self.sleep_hours} hours of sleep.")


class ClinicalStudent(MedicalStudent):
    def __init__(self, name, year, school, specialty_interest, gpa, sleep_hours, rotation):
        super().__init__(name, year, school, specialty_interest, gpa, sleep_hours)
        self.rotation = rotation

    def attend_class(self):
        print(f"{self.name} is doing a {self.rotation} rotation and shadowing doctors.")


# ---------------- Activity 2: Food Polymorphism ----------------

class Food:
    def eat(self):
        print("Eating food...")

class Pizza(Food):
    def eat(self):
        print("Eating pizza with hands – delicious and cheesy!")

class Soup(Food):
    def eat(self):
        print("Sipping hot soup with a spoon – warm and comforting!")

class IceCream(Food):
    def eat(self):
        print("Licking ice cream from a cone – cold and sweet!")


# ---------------- Running the Program ----------------

print("---- MEDICAL STUDENT PROGRAM ----\n")

student1 = MedicalStudent("Zara", "2nd year", "University of Lagos", "Neurology", 3.8, 7)
student2 = ClinicalStudent("Ahmed", "5th year", "University of Ibadan", "Surgery", 3.5, 5, "O&G")

student1.introduce()
student1.study("Biochemistry", 3)
student1.attend_class()
student1.check_status()

print("\n---\n")

student2.introduce()
student2.study("Obstetrics", 4)
student2.attend_class()
student2.take_exam("Surgery")
student2.check_status()

print("\n---- FOOD POLYMORPHISM ----\n")

foods = [Pizza(), Soup(), IceCream()]
for food in foods:
    food.eat()

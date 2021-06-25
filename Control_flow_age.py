class Identidy:
    def __init__(self, age, license):
        self.age = age
        self.license = license

    def able_to_vote(self):
        if self.age >= 18:
            return "You can vote!"
        else:
            return "You are too young to vote"

    def able_to_drink(self):
        if self.age >= 25:
            return "You are able to drink and buy alcohol"
        if self.age >= 18 and self.age <= 25:
            return "You can drink but if you want to buy it show some ID!"
        if self.age > 15 and self.age < 18:
            return "you can't legally drink but your mates/unties might have your back!"
        else:
            return "You can't drink you are too young!"

    def to_drive(self):
        if self.license and self.age <= 16:
            return "You have a license and are old enough to drive!"
        else:
            return "You can not drive!"

    def is_student(self):
        if self.age < 16:
            return "Get back to school!"
        else:
            return "You are free!"




while True:
    age = input("How old are you? ")
    if age.isdigit() == False:
        print("Invalid inout. Please enter a number!")
        age = input("How old are you?")
    break
while True:
    answer = input("Do you have a driving license? Enter 'y' or 'n' or enter 'exit' to exit ")
    if answer.lower() == "y":
        license = True
        break
    elif answer.lower() == 'n':
        license = False
        break
    elif answer == "exit":
        break
    else:
        print("Invalid input! enter 'y' 'n' or 'exit' ")

person = Identidy(int(age), license)
print(person.able_to_drink())
print(person.to_drive())
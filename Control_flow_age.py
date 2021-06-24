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


user_prompt = True
age = int(input("How old are you? "))


you = Identidy(age, license)
print(you.able_to_vote())


class Person:
    def getGender(self):
        print("Unknown")

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

print("\n=== Question_3 ===")
m = Male()
m.getGender()
f = Female()
f.getGender()
class StringHandler:
    def __init__(self):
        self.text = ""

    def get_string(self):
        self.text = input("Enter a string: ")

    def print_string(self):
        print(self.text.upper())

obj1 = StringHandler()
obj1.get_string()
obj1.print_string()
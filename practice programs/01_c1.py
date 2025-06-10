class student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

       

    def info(self):
         print(f"Name of stuent is: {self.name} , average marks that {self.name} obtain is: {self.marks}")


s1 = student("Harsh", 499)
s1.info()
                   
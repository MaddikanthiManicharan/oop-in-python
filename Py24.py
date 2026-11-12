class parent:
    def display(self):
        print("Parent")

class child(parent):
    def display(self):
        print("Child")

c = child()
c.display()
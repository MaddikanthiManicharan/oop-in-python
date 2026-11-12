print("Yo")
class parent:
    pass
class child(parent):
    pass
class student:
    name="Kprit"
    age=20
class csestudent(student):
    branch="CSE"
fg=csestudent()
print(fg.name)
print(fg.age)
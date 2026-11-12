class father:
    def work(self):
        print("father work in IT")
class mother:
    def cook(self):
        print("mother cooks")
class child(father,mother):
    def study(self):
        print("child study")
c=child()
c.work()
c.cook()
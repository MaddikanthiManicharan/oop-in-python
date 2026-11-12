class demo:
    a=1
    b=3
    def abc(self):
        print("abc")
class sample(demo):
    c=3
    d=4
    def cde(self):
        print("cde")
s=sample()
print(s.a)
print(s.b)
s.abc()
s.cde()
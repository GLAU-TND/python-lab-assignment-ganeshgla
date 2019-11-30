class MyException(Exception):
    def __init__(self,v):
        self.v=v
    def __str__(self):
        return str(self.v)
def xyz(a,b):
    if a+b<150:
        raise MyException("Custom Exception Occured")
    else:
        return a+b
a=int(input())
b=int(input())
print(xyz(a,b))

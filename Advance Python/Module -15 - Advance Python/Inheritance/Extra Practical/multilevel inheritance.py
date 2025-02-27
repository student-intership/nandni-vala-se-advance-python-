class A:
    def fun1(self):
        l = [1,2,3,'Hello',1.25]
        print(l)

class B(A):
    def fun2(self):
        t = ('apple','banana','mango')
        print(t)

class C(B):
    def fun3(self):
        d = {1:'Apple',2:'Banana',3:'Mamgo'}
        print(d)


obj = C()
obj.fun1()
obj.fun2()
obj.fun3()
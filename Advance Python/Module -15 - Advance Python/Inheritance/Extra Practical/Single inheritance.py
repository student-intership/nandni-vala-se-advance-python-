class A:
    def fun1(self):
        l = [1,2,100,'Hello']
        print(l)

class B(A):
    def fun2(self):
        d1={1:'apple',2:'Banana',3:'Mango'}
        print(d1)


obj = B()
obj.fun1()
obj.fun2()
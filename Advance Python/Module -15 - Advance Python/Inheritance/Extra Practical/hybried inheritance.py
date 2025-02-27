class A :
    def fun1(self):
        print("This is Fun 1!!")

class B(A):
    def fun2(self):
        print("This is Fun2!!")

class C():
    def fun3(self):
        print("This is Fun3!!")

class D(B,C):
    def fun4(self):
        print("This is Fun4!!")


obj = B()
obj.fun1()
obj.fun2()

obj = D()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()
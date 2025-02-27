#single Inheritance
class A :
    def fun1(self):
        print("This is Fun 1!!")

class B(A):
    def fun2(self):
        print("This is Fun2!!")

obj = B()
obj.fun1()
obj.fun2()

#Multilevel
class A :
    def fun1(self):
        print("\nThis is Fun 1!!")

class B(A):
    def fun2(self):
        print("This is Fun2!!")

class C(B):
    def fun3(self):
        print("This is Fun3!!")
obj = C()
obj.fun1()
obj.fun2()
obj.fun3()

#Multiple
class A :
    def fun1(self):
        print("\nThis is Fun 1!!")

class B:
    def fun2(self):
        print("This is Fun2!!")

class C(A,B):
    def fun3(self):
        print("This is Fun3!!")
obj = C()
obj.fun1()
obj.fun2()
obj.fun3()
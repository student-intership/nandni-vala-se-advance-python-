class A:
    def fun1(self):
        l=[1,2,3]

class B:
    def fun1(self):
        l1=[1,2,3,4,5]
        print(l1)

class C(B,A):
    def fun1(self):
        super().fun1()
        l2=['Mango','Apple']
        print(l2)

obj = C()
obj.fun1()
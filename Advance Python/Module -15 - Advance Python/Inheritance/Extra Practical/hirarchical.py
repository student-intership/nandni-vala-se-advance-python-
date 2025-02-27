class A:
    def fun1(self):
        l1=[1,2,3,4]
        print(l1)

class B(A):
    def fun1(self):
        super().fun1()
        l2=['Apple','Banana']
        print(l2)

class C:
    def fun1(self):
        super().fun1()
        d = {1:"Hello",2:"c",3:"Java",4:"Python"}
        print(d)
    
class D(C,B):
    def fun1(self):
        super().fun1()
        t=(1,2,3)
        print(t)
        
obj = B()
obj.fun1()


obj = D()
obj.fun1()

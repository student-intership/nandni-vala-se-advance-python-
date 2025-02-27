class A:
    def fun1(self):
        n = int(input("Entger No Of Rows : "))
        for i in range(1,n+1):
            print("*"*i)

class B:
    def fun2(self):
        n1 = input("Enter String 1 : ")
        n2 = input("Enter String 2 : ")
        Merge_String =n1+n2
        print("\nMerge String : ",Merge_String)

class C(B,A):
    def fun3(self):
        l = [1,2,'Apple',2.50]
        print("\nlist Is : ",l) 

obj = C()
obj.fun1()
obj.fun2()
obj.fun3()
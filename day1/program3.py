def swap(a,b):
def swap_no(a,b):
    (a,b)=(b,a)
    print("Number 1 is",a)
    print("Number 2 is",b)
a=int(input("Enter Number 1: "))
b=int(input("Enter Number 2: "))
swap(a,b)
swap_no(a,b)

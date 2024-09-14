n1=float(input("enter a number:"))
n2=float(input("enter a number:"))
print('1.for addition\n','2.for subtraction\n','3.for Multiplication\n','4.for Division')
choice=int(input('enter a number'))
if choice==1:
    n3=n1+n2
    print(n3)
    print("addition successfully")  
elif choice==2:
    n3=n1-n2
    print(n3)
    print("subtraction successfully")
elif choice==3:
    n3=n1*n2
    print(n3)
    print("Multiplication Successfully")
elif choice==4:
    n3=n1%n2
    print(n3)
    print("Division Successfully")

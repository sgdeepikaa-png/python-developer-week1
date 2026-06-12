a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
op=input("Enter the operation you need to perform: ")
if(op=='+'):
    res=a+b
elif(op=="-"):
    res=a-b
elif(op=="*"):
    res=a*b
elif(op=="/"):
    if(b==0):
        print("Error : cannot divide by zero")
    else:
        res=a/b

else:
    print("Invalid operator")
print(a,op,b ,"=",res)

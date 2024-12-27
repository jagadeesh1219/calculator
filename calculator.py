def fun():
    number1=eval(input("enter number1:"))
    number2=eval(input("enter number2:"))
    operation=input("select operation:")
    if operation=="+":
        print(number1+number2)
    elif operation=="-":
        print(number1-number2)
    elif operation=="*":
        print(number1*number2)
    elif operation=="/":
        try:
            print(number1/number2)
        except ZeroDivisionError:
            print("undefined")
    elif operation=="%":
        print(number1%number2)
    else:
        print("enter valid numbers")
        
fun()
while(1):
    n=input("do you want to continue:(yes/no)").lower()
    if n=="yes":
        fun()
    else:
        break

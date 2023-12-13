print("SIMPLE CALCULATOR")
num1=int(input("Enter the first number: \n"))
num2=int(input("Enter the second number: \n"))
print("The basic operators are +,-,*,/,%")
ch=input("Enter the operator of your task to perform the task")
print("Calculation")
if ch=="+":
    add_result=num1+num2
    print("Addition_Result:\n",add_result)
if ch=="-":
    sub_result=num1-num2
    print("Subtraction_Result\n",sub_result)
if ch=="*":
    mul_result=num1*num2
    print("Multiplication_Result\n",mul_result)
if ch=="/":
    if num2==0:
        print("Error:Divsion not possible ")
    else:
        div_result=num1/num2
        print("Division_Result\n",div_result)
if ch=="%":
    mod_result=num1%num2
    print("Remainder_Result\n",mod_result)

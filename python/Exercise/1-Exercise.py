#Calculator using python

a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))

print("Kindly select operator\n(+,-,*,/) : ")

operator = input("Select Operator Only one : ")

if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(round(a/b,2))

else:
    print("Please select valid operator")

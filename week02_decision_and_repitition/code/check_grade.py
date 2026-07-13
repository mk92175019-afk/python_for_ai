print("===============Check Grade Programe===============")
print("Enter valid input number [0 - 100] or enter charecter only 'A'")

marks = input("Enter your marks to get Grade : ")

if marks == "A":
    print("student was absent")
elif marks >= str(90):
    print("Grade A")
elif marks >= str(70) and marks < str(90):
    print("Grade B")
elif marks >= str(50) and marks < str(70) :
    print("Grade C")
elif marks < str(50):
    print("Grade D")
    print("Failed")
elif marks == "A":
    print("student was absent")

print("==========Thank you for using check grade programe==========")

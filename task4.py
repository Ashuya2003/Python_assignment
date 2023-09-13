name = input("Name of the student: ")

subject1 = float(input("Enter the subject1 score: "))
if subject1 < 40:
    print("Fail")
else:
    print("Pass")

subject2 = float(input("Enter the subject2 score: "))
if subject2 < 40:
    print("Fail")
else:
    print("Pass")

subject3 = float(input("Enter the subject3 score: "))
if subject3 < 40:
    print("Fail")
else:
    print("Pass")

subject4 = float(input("Enter the subject4 score: "))
if subject4 < 40:
    print("Fail")
else:
    print("Pass")

subject5 = float(input("Enter the subject5 score: "))
if subject5 < 40:
    print("Fail")
else:
    print("Pass")

subject6 = float(input("Enter the subject6 score: "))
if subject6 < 40:
    print("Fail")
else:
    print("Pass")

result = subject1 + subject2 + subject3 + subject4 + subject5 + subject6

print("Sum of the subjects:", result)
print(name)

if result > 240 and result <= 600:
    if result > 600:
        print("Congrats for O+ grade")
    elif result > 580:
        print("Congrats for O grade")
    elif result > 570:
        print("Congrats for D++ grade")
    elif result > 560:
        print("Congrats for D+ grade")
    elif result > 550:
        print("Congrats for D grade")
    elif result > 530:
        print("Congrats for A+ grade")
    elif result > 500:
        print("Congrats for A grade")
    elif result > 400:
        print("Congrats for B grade")
else:
    if result > 200:
        print("Keep studying")
    else:
        print("Work hard - Overall Fail")

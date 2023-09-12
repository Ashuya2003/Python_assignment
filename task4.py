name= input("name of the student : ")
subject1 = float(input("Enter the subject1: "))
subject2 = float(input("Enter the subject2: "))
subject3 = float(input("Enter the subject3: "))
subject4 = float(input("Enter the subject4: "))
subject5 = float(input("Enter the subject5: "))
subject6 = float(input("Enter the subject6: "))
result=subject1 + subject2 + subject3 + subject4 + subject5 + subject6
print("sum of the subjects",result)
print(name)
if result>600:
    print("congrats for O+ grade")
elif result>580:
   print("congrats for O grade")
elif result>570:
   print("congrats for D++ grade")
elif result>560:
   print("congrats for D+ grade")
elif result>550:
   print("congrats for D grade")
elif result>530:
   print("congrats for A+ grade")
elif result>500:
   print("congrats for A grade")
elif result>400:
   print("congrats for B grade")
elif result>200:
   print("keep studying")
else:
       print("work hard")
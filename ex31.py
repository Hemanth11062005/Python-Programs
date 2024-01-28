#program to accept student details like student id, name,maths,physics, chemisty marks ,find total, avergae,grade
stuname = input("Enter student name:")
stuid = int(input("Enter student id:"))
matmak = int(input("enter maths marks:"))
chemmak = int(input("Enter chemistry marks:"))
phymak = int(input("Enter physics marks:"))

tot = matmak + phymak + chemmak
avg = tot//3

if(matmak>35 and phymak>35 and chemmak>35):
    if(matmak<=100):
        if(phymak<=100):
            if(chemmak<=100):
                if(avg>=60):
                    print("First grade")
                elif(avg>=50 and avg<60):
                    print("Second grade:")
                elif(avg>=35 and avg<50):
                    print("Third grade")
                else:
                    print("Invalid marks")
            else:
                print("Chemsistry exceeds 100 invalid")
        else:
            print("Physics exceeds 100 invalid")
    else:
        print("maths exceeds 100 invalid")
else:
    print("Fail")
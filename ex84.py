#sort

students = [("Squidward","F",60),
            ("Sandy","A",33),
            ("Patrick","D",36),
            ("Spongebob","B",20),
            ("Mr.Krabs","C",78)]

age = lambda ages : ages[2] # [2] is index
student_sorted = sorted(students,key = age)

for i in student_sorted:
    print(i)
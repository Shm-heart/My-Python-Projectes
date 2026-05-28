name = input("Enter Student Name: ")

m1 = int(input("Enter Mark 1: "))
m2 = int(input("Enter Mark 2: "))
m3 = int(input("Enter Mark 4: "))

total = m1 + m2 + m3
average = total / 3

print("\n----- STUDENT " \
"MARK LIST -----")
print("Student Name :",me)
print("Total Marks  :", total)
print("Average      :", average)

# Convert average into grade code
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

# Switch Case
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "F":
        print("Fail")
print("Grade Assesment")


eng = int(input("Enter English Marks: "))
if eng<0 or eng>100:
    print("Invalid Input")

lang = int(input("Enter Language Marks: "))
if lang <0 or lang>100:
    print("Invalid Input")

phy = int(input("Enter Physics Marks: "))
if phy<0 or phy>100:
    print("Invalid Input")

chem = int(input("Enter Chemistry Marks: "))
if chem<0 or chem>100:
    print("Invalid Input")

math = int(input("Enter Math Marks: "))
if math<0 or math>100:
    print("Invalid Input")

comp = int(input("Enter Computer Marks: "))
if comp<0 or comp>100:
    print("Invalid Input")

total = eng+lang+phy+chem+math+comp
percentage = total/6

if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
else:
    print("Grade: C+")
    
print("Total: ",total)
print("Percentage: ",percentage)
chemistry = int(input("Enter Chemistry Grade Here: "))
maths = int(input("Enter Math Grade Here: "))
physics = int(input("Enter PhysicsGrade Here: "))

def grade():
    percentage = chemistry + maths + physics

    percentage_total = int(percentage / 300 * 100)

    if percentage_total < 40:
        print("You Failed")
    elif percentage_total >= 40 and percentage_total < 50:
        print("D")
    elif percentage_total >= 50 and percentage_total < 60: 
        print("C")
    elif percentage_total >= 60 and percentage_total < 70: 
        print("B")
    else:
        print("A")
    
    print(percentage)
    print(percentage_total)
    return percentage_total

grade()
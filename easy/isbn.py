
number = str(input("Enter number: "))

def isbn_solution():
    for num in number: 
        count = ''
        print(num)
        if index(num)%2==0: 
            print('/')
        else:
            print('z')
 
    print('')

isbn_solution()
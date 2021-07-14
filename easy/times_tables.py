x = int(input("Enter first number here"))
def timestables():
    for i in range(x):
        if i == 0 :
            continue
        for j in range (x):
            if j == 0: 
                continue   
            print('{:3}'.format(i*j), end=' ')
        print()
timestables()
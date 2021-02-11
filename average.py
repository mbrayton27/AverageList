
"""
check = False;
while check == False:
    try:
        num_list = int(input("How many numbers do you want in your list? "))
        if num_list < 1:
            print("Please enter a positive number or zero.")
            check = False;
        else :
            check = True;
            break;
    except ValueError:
        print("Please enter an integer")
        continue

array = []
for x in range(0, num_list):
    check = False
    while check == False:
        try:
            array.append(int(input("Enter number ")))
            check = True
        except ValueError:
            print("Please enter an integer")
            check = False
            continue

sum = 0
for y in range(0, num_list):
    sum = int(array[y]) + sum

sum /= (y+1)
print("The average of the list is " + str(sum))
"""
def avg(a, b, c, d):
    return (a + b + c + d)/4

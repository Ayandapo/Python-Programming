# Question 1
Total=0
count=0
Number=input('Enter Number "enter done to halt";')
while True:
    try:
        if Number != 'done':
            Total=Total+int(Number)
            count=count+1
            Number=input('Enter Number "enter done to halt";')
        else:
            break
    except Exception as ValueError:
        print('Invalid Input')
        Number=input('Enter Number "enter done to halt";')

print("Total:", Total)
print("count:", count)
print("Average:",Total/count)

# Question 2
Maximum=0
Minimum=0
Number=input('Enter Number"Enter done to stop":')
while True:
    if Number!='done':
        if int(Number)>Maximum:
            Maximum=int(Number)
        if int(Number)<Minimum:
            Minimum=int(Number)
        Number=input('Enter Number"Enter done to stop":')
    else:
        break

print('Maximum is equals to',Maximum)
print('Minimum is equals to',Minimum)

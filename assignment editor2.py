#question3
score=input('Enter score:')
try:
    Score=float(score)
except:
    print('Error!,Grade out of range')
if 0.9<=Score<=1.0:
    print('A')
elif 0.8<=Score<0.9:
    print('B')
elif 0.7<+Score<0.8:
    print('C')
elif 0.6<=Score<0.7:
    print ('D')
else:
    print('F')

    

#question3
try:
    score=input('Enter score:')
    Score=float(score)
except:
    print('Error!,Grade out of range')
if 0.9<=Score<=1.0:
    print('A')
elif 0.8<=Score<0.9:
    print('B')
elif 0.7<=Score<0.8:
    print('C')
elif 0.6<=Score<0.7:
    print ('D')
elif 0.0<=Score<0.6:
    print('F')
else:
    print('Error!,out of range')
    

    

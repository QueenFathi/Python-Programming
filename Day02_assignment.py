#Exercise 1
hours=int(input('Enter Hours: '))
print(hours)
rate=int(input('Enter Rate: '))
print(rate)
if hours>40:
    pay=hours*(1.5*rate)
    
else:
    pay=hours*rate
    
print('Pay:', pay)


#Exercise 2
print('Exercise 2')
try:
    hours=int(input('Enter Hours: '))
    print(hours)
    rate=int(input('Enter Rate: '))
    print(rate)
    if hours>40:
        pay=hours*(1.5*rate)
    
    else:
        pay=hours*rate
        
    print('Pay:', pay)
except:
    print('Error, please enter a numeric input')
    

#Exercise 3
try:
    score=float(input('Enter score: '))
    print(score)
    if score <=1.0:
        if score>=0.9:
            print('A')
        elif score>=0.8:
            print('B')
        elif score>=0.7:
            print('C')
        elif score>=0.6:
            print('D')
        else:
            print('F')
            
    else:
        print('Bad score')
except:
    print('Bad score')
  
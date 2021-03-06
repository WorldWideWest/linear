import pandas as pd

## Defining the data ##

data = pd.DataFrame({
            'Hours studied (x)': [0, 10, 8, 7, 4, 8, 10, 11, 15, 20, 5, 2, 13, 10, 6],
            'Points won (y)': [15, 78, 70, 65, 50, 73, 80, 88, 95, 96, 55, 32, 75, 80, 60]
            })



## Calculations ##

if len(data['Hours studied (x)']) == len(data['Points won (y)']):

    xHat = sum(data['Hours studied (x)']) / len(data['Hours studied (x)'])
    yHat = sum(data['Points won (y)']) / len(data['Points won (y)'])

    xSub = [round((hour - xHat), 4) for hour in data['Hours studied (x)']]
    ySub = [round((hour - yHat), 4) for hour in data['Points won (y)']]
    
    


else:
    print('The data in the two rows has different lenghts')


## Slope of the line ##

# b = r * (Sy / Sx) 
# S - standard deviation
# r = Sum((x-xHat)(y-yHat)) / SQRT(Sum(x-xHat)^2 Sum(y-yHat)^2)
# r - Pearsons correlation coefficient











## Intercept of the line ##

# a = yHat - bxHat
# x and y Hat - mean values of their columns


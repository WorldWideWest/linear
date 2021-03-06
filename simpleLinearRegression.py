import pandas as pd
import math

## Defining the data ##

data = pd.DataFrame({
            'Hours studied (x)': [0, 10, 8, 7, 4, 8, 10, 11, 15, 20, 5, 2, 13, 10, 6],
            'Points won (y)': [15, 78, 70, 65, 50, 73, 80, 88, 95, 96, 55, 32, 75, 80, 60]
            })
## Calculations ##

r, Sx, Sy, xHat, yHat = 0, 0, 0, 0, 0

if len(data['Hours studied (x)']) == len(data['Points won (y)']):

    xHat = sum(data['Hours studied (x)']) / len(data['Hours studied (x)'])
    yHat = sum(data['Points won (y)']) / len(data['Points won (y)'])

    xSub = [round((hour - xHat), 4) for hour in data['Hours studied (x)']]
    ySub = [round((hour - yHat), 4) for hour in data['Points won (y)']]
  
    xGr = [round((hour - xHat)**2, 4) for hour in data['Hours studied (x)']]
    yGr = [round((hour - yHat)**2, 4) for hour in data['Points won (y)']]
   

    product = []
    sumProduct = 0
    
    if len(xSub) == len(ySub):
        for index in range(len(xSub)):
            product.append(round(xSub[index] * ySub[index], 4))
    else:
        print('The data in the two rows has different lenghts')
    
    # Calculations for b #

    r = sum(product) / math.sqrt(sum(xGr) * sum(yGr))
    
    Sx = math.sqrt(sum(xGr)/(len(xGr)-1))
    Sy = math.sqrt(sum(yGr)/(len(yGr)-1))

else:
    print('The data in the two rows has different lenghts')


## Slope of the line ##

# b = r * (Sy / Sx) 
# S - standard deviation
# r = Sum((x-xHat)(y-yHat)) / SQRT(Sum(x-xHat)^2 Sum(y-yHat)^2)
# r - Pearsons correlation coefficient
# Sn = sqrt((Sum(n-nHat)^2)/(n-1))

b = r * (Sy/Sx)

## Intercept of the line ##

# a = yHat - bxHat
# x and y Hat - mean values of their columns

a = yHat - b * xHat

## Testing the algorithm ##

result = [round((a + b * hour), 0) for hour in data['Hours studied (x)']]

for i in range(len(xSub)):
    print([xSub[i], ySub[i], product[i], xGr[i], yGr[i]])


print("Results")

for i in range(len(result)):
    print([data.iloc[i,0], data.iloc[i, 1], result[i], result[i] - data.iloc[i, 1], round((result[i] - data.iloc[i, 1]) / data.iloc[i, 1 ] * 100, 3)])




import pandas as pd

## Data ##

data = pd.DataFrame({
    'milesTraveled (x1)': [89, 66, 78, 111, 44, 77, 80, 66, 109, 76],
    'numDeliveries (x2)': [4, 1, 3, 6, 1, 3, 3, 2, 5, 3],
    'gasPrice (x3)': [3.84, 3.19, 3.78, 3.89, 3.57, 3.57, 3.03, 3.51, 3.54, 3.25],
    'travelTime (y)': [7, 5.4, 6.6, 7.4, 4.8, 6.4, 7, 5.6, 7.3, 6.4]
    })

print(data.corr())



# y = b0 + b1*x1 + ... + bi*xi

# b0 = yHat - b1*x1Hat - b2*x2Hat - ... - bi * xiHat

# b1 = Sum (x2**2) * Sum(x1*y) -  Sum(x1*x2) * Sum(x2*y) / Sum(x1**2) * Sum(x2**2) - Sum(x1 * x2)**2

# Sum(xi**2) = Sum(xi**2) - (Sum(xi)**2  / N)

# Sum(xi*y) = Sum(xi * y) - (Sum(xi) * Sum(y) / N)

# Sum(x1 * x2) = Sum(x1 * x2) - (Sum(xi) - Sum(x2) / N)



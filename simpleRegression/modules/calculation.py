import pandas as pd
from math import sqrt



class Calculation:
    def __init__(self, dataFrame):
        self.dataFrame = pd.DataFrame(dataFrame)
        self.columns = [col for col in self.dataFrame.columns]

    def baseCalculation(self):
        
        # Extracting the mean
        xHat = sum(self.dataFrame[self.columns[0]]) / len(self.dataFrame[self.columns[0]])
        yHat = sum(self.dataFrame[self.columns[1]]) / len(self.dataFrame[self.columns[1]])
        
        xSub = [round((predictor - xHat), 4) for predictor in self.dataFrame[self.columns[0]]] # (x - xHat)
        ySub = [round((predictions - yHat), 4) for predictions in self.dataFrame[self.columns[1]]] # (y - yHat)

        xGr = [round((predicor - xHat)**2, 4) for predictor in self.dataFrame[self.columns[0]]] # (x - xHat)^2
        yGr = [round((predictions - yHat)**2, 4) for predictions in self.dataFrame[self.columns[1]]] # (y - yHat)^2
        
        product = []
        if len(xSub) != len(ySub):
            print('The data in the two rows has different lenghts')
        else:
            for index in range(len(xSub)):
                product.append(round(xSub[index] * ySub[index], 4)) # (x - xHat) * (y - yHat)

        r = sum(product) / sqrt(sum(xGr) * sum(yGr)) # Correlation coefficient
        Sx = sqrt(sum(xGr)/(len(xGr)-1)) # Standard deviation of x
        Sy = sqrt(sum(yGr)/(len(yGr)-1)) # Standard deviation of y

        return [xHat, yHat, r, Sx, Sy] # baseParams

    def fit(self, baseParams):
        
        xHat = baseParams[0]
        yHat = baseParams[1]
        r = baseParams[2]
        Sx = baseParams[3]
        Sy = baseParams[4]

        a = r * (Sx / Sy) # slope
        b = yHat - b * xHat # intercept

        return [a, b]

    def predict(self, slope, intercept):
        return [round((slope + intercept * data)) for data in self.dataFrame[self.columns[0]]]

        





        
        

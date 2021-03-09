import pandas as pd




class Calculation:
    def __init__(self, dataFrame):
        self.dataFrame = pd.DataFrame(dataFrame)

    def centralTendencyMeasurements(self):
        
        columns = [col for col in self.dataFrame.columns]
        
        # Extracting the mean
        xHat = sum(self.dataFrame[columns[0]]) / len(self.dataFrame[columns[0]])
        yHat = sum(self.dataFrame[columns[1]]) / len(self.dataFrame[columns[1]])
        
        xSub = [round((predictor - xHat), 4) for predictor in self.dataFrame[columns[0]]]
        ySub = [round((predictions - yHat), 4) for predictions in self.dataFrame[columns[1]]]




        
        

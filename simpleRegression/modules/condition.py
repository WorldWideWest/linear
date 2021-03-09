import pandas as pd


class Condition:
    
    def __init__(self, dataFrame, columns):
        self.dataFrame = pd.DataFrame(dataFrame)
        self.columns = columns # the maximum num of colums are two, because this is a simple LR and one column is reserved  for the predictor and one for the predictions (x, y)
        
    def Check(self):
        if len(self.columns) != 2:
            print("Maximum number of columns are two. This is because this is a simple linear regression and one colum is reserved for the predictor and one for the predictions")
            return False
        else:
            return self.dataFrame[self.columns]

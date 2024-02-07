import pandas as pd
import numpy as np

# get last used ID
previousList = pd.read_csv('pc.csv', usecols=range(1,4))
previousId = previousList.iloc[-1]['id']

pcType = input("What is your current PC type: ")
name = input("What is your name: ")

def convertInput(pcType, name):
    currentId = previousId + 1
    entry = np.array([[currentId, pcType, name]])
    pd.DataFrame(entry).to_csv('pc.csv', mode='a', header=False)


convertInput(pcType, name)
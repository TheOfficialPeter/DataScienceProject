import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# 4.1
BDW = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
print(BDW.head(5))

BDW1 = BDW.drop(BDW.index[0])
print(BDW1[:3])

# 4.2
Indexcount_year = {}
for year in BDW1["Year"]:
    if Indexcount_year.get(year) == None:
        Indexcount_year[year] = 1
    else:
        Indexcount_year[year] = Indexcount_year[year] + 1

Indexpercent_year = {}
index = 0
for year in BDW1["Year"]:
    if Indexpercent_year.get(year) == None:
        Indexpercent_year[year] = index
    index += 1

# 4.3
Maths_Stats = []
Physic_Sci = []
Engine = []
Comp_Sci = []
Year = []

for index, record in BDW1.iterrows():
    Maths_Stats.append(record['Math and Statistics'])
    Physic_Sci.append(record['Physical Sciences'])
    Engine.append(record['Engineering'])
    Comp_Sci.append(record['Computer Science'])
    Year.append(record['Year'])

# 4.4
Selected4Majors = np.array([Maths_Stats, Physic_Sci, Engine, Comp_Sci], dtype=float)

Majors = {
    'Maths_Stats': 1,
    'Physic_Sci': 2,
    'Engine': 3,
    'Comp_Sci': 4
}

def displayData(Year, majorList):
    for major_name, major_index in Majors.items():
            major_data = majorList[major_index - 1]
            plt.plot(Year, major_data, label=major_name)

    plt.xlabel('Year')
    plt.ylabel('Selected4Degrees')
    plt.title('Percentage of Selected4Degrees per Years')

    plt.legend(loc='upper left')
    plt.show()

displayData(Year, Selected4Majors)

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# read the csv files
df1 = pd.read_csv('exam1.csv')
df2 = pd.read_csv('exam2.csv')
data = pd.concat([df1, df2])

# create frequency tables
frequency = {"Average hours on campus": {}, "Student age": {}, "Student mark": {}}

# average hours 
for value in data['average_hours']:
    if str(value) in frequency['Average hours on campus']:
        frequency['Average hours on campus'][str(value)] = frequency['Average hours on campus'][str(value)] + 1
    else:
        frequency['Average hours on campus'][str(value)] = 0

# age
for value in data['age']:
    if value >= 18 and value <= 25:
        value = "18-25"
    elif value >= 25 and value <= 35:
        value = "25-35"
    elif value >= 35 and value <= 45:
        value = "35-45"
    elif value >= 45:
        value = "over 45"

    if str(value) in frequency['Student age']:
        frequency['Student age'][str(value)] = frequency['Student age'][str(value)] + 1
    else:
        frequency['Student age'][str(value)] = 0

# mark
for value in data['mark']:
    if str(value) in frequency['Student mark']:
        frequency['Student mark'][str(value)] = frequency['Student mark'][str(value)] + 1
    else:
        frequency['Student mark'][str(value)] = 0

#print(frequency)

# display bar chart for amount of students per age group
"""
age_groups = []
ages = data['age'].tolist()
ages.sort()

for age in ages:
    if age >= 18 and age <= 25:
        age_groups.append('18-25')
    elif age >= 25 and age <= 35:
        age_groups.append('25-35')
    elif age >= 35 and age <= 45:
        age_groups.append('35-45')
    elif age >= 45 and age <= 50:
        age_groups.append('over 45')
    else:
        print(age)
"""
plt.bar(frequency['Student age'].keys(), frequency['Student age'].values())
plt.title('number of students per age group')
plt.xlabel('age group')
plt.ylabel('number of students')
plt.show()

# display line chart for student test marks against how many hours they spend on campus average
marks = data['mark']
average_hours = data['average_hours']
plt.xlabel('marks on test')
plt.ylabel('average hours spent on campus')
plt.plot(marks, average_hours)
plt.show()

# display graphs for how many marks students get on test against how much time they spent writing the test
marks = data['mark']
time_taken = data['time_taken']
plt.xlabel('mark on test')
plt.ylabel('time spent on test')
plt.scatter(marks, time_taken)
plt.show()

# display graph for how old the students are compared to how much time they spend on campus
ages = data['age']
average_hours = data['average_hours']
plt.xlabel('ages')
plt.ylabel('hours spent on campus')
plt.scatter(ages, average_hours)
plt.show()
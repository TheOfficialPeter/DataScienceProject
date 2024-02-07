import pandas as pd
import random

for i in range(1,3):
    studentNum = []
    age = []
    hours = []
    mark = []
    percentage = []
    timeTaken = []

    counter = 0 # count student numbers
    for i2 in range(150):
        counter += 1

        # student number
        studentNum.append(counter)
        
        # age
        age.append(random.randint(18,50))

        # average hours on campus
        hours.append(random.randint(1,5))

        # student marks and calculate percentage
        x = random.randint(50,130)
        mark.append(x)
        x = round(int(x)/130*100, 2)
        percentage.append(x)
        
        # students time taken on the test
        timeTaken.append(random.randint(100,180))

    # save the records in the csv files
    df = pd.DataFrame({"student_num": studentNum, "age": age, "average_hours": hours, "mark": mark, "percentage": percentage, "time_taken": timeTaken})
    df.to_csv('exam'+str(i)+'.csv')
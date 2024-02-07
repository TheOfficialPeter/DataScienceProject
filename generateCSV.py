import pandas as pd
import random

df = pd.read_csv('studentInfo.txt', index_col=0)

row_counter = 0
for index in range(150):
    row_counter += 1

    random_record = random.randint(0,19)
    row = df.loc[random_record]

    final_row = [row_counter]

    for value in row:
        final_row.append(value)

    final_row = pd.DataFrame(final_row).transpose()
    final_row.to_csv('exam1.csv', mode='a', header=False, index=False)
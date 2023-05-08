import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

exam_data = dict(
    student_name=['Daan', 'Emma', 'Katherine', 'Luuk', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Sophie'],
    grade=[8.5, 9, 6.5, np.nan, 6, 5, 7.5, np.nan, 4, 7],
    attempts=[1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    qualify=['yes', 'yes', 'yes', 'no grade', 'yes', 'no', 'yes', 'no grade', 'no', 'yes']
)

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 1. Create and display a DataFrame from a specified dictionary data which has the index labels.
df = pd.DataFrame(exam_data, labels)
# print(df)
# 2. Show the 'student_name' and 'grade' columns from the DataFrame for the students who had a\
# number of attempts in the examination greater than 2.
# print(df[df['attempts'] > 2][['student_name', 'grade']])

# 3. List the name of students who will pass the exam, i.e. grade above 5.5.
# print(df[df['grade']>=5.5][['student_name']])

# 4. Show the names of students whose grade is missing, i.e. is NaN.
# print(df[df.grade.isnull()][['student_name']])

#5. Calculate the mean and standard deviation of the grades for all students in the DataFrame.
# print('Mean:', df.grade.mean())
# print('Mean:', df['grade'].mean())
#
# print('Standard Dev:', df['grade'].std())
# print('Standard Dev:', df.grade.std())

#6. Replace the missing grades by a pass grade, i.e. 6, and update the corresponding 'qualify' rows.
# df.grade = df.grade.replace(np.nan, 6)
# df.qualify = df.qualify.replace('no grade', 'yes')
# print(df)

# 7. Using matplotlib Python library, create some plots to present a visual representation of the
# information in the DataFrame of task 6, such as a histogram or a box plot of students grades,
# and a bar plot for the number of attempts per each student. Use PyPlot methods to improve the
# readability of your figures.

plt.barh(df.student_name, df.grade)
plt.xlabel('Points')
plt.ylabel('Student Names')
plt.show()

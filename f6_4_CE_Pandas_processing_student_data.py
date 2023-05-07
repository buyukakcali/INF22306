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

# 2. Show the 'student_name' and 'grade' columns from the DataFrame for the students who had a\
# number of attempts in the examination greater than 2.

# 3. List the name of students who will pass the exam, i.e. grade above 5.5.

# 4. Show the names of students whose grade is missing, i.e. is NaN.

#5. Calculate the mean and standard deviation of the grades for all students in the DataFrame.

#6. Replace the missing grades by a pass grade, i.e. 6, and update the corresponding 'qualify' rows.

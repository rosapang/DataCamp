'''
Choosing a joining strategy
Suppose you have two DataFrames: students (with columns 'StudentID', 'LastName', 'FirstName', and 'Major') and midterm_results (with columns 'StudentID', 'Q1', 'Q2', and 'Q3' for their scores on midterm questions).

You want to combine the DataFrames into a single DataFrame grades, and be able to easily spot which students wrote the midterm and which didn't (their midterm question scores 'Q1', 'Q2', & 'Q3' should be filled with NaN values).

You also want to drop rows from midterm_results in which the StudentID is not found in students.

Which of the following strategies gives the desired result?

INSTRUCTIONS
50 XP
INSTRUCTIONS
50 XP
Possible Answers
A left join: grades = pd.merge(students, midterm_results, how='left').
press 1
A right join: grades = pd.merge(students, midterm_results, how='right').
press 2
An inner join: grades = pd.merge(students, midterm_results, how='inner').
press 3
An outer join: grades = pd.merge(students, midterm_results, how='outer').
press 4
'''
# A left join: grades = pd.merge(students, midterm_results, how='left').

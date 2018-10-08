'''Merging company DataFrames
Suppose your company has operations in several different cities under several different managers. The DataFrames revenue and managers contain partial information related to the company. That is, the rows of the city columns don't quite match in revenue and managers (the Mendocino branch has no revenue yet since it just opened and the manager of Springfield branch recently left the company).

The DataFrames have been printed in the IPython Shell. If you were to run the command combined = pd.merge(revenue, managers, on='city'), how many rows would combined have?'''

#           city  revenue
# 0       Austin      100
# 1       Denver       83
# 2  Springfield        4

#         city   manager
# 0     Austin  Charlers
# 1     Denver      Joel
# 2  Mendocino     Brett

INSTRUCTIONS
50 XP
Possible Answers
0 rows.
press 1
2 rows.
press 2
3 rows.
press 3
4 rows.
press 4

# 2 rows


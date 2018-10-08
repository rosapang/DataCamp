'''Joining by Index
The DataFrames revenue and managers are displayed in the IPython Shell. Here, they are indexed by 'branch_id'.

Choose the function call below that will join the DataFrames on their indexes and return 5 rows with index labels [10, 20, 30, 31, 47]. Explore each of them in the IPython Shell to get a better understanding of their functionality.
'''

#                   city  revenue state
# branch_id                            
# 10              Austin      100    TX
# 20              Denver       83    CO
# 30         Springfield        4    IL
# 47           Mendocino      200    CA

#                 branch   manager state
# branch_id                             
# 10              Austin  Charlers    TX
# 20              Denver      Joel    CO
# 47           Mendocino     Brett    CA
# 31         Springfield     Sally    MO

INSTRUCTIONS
50 XP
Possible Answers
pd.merge(revenue, managers, on='branch_id').
press 1
pd.merge(managers, revenue, how='left').
press 2
revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer').
press 3
managers.join(revenue, lsuffix='_mgn', rsuffix='_rev', how='left').
press 4

# revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer').
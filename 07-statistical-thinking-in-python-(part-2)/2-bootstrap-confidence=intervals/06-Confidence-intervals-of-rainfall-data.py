'''
Confidence intervals of rainfall data
A confidence interval gives bounds on the range of parameter values you might expect to get if we repeat our measurements. For named distributions, you can compute them analytically or look them up, but one of the many beautiful properties of the bootstrap method is that you can just take percentiles of your bootstrap replicates to get your confidence interval. Conveniently, you can use the np.percentile() function.

Use your bootstrap replicates you just generated to compute the 95% confidence interval. That is, give the 2.5th and 97.5th percentile of your bootstrap replicates stored as bs_replicates. What is the 95% confidence interval?

INSTRUCTIONS
50 XP
Possible Answers
(765, 776) mm/year
press 1
(780, 821) mm/year
press 2
(761, 817) mm/year
press 3
(761, 841) mm/year
press 4
'''

# (780, 821) mm/year

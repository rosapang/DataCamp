'''
Simulating a null hypothesis concerning correlation
The observed correlation between female illiteracy and fertility in the data set of 162 countries may just be by chance; the fertility of a given country may actually be totally independent of its illiteracy. You will test this null hypothesis in the next exercise.

To do the test, you need to simulate the data assuming the null hypothesis is true. Of the following choices, which is the best way to to do it?

ANSWER THE QUESTION
50 XP
Possible Answers
Click or Press Ctrl+1 to focus
Choose 162 random numbers to represent the illiteracy rate and 162 random numbers to represent the corresponding fertility rate.
press 1
Do a pairs bootstrap: Sample pairs of observed data with replacement to generate a new set of (illiteracy, fertility) data.
press 2
Do a bootstrap sampling in which you sample 162 illiteracy values with replacement and then 162 fertility values with replacement.
press 3
Do a permutation test: Permute the illiteracy values but leave the fertility values fixed to generate a new set of (illiteracy, fertility) data.
press 4
Do a permutation test: Permute both the illiteracy and fertility values to generate a new set of (illiteracy, fertility data).
press 5
'''

# Do a permutation test: Permute the illiteracy values but leave the fertility values fixed to generate a new set of (illiteracy, fertility) data.
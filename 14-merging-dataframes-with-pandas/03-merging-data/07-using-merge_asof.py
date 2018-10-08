'''
Using merge_asof()

Similar to pd.merge_ordered(), the pd.merge_asof() function will also merge values in order using the on column, but for each row in the left DataFrame, only rows from the right DataFrame whose 'on' column values are less than the left value will be kept.

This function can be use to align disparate datetime frequencies without having to first resample.

Here, you'll merge monthly oil prices (US dollars) into a full automobile fuel efficiency dataset. The oil and automobile DataFrames have been pre-loaded as oil and auto. The first 5 rows of each have been printed in the IPython Shell for you to explore.

These datasets will align such that the first price of the year will be broadcast into the rows of the automobiles DataFrame. This is considered correct since by the start of any given year, most automobiles for that year will have already been manufactured.

You'll then inspect the merged DataFrame, resample by year and compute the mean 'Price' and 'mpg'. You should be able to see a trend in these two columns, that you can confirm by computing the Pearson correlation between resampled 'Price' and 'mpg'.

INSTRUCTIONS
100XP
Merge auto and oil using pd.merge_asof() with left_on='yr' and right_on='Date'. Store the result as merged.
Print the tail of merged. This has been done for you.
Resample merged using 'A' (annual frequency), and on='Date'. Select [['mpg','Price']] and aggregate the mean. Store the result as yearly.
Hit Submit Answer to examine the contents of yearly and yearly.corr(), which shows the Pearson correlation between the resampled 'Price' and 'mpg'.
'''

# oil
#         Date  Price
# 0 1970-01-01   3.35
# 1 1970-02-01   3.35
# 2 1970-03-01   3.35
# 3 1970-04-01   3.35
# 4 1970-05-01   3.35

# auto
#     mpg  cyl  displ   hp  weight  accel         yr origin  \
# 0  18.0    8  307.0  130    3504   12.0 1970-01-01     US   
# 1  15.0    8  350.0  165    3693   11.5 1970-01-01     US   
# 2  18.0    8  318.0  150    3436   11.0 1970-01-01     US   
# 3  16.0    8  304.0  150    3433   12.0 1970-01-01     US   
# 4  17.0    8  302.0  140    3449   10.5 1970-01-01     US   

#                         name  
# 0  chevrolet chevelle malibu  
# 1          buick skylark 320  
# 2         plymouth satellite  
# 3              amc rebel sst  
# 4                ford torino

# Merge auto and oil: merged
merged = pd.merge_asof(auto, oil, left_on='yr', right_on='Date')

# Print the tail of merged
print(merged.tail())

# Resample merged: yearly
yearly = merged.resample('A',on='Date')[['mpg','Price']].mean()

# Print yearly
print(yearly)

# Print yearly.corr()
print(yearly.corr())
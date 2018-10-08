'''
Correlation of offspring and parental data
In an effort to quantify the correlation between offspring and parent beak depths, we would like to compute statistics, such as the Pearson correlation coefficient, between parents and offspring. To get confidence intervals on this, we need to do a pairs bootstrap.

You have already written a function to do pairs bootstrap to get estimates for parameters derived from linear regression. Your task in this exercise is to modify that function to make a new function with call signature draw_bs_pairs(x, y, func, size=1) that performs pairs bootstrap and computes a single statistic on the pairs samples defined by func(bs_x, bs_y). In the next exercise, you will use pearson_r for func.

INSTRUCTIONS
100 XP
INSTRUCTIONS
100 XP
We have provided your original draw_bs_pairs_linreg() function (named as draw_bs_pairs()). Modify this function to make the draw_bs_pairs() function described above. Be sure to adjust the doc string appropriately, and remember that in this modified function, you only need to return a single statistic.
Things to keep in mind: The modified function requires an additional func parameter and returns only bs_replicates, as opposed to bs_slope_reps and bs_intercept_reps as the function in the sample code does.
'''

def draw_bs_pairs(x, y, func, size=1):
    """Perform pairs bootstrap for single statistic."""

    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))

    # Initialize replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_replicates[i] = func(bs_x, bs_y)

    return bs_replicates
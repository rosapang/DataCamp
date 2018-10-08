'''Array orientation
matrix picture

The commands

In [1]: plt.pcolor(A, cmap='Blues')
In [2]: plt.colorbar()
In [3]: plt.show()
produce the pseudocolor plot above using a Numpy array A. Which of the commands below could have generated A?

numpy and matplotlib.pyplot have been imported as np and plt respectively. Play around in the IPython shell with different arrays and generate pseudocolor plots from them to identify which of the below commands could have generated A.

INSTRUCTIONS
50 XP
Possible Answers
A = np.array([[1, 2, 1], [0, 0, 1], [-1, 1, 1]])
press 1
A = np.array([[1, 0, -1], [2, 0, 1], [1, 1, 1]])
press 2
A = np.array([[-1, 0, 1], [1, 0, 2], [1, 1, 1]])
press 3
A = np.array([[1, 1, 1], [2, 0, 1], [1, 0, -1]])
press 4'''

# A = np.array([[1, 0, -1], [2, 0, 1], [1, 1, 1]])
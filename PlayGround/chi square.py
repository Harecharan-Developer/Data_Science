import numpy as np
from scipy.stats import chi2_contingency
import numpy as np

# create the contingency table
observed = np.array([[60, 235], [141, 34]])

# perform the chi-square test
chi2, p, dof, expected = chi2_contingency(observed)

# print the results
print("Chi-square statistic:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)
print("Expected frequencies:\n", expected)
# define the observed values
observed = [[60, 235], [141, 34]]

# calculate the row and column totals
row_totals = [sum(row) for row in observed]
col_totals = [sum(col) for col in zip(*observed)]
total = sum(row_totals)

# calculate the expected values
expected = [[(row_total * col_total) / total for col_total in col_totals] for row_total in row_totals]

# calculate the chi-square statistic
chi2 = sum([(observed[i][j] - expected[i][j])**2 / expected[i][j] for i in range(len(observed)) for j in range(len(observed[0]))])

# calculate the degrees of freedom
dof = (len(observed) - 1) * (len(observed[0]) - 1)

# calculate the p-value
p = 1 - chi2_contingency(observed)[1]

# print the results
print("Chi-square statistic:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)
print("Expected frequencies:\n", expected)



# define the data
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# define the number of bootstrap samples
n_samples = 1000

# define the size of each bootstrap sample
sample_size = len(data)

# generate the bootstrap samples
samples = np.random.choice(data, size=(n_samples, sample_size), replace=True)

# calculate the mean of each bootstrap sample
means = np.mean(samples, axis=1)

# calculate the 95% confidence interval using the percentile method
lower = np.percentile(means, 2.5)
upper = np.percentile(means, 97.5)

# print the results
print("Bootstrap percentile confidence interval:")
print("Lower:", lower)
print("Upper:", upper)

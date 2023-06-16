""" for r in range(1, 11):
    for c in range(1, 11):
        for n in range(2, 12):
            if (r*c*(n-1) <= 10) and ((r-1)*(c-1) <= 10) and ((c-1)*(r-1) != 0):
                print(f"r={r}, c={c}, n={n}")


# Calculate ANOVA with replicate function
        row_data = [sm.stats.anova_lm(sm.stats.ols(formula='~C(j) + C(i):C(j)', data={'X': data}).fit()) for i in range(row_count)]
        column_data = [sm.stats.anova_lm(sm.stats.ols(formula='~C(i) + C(i):C(j)', data={'X': data}).fit()) for j in range(column_count)]
        interaction_data = sm.stats.anova_lm(sm.stats.ols(formula='~C(i) + C(j) + C(i):C(j)', data={'X': data}).fit

 """
from scipy import stats

# create the data for the ANOVA test
data = [[34, 28, 29, 31], 
        [37, 32, 35, 29], 
        [38, 30, 33, 28]]

# perform the two-way ANOVA test with replication
F, p = stats.f_oneway(*data)
print("F-value: {0}".format(F))
print("p-value: {0}".format(p))

# validate the final result with alpha=5%
if p < 0.05:
    print("Reject null hypothesis at alpha=5%. There is significant evidence to suggest that at least one of the means is different from the others.")
else:
    print("Fail to reject null hypothesis at alpha=5%. There is insufficient evidence to suggest that at least one of the means is different from the others.")

# validate the final result with alpha=1%
if p < 0.01:
    print("Reject null hypothesis at alpha=1%. There is significant evidence to suggest that at least one of the means is different from the others.")
else:
    print("Fail to reject null hypothesis at alpha=1%. There is insufficient evidence to suggest that at least one of the means is different from the others.")
#use the scipy library to validate the final result of a two anova test with replication alpha=5% and 1 %
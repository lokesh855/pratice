import scipy.stats as stats
import seaborn as sns
import pandas as pd
import numpy as np
dataset=sns.load_dataset("tips")
dataset.head(10)
dataset
dataset_table=pd.crosstab(dataset["sex"],dataset["smoker"])
print(dataset_table)
dataset_table.values
observed_values=dataset_table.values
print("observed values:\n",observed_values)
no_of_rows=len(dataset_table.iloc[0:210])
no_of_cols=len(dataset_table.iloc[0,0:2])
ddof=(no_of_rows-1)*(no_of_cols-1)
print("degree of freedom:",ddof)
alpha=0.05
val=stats.chi2_contingency(dataset_table)
val
expected_values=val[3]
expected_values
from scipy.stats import chi2
chi_square=sum([(o-e)**2./e for o,e in zip(observed_values,expected_values)])
chi_square_statistic=chi_square[0]+chi_square[1]
print("chi_square_statistic:",chi_square_statistic)
critical_value=chi2.ppf(q=1-alpha,df=ddof)
print('critical_value:',critical_value)
p_value=1-chi2.cdf(x=chi_square_statistic,df=ddof)
print('p-value:',p_value)
print('Significance level: ',alpha)
print('Degree of Freedom: ',ddof)
print('p-value:',p_value)
if chi_square_statistic>=critical_value:
    print("Reject H0,There is a relationship between 2 categorical variables")
else:
    print("Retain H0,There is no relationship between 2 categorical variables")
if p_value<=alpha:
    print("Reject H0,There is a relationship between 2 categorical variables")
else:
    print("Retain H0,There is no relationship between 2 categorical variables")
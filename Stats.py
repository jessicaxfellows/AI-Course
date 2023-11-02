import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import ttest_ind
import statsmodels.api as sm
import warnings 

# load the dataset
dataset = pd.read_csv("C://Users//jessi//OneDrive//Documents//GitHub//AI-Course//dataset.csv")

# data analysis
num_rows, num_cols = dataset.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

# descriptive stats
summary_stats = dataset.describe()
print("Descriptive Statistics:")
print(summary_stats)

# probability calculation
if len(dataset) >= 8:
    prob = norm.cdf(2.5, loc=dataset['column_1'].mean(), scale=dataset['column_1'].std())
    print(f'Probability: {prob}')
else:
    print("Insufficient data for probability calculation.")

# hypothesis testing 
warnings.filterwarnings("ignore") # ignore the warning for the small sample size
group_a_data = dataset[dataset['group'] == 'A']['column_2']
group_b_data = dataset[dataset['group'] == 'B']['column_2']
if len(group_a_data) >= 8 and len(group_b_data) >= 8:
    t_stat, p_value = ttest_ind(group_a_data, group_b_data)
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")
else:
    print("Insufficient data for hypothesis testing.")

# correlation analysis
numeric_columns = dataset.select_dtypes(include=[np.number]).columns
corr_matrix = dataset[numeric_columns].corr()
print("Correlation Matrix:")
print(corr_matrix)

# regression analysis
if len(dataset) >= 8:
    x = dataset[['column_1', 'column_2', 'feature_1', 'feature_2']]
    y = dataset['target']
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    print(model.summary())
else:
    print("Insufficient data for the regression analysis.")
import pandas as pd

# load the dataset
df = pd.read_csv("C:/Users/jessi/OneDrive/Documents/GitHub/AI-Course/example_dataset.csv")

# perform data preprocessing and feature engineering steps 
df.fillna(df.mean(), inplace=True) # fill missing values with mean
df['interaction_feature_example'] = df['feature_1'] * df['feature_2'] #interaction feature

# save the preprocessed dataset
df.to_csv("preprocessed_dataset.csv", index=False)
print(df['interaction_feature_example'])
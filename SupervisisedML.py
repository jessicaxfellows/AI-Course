import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# load the dataset
df = pd.read_csv("C:/Users/jessi/OneDrive/Documents/GitHub/AI-Course/exampledataset1.csv")

# split the dataset into features (x) and target (y)
X = df.drop("Target", axis=1)
y = df["Target"]

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the logistic regression model
model = LogisticRegression(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the testing set
predictions = model.predict(X_test)

# Evaluate the model's performance and print accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
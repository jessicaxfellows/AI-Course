# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the dataset
file_path = 'C:/Users/jessi/OneDrive/Documents/GitHub/AI-Course/exampledataset2.csv'
df = pd.read_csv(file_path)

# Select columns for sentiment analysis
text_column = 'text'  # Replace 'text' with the actual column name containing text data
sentiment_column = 'sentiment'  # Replace 'sentiment' with the actual column name containing sentiment labels

# Split the dataset into features (X) and target (y)
X = df[text_column]
y = df[sentiment_column]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Initialize the SVM classifier
svm_classifier = SVC()

# Train the model
svm_classifier.fit(X_train_vectorized, y_train)

# Make predictions on the testing set
predictions = svm_classifier.predict(X_test_vectorized)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, predictions)

# Print the accuracy of the model
print("Accuracy:", accuracy)

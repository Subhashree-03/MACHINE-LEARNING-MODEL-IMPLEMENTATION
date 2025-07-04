# spam_email_detection.ipynb

 Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

 Load Dataset
df = pd.read_csv("spam.csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']
print(df.head())

Data Preprocessing
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})
X = df['message']
y = df['label_num']

 Text Vectorization
cv = CountVectorizer()
X_cv = cv.fit_transform(X)

 Split Dataset
X_train, X_test, y_train, y_test = train_test_split(X_cv, y, test_size=0.2, random_state=42)

 Train Model
model = MultinomialNB()
model.fit(X_train, y_train)

 Predictions and Evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Step 8: Predict on new data
sample_msg = ["Congratulations! You've won a free ticket to Dubai!"]
sample_vector = cv.transform(sample_msg)
print("Prediction:", model.predict(sample_vector))  # 1 = spam, 0 = ham

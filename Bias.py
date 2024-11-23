# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score,precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the iris dataset
from sklearn.datasets import load_iris
iris = load_iris()


# Convert the dataset into a DataFrame
df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                  columns=iris['feature_names']+['target'])
df['target'] = df['target'].astype(int)
df

df.info()

# Remove duplicates
df.drop_duplicates(inplace=True)


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[iris['feature_names']],df ['target'], test_size= 0.4, random_state=0)


# Fit a Random Forest Classifier model
model = RandomForestClassifier()
model.fit(X_train, y_train)




# Calculate Bias and Variance
train_error = 1 - model.score(X_train, y_train)
test_error = 1 - model.score(X_test, y_test)
bias = np.mean([train_error, test_error])
variance = model.score(X_test, y_test) - train_error

print("Bias: {:.2f}".format(bias))
print("Variance: {:.2f}".format(variance))

# Cross-validation
cv_scores = cross_val_score(model, df[iris['feature_names']], df['target'], cv=5)
print("\nCross-validation scores: ", cv_scores)
print("Mean CV Accuracy: {:.2f}".format(np.mean(cv_scores)))


# Confusion matrix
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 3))
sns.heatmap(cm, annot=True, cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Accuracy, Precision, and Recall
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
print("\nAccuracy: {:.2f}".format(accuracy))
print("Precision: {:.2f}".format(precision))
print("Recall: {:.2f}".format(recall))

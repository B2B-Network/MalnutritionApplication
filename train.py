import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib
 
 
# Load the dataset
data = pd.read_csv('dataset.csv')
 
# Split the dataset into features and labels
X = data.drop('result', axis=1)  # Features
y = data['result']  # Labels
 
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
 
# Train logistic regression model
logreg = LogisticRegression()
logreg.fit(X_train_scaled, y_train)
 
# Save the model to a file
joblib.dump(logreg, 'model.pkl')
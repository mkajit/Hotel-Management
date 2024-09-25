import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
df = pd.read_csv('creditcard.csv')

# Split the dataset into features and target
X = df.drop('Class', axis=1)
y = df['Class']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a random forest classifier
rfc = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rfc.fit(X_train, y_train)

# Function to get user input
def get_user_input():
    time = float(input("Enter the time of the transaction: "))
    v1 = float(input("Enter the V1 feature: "))
    v2 = float(input("Enter the V2 feature: "))
    ...
    v28 = float(input("Enter the V28 feature: "))
    amount = float(input("Enter the amount of the transaction: "))
    return [time, v1, v2, ..., v28, amount]

# Function to predict fraud
def predict_fraud(user_input):
    prediction = rfc.predict([user_input])
    if prediction[0] == 0:
        return "Transaction is not fraudulent"
    else:
        return "Transaction is fraudulent"

# Get user input
user_input = get_user_input()

# Predict fraud
result = predict_fraud(user_input)

# Print the result
print(result)
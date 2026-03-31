import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset
data = {
    'length': [20, 60, 75, 30, 90],
    'dots': [2, 5, 6, 3, 7],
    'https': [1, 0, 0, 1, 0],
    'label': [0, 1, 1, 0, 1]  # 0 = Safe, 1 = Phishing
}

df = pd.DataFrame(data)

X = df[['length', 'dots', 'https']]
y = df['label']

model = LogisticRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))
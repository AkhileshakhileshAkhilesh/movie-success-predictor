import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("movie_data.csv")

# Preprocess
df = pd.get_dummies(df, columns=['Genre'])  # One-hot encode Genre
X = df.drop(['Movie Name', 'Hit/Flop'], axis=1)
y = df['Hit/Flop'].map({'Hit': 1, 'Flop': 0})

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Make a prediction
new_movie = pd.DataFrame([{
    'Budget (in Cr)': 85,
    'Duration (mins)': 135,
    'Star Power (1-5)': 5,
    'Genre_Action': 1,
    'Genre_Comedy': 0,
    'Genre_Drama': 0,
    'Genre_Romance': 0
}])

prediction = model.predict(new_movie)
print("Prediction for new movie:", "Hit" if prediction[0] == 1 else "Flop")

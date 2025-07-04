# 🎬 Movie Success Predictor 🎯

This project is a simple and beginner-friendly **Machine Learning model** that predicts whether a movie will be a **Hit or Flop** based on various factors like budget, duration, genre, and star power.

---

## 🚀 Objective

To build a classification model using **Random Forest** that helps predict the success of a movie based on past movie data.

---

## 📁 Features Used

- 🎯 Budget (in Crores)
- ⏱ Duration (in Minutes)
- 🎭 Genre (Action, Drama, Comedy, Romance)
- 🌟 Star Power (1–5)

---

## 🛠 Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Visual Studio Code

---

## ⚙ How It Works

1. The dataset is loaded and preprocessed
2. Categorical variables (genre) are one-hot encoded
3. A Random Forest model is trained
4. Accuracy is evaluated using test data
5. The model predicts whether a new movie will be a Hit or Flop

---

## 📊 Sample Input

```python
new_movie = pd.DataFrame([{
    'Budget (in Cr)': 85,
    'Duration (mins)': 135,
    'Star Power (1-5)': 5,
    'Genre_Action': 1,
    'Genre_Comedy': 0,
    'Genre_Drama': 0,
    'Genre_Romance': 0
}])

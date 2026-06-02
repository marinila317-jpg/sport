import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Приклад даних (заміни на реальні з API)
data = {
    'home_team_goals_avg': [1.5, 2.0, 1.2],
    'away_team_goals_avg': [1.0, 1.5, 0.8],
    'home_wins_last_5': [3, 4, 2],
    'away_wins_last_5': [2, 1, 3],
    'result': ['W', 'D', 'L']  # W - home win, D - draw, L - home loss
}

df = pd.DataFrame(data)

X = df.drop('result', axis=1)
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, predictions))

# TODO: Додати реальний API для даних, наприклад API-Football
print('Модель готова для прогнозів. Додай дані!')
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Dummy data - в реальності заміни на завантаження з API
# Для прикладу

data = {
    'home_team_goals_avg': [1.5, 2.0, 1.2, 1.8, 2.3],
    'away_team_goals_avg': [1.0, 1.5, 0.8, 1.2, 1.6],
    'home_wins_last_5': [3, 4, 2, 3, 5],
    'away_wins_last_5': [2, 1, 3, 2, 1],
    'home_draws_last_5': [1, 0, 2, 1, 0],
    'result': ['W', 'D', 'L', 'W', 'W']  # W - home win, D - draw, L - home loss
}

df = pd.DataFrame(data)

X = df.drop('result', axis=1)
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

# Збереження моделі
joblib.dump(model, 'football_model.pkl')
print('Модель збережена в football_model.pkl')

print('\n=== TODO ===')
print('1. Підключити API-Football або Football-Data.org')
print('2. Додати Poisson для голів')
print('3. Feature engineering: H2H, форма, травми')
print('4. Backtesting на реальних даних')
print('5. Pipeline з cross-validation')

# TODO: Реальний прогноз
function
print('Готовий до покращення, лохи не чекають!')
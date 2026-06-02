# Sport Football Predictor

## Опис

Проєкт для прогнозування результатів футбольних матчів за допомогою Machine Learning. Використовує історичні дані команд, форму, H2H тощо.

**Мета:** Допомогти аналізувати матчі та робити обґрунтовані ставки (для навчання, не для азарту!).

## Як запустити

1. `git clone https://github.com/marinila317-jpg/sport.git`
2. `pip install -r requirements.txt`
3. `python football_predictor.py`

## Структура
- `src/` — основний код
- `data/` — дані (gitignore)
- `notebooks/` — Jupyter для експериментів

## Покращення (TODO)
- Реальний API-Football
- Poisson distribution для голів
- Backtesting ставок
- Feature engineering

**Попередження:** Прогнози — це не гарантія. Азарт руйнує гаманці швидше за будь-яку модель.

## Результати
Поки що dummy-модель. Тестова точність ~33% на трьох рядках (бо даних нихуя).
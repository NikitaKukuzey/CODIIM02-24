import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('project_codiim/result.csv')

# Изменение целевой переменной на 'Убийства'
X = df[['Год', 'Осуждено', 'МВД', 'Полиция']]
y = df['Убийства']  # Изменение целевой переменной

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказания для будущих годов
future_years = [2020, 2021, 2022, 2023, 2024, 2025]
future_data = pd.DataFrame({
    'Год': future_years,
    'Осуждено': [df['Осуждено'].mean()] * len(future_years),
    'МВД': [df['МВД'].mean()] * len(future_years),
    'Полиция': [df['Полиция'].mean()] * len(future_years)
})

predictions = model.predict(future_data[['Год', 'Осуждено', 'МВД', 'Полиция']])

# Вывод предсказаний для будущих годов
future_predictions = pd.DataFrame({
    'Год': future_years,
    'Предсказанные Убийства': predictions
})

future_predictions['Предсказанные Убийства'] = future_predictions['Предсказанные Убийства'].astype('int64')



# Загрузка данных
df = pd.read_csv('project_codiim/result.csv')

# Группируем данные для построения столбчатой диаграммы
bar_positions = df['Год']
bar_width = 0.35

# Столбец с количеством осужденных
plt.bar(bar_positions, df['Осуждено'], width=bar_width, label='Закрыто дел', color='pink')

# Столбец с количеством убийств
plt.bar(bar_positions, df['Убийства']-df['Осуждено'], width=bar_width, label='Убийства', color='black', bottom=df['Осуждено'])

# Столбец с количеством полиции (в сотнях)
plt.bar([pos + bar_width for pos in bar_positions], df['Полиция'], width=bar_width, label='Полиция', color='blue')

# Столбец с предсказанным количеством убийств
plt.bar(future_predictions['Год'], future_predictions['Предсказанные Убийства'], width=bar_width, label='Предсказанные Убийства', color='red')

plt.xlabel('Год')
plt.ylabel('Количество')
plt.title('Столбчатая диаграмма закрытых дел, убийств, полиции и предсказанных убийств по годам')
plt.legend()
plt.show()




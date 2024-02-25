import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

df = pd.read_csv('project_codiim/result.csv')

X = df[['Год', 'Осуждено', 'МВД', 'Полиция']]
y = df['Убийства']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)



future_years = [2020, 2021, 2022, 2023, 2024, 2025]
future_data = pd.DataFrame({
    'Год': future_years,
    'Осуждено': [df['Осуждено'].mean()] * len(future_years),
    'МВД': [df['МВД'].mean()] * len(future_years),  
    'Полиция': [df['Полиция'].mean()] * len(future_years)
})

# Предсказания для будущих годов
future_predictions = model.predict(future_data[['Год', 'Осуждено', 'МВД', 'Полиция']])

# Создание DataFrame с предсказанными значениями
result_df = pd.DataFrame({
    'Год': future_years,
    'Предсказанные Убийства': future_predictions
})
result_df['Предсказанные Убийства'] = result_df['Предсказанные Убийства'].astype('int64')

print(result_df)



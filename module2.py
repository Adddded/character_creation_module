# Из модуля module1.py импортируем функцию special_calculation.
from module1 import special_calculation
from main import attack

print("Основной модуль")
# Производим расчёты. 
coef = special_calculation(2, 5)
print(coef) 
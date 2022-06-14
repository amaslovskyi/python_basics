"""
Задание 5.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""
gain = int(input("Введи выручку фирмы: "))
cost = int(input("Введи издержки фирмы: "))

if gain > cost:
    income = gain - cost
    ros = income / gain * 100
    print(f"Твоя фирма работает с прибылью, рентабельность выручки {ros:.2f}%")
    mem = int(input("Введите количество сотрудников: "))
    p_cost = income / mem
    print("Прибыль фирмы в расчете на одного сотрудника", round(p_cost, 2))
else:
    print("Фирма работает в убыток")
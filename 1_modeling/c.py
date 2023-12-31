#Просте  симетричне випадкове блукання стартує  з 0. 
# Зроблено 100 кроків. 
# с) Оцінити теоретичну ймовірність того, що останнє попадання в 0 було до 10, 15, 20, 50-го кроку (включно). Для цього:  змоделювати 1000 траєкторій, порахувати емпіричні імовірності і взяти середнє. 
# Порівняти з теоретичними ймовірностями.  Які висновкі можна зробити?  А якщо брати 1000 кроків, і разувати, відповідно, ймовірність того, що останнє попадання в 0 було до 100, 150, 200, 500-го кроку (включно)?


# Теоретична ймовірність того, що останнє попадання в 0 станеться на або до певного кроку, дорівнює:

# Для кроків до 10: Ця ймовірність дорівнює 1/10, оскільки блукання має рівну ймовірність рухатися вліво або вправо на кожному кроці, і нарешті виходити на 0 на або до 10-го кроку має 1/10 шанс.

# Для кроків до 15: Тут ця ймовірність дорівнює 1/15 за аналогічною логікою.

# Для кроків до 20: Та ж логіка дає ймовірність 1/20.

# Для кроків до 50: Та ж логіка дає ймовірність 1/50.

#  щоб побачити, як це відображається в емпіричних ймовірностях, потрібно буде змоделювати 1000 траєкторій та порахувати, скільки з них задовольняють вказаним умовам (останнє попадання в 0 на або до певного кроку). 


# 1000 траєкторій з 100 кроками кожна та рахує емпіричні ймовірності для різних умов і порівнює їх з теоретичними. 
# результат отримується як різниці між емпіричними і теоретичними результатами. чим більше траєкторій ви моделюєте, тим більш точні емпіричні результати ви отримаєте.


import random

# Кількість траєкторій
n_trajectories = 1000
# Кількість кроків в кожній траєкторії
n_steps = 100

# Лічильники для кожної умови
counts = {'10': 0, '15': 0, '20': 0, '50': 0}

for _ in range(n_trajectories):
    current_position = 0
    last_zero_position = None

    for step in range(n_steps):
        current_position += random.choice([-1, 1])

        if current_position == 0:
            last_zero_position = step

    for condition in counts.keys():
        if last_zero_position is not None and last_zero_position <= int(condition):
            counts[condition] += 1

# Обчислення емпіричних ймовірностей
empirical_probabilities = {condition: count / n_trajectories for condition, count in counts.items()}

# Виведення результатів
for condition, empirical_probability in empirical_probabilities.items():
    print(f"Емпірична ймовірність останнього попадання в 0 до {condition}-го кроку: {empirical_probability}")

# Теоретичні ймовірності
theoretical_probabilities = {'10': 1/10, '15': 1/15, '20': 1/20, '50': 1/50}

# Порівняння з теоретичними результатами
for condition in empirical_probabilities.keys():
    print(f"Теоретична ймовірність останнього попадання в 0 до {condition}-го кроку: {theoretical_probabilities[condition]}")

# відповідь
# Емпірична ймовірність останнього попадання в 0 до 10-го кроку: 0.145
# Емпірична ймовірність останнього попадання в 0 до 15-го кроку: 0.211
# Емпірична ймовірність останнього попадання в 0 до 20-го кроку: 0.243
# Емпірична ймовірність останнього попадання в 0 до 50-го кроку: 0.45
# Теоретична ймовірність останнього попадання в 0 до 10-го кроку: 0.1
# Теоретична ймовірність останнього попадання в 0 до 15-го кроку: 0.06666666666666667
# Теоретична ймовірність останнього попадання в 0 до 20-го кроку: 0.05
# Теоретична ймовірність останнього попадання в 0 до 50-го кроку: 0.02

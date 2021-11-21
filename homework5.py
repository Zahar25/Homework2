#5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для роботи захардкодити свій.
dictionary = {1:'who', 2: 'is', 3: 'who', 4: 'that', 5: 'that', 6:'?'}
temp = []
result = dict()
for key, value in dictionary.items():
    if value not in temp:
        temp.append(value)
        result [key] = value
print(result)

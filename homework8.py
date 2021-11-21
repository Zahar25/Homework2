#8.Написати скрипт, який отримує від користувача позитивне ціле число і створює словник, з ключами від 0 до введеного числа, а значення для цих ключів - це квадрат ключа.
number = int(input("Write a number: "))
dict = dict()
for value in range(0, number+1):
    dict[value]=value*value
print (dict)

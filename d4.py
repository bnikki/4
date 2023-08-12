# 1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран. (використовувати цикл) command = input("Enter a string of letters and numbers:")
usercommand = input("Enter a string of letters and numbers:")
UserDisplay = {'Special symbols': 0, 'Letters': 0, 'Numbers': 0}
for i in usercommand:
    if i.isalpha():
        UserDisplay['Letters'] += 1
    elif i.isdigit():
        UserDisplay['Numbers'] += 1
    else:
        UserDisplay['Special symbols'] += 1

print (UserDisplay)

# 2. Користувач вводить з клавіатури рядок та символ для пошуку. Порахуйте скільки разів у рядку зустрічається потрібний символ. Отримане число виведіть на екран.
string = input("Enter a string: ")

symbol = input("Enter a character to search for: ")

count = 0

for c in string:

 if c == symbol:

  count += 1

print(f"The character '{symbol}' appears {count} times in the string.")

# 3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни. Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.
string = input("Enter the string:")
word = input("Enter a search term:")
replacementword = input("Enter a replacement word:")
string = string.replace(word, replacementword)
print(string)

# 4. Дано рядок. (зробити зрізи)
sentence = "The world is an amazing place"
# - Спершу виведіть третій символ цього рядка.
print(sentence[2:4:5])
# - У другому рядку виведіть передостанній символ цього рядка.
print(sentence[27:28])
# - У третьому рядку виведіть перші п'ять символів цього рядка.
print(sentence[:5])
# - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
print(sentence[:-2])
# - У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться з першого).
print(sentence[::2])
# - У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
print(sentence[1::2])
# - У сьомому рядку виведіть усі символи у зворотному порядку.
print(sentence[::-1])
# - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
print(sentence[::-2])
# - У дев'ятому рядку виведіть довжину цього рядка.
print(len(sentence))

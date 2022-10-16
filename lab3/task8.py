money_capital = 10000 # финансовая подушка безопасности
salary = 5000 # зарплата в месяц
spend = 6000 # расходы на проживаение
increase = 0.05 # рост цен

month = 1  # количество месяцев, которое можно прожить
all_money = money_capital + salary

while all_money >= spend:
    month += 1
    if increase == 0.05:
        increase = 0.05
    else:
        increase = increase + 0.05
    spend = spend + (1 * increase)
    all_money = all_money - spend

print(month)

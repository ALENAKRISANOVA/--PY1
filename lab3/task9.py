salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

total = 0
i = 1 # начинаем считать с первого месяца по порядку
while months != 0:
        spend *= 1 + increase * (i - 1)
        i = 2
        while need_money + salary < round(spend):
                need_money += 1
        total += need_money
        months -= 1

print(round(total))


salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
total_spend = spend
for i in range (2, 11):
    spend = spend + spend * increase
    total_spend += spend
need_money = -(salary * months - total_spend)
print(round(need_money))

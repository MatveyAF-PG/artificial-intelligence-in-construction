money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
spend_month = spend
while money_capital > spend_month:
    for i in range(month):
        if i > 0:
            spend_month = spend_month + spend_month * increase
            money_capital = (money_capital + salary) - spend
    if money_capital > 0:
        month += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", month)


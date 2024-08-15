"""Функция вычисления сложных процентов"""


def compound(amount, year_percent, months):
    month_percent = year_percent / 12
    for i in range(months):
        inc = amount / 100 * month_percent
        amount += inc
    return amount


print(compound(100000, 10, 12))

"""Функция вычисления сложных процентов"""


def compound2(amount, year_percent, months):
    month_percent = year_percent / 12
    return amount * (1 + month_percent / 100) ** months


print(compound2(100000, 10, 12))

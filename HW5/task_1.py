# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict
from statistics import mean
from random import uniform

companies = defaultdict(list)

companies_count = input('Enter companies count or press enter to load predefined: ')
if companies_count:
    for _ in range(int(companies_count)):
        name = input('Enter company name: ')
        income = list(map(float, input('Enter company income for each quarter (space as delimiter): ').split()))
        companies[name] = income
else:
    names = ['Tet Corp.', 'Beauty and the Beast LLC', 'Housewife Inc.', 'Midnight Sorcerer PLC', 'OMG!!!',
             'MasterMind']
    for name in names:
        companies[name] = [round(uniform(50000, 500000), 2) for _ in range(4)]

mean_year_income = mean(map(sum, companies.values()))
print(f'Companies that earned LESS than the avg. for the year:')
print(*[f'  - {name}' for name, income in companies.items() if sum(income) < mean_year_income], sep='\n')

print(f'Companies that earned MORE than the avg. for the year:')
print(*[f'  - {name}' for name, income in companies.items() if sum(income) > mean_year_income], sep='\n')

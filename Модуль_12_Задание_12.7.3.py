per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
banki = [] #список_процентных_ставок
for key in per_cent.keys():
    banki.append(per_cent[key])     #значения_ставок
money = int(input('Введите размер депозита: '))    #размер_депозита
deposit = list([i * (money / 100) for i in banki])
deposit = list([round(i, 2) for i in deposit])
print('Размер процентов в разных банках составит -', ", ".join(map(str, deposit)))    #вывод_накоплений в разных_банках_за год
print('Максимальная сумма, которую вы можете заработать -', max(deposit))    #вывод_максимальной_суммы_процентов_за_год
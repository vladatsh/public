#количество билетов на конференцию
tickets = int(input('Введите количество билетов: '))
#возраст посетителей - список
member = []
#запрашиваем возраст каждого посетителя
for i in range(0, tickets):
    age = int(input(f'Введите возраст посетителя №{i + 1}:\n'))
    #заполняем ранее созданный список данными
    member.append(age)
    #устанавливаем прайс, включая льготы
    def priсe(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390
#суммируем стоимость билетов
fullpriсe = sum(map(priсe, member))
#даем скидку 10% для посетителей в группе от трех человек
if tickets > 3:
    fullpriсe = int(fullpriсe * 0.9)
#конечный итог
print('Итоговая стоимость:', fullpriсe, 'руб.')
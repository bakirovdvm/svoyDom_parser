import openpyxl
import json
import datetime

# print(datetime.date.today())


with open('result_zhana_urpaq.json') as file:
    data = json.load(file)
#
# for item in data:
#     apt_number = item['Номер квартиры:']
#     rooms_quality = item['Количество комнат:']
#     apt_S = item['Площадь:']
#     price_sq_m = item['Цена за квм:']
#     price_total = item['Цена общая:']
#     floor = item['Этаж:']
#     entrance = item['Подъезд:']
#     print(apt_number, rooms_quality, apt_S, price_sq_m, price_total, floor, entrance)

book = openpyxl.Workbook()
sheet = book.active

sheet['A3'] = 'APT_NUMBER'
sheet['B3'] = 'ROOMS_Q'
sheet['C3'] = 'APT_S'
sheet['D3'] = 'FLOOR'
sheet['E3'] = 'ENTRANCE'
sheet['G3'] = 'DATE'
sheet['H3'] = 'PRICE_SQ_M'
sheet['I3'] = 'PRICE_TOTAL'

row = 4
for item in data:
    sheet[row][0].value = item['Номер квартиры:']
    sheet[row][1].value = item['Количество комнат:']
    sheet[row][2].value = item['Площадь:']
    sheet[row][3].value = item['Этаж:']
    sheet[row][4].value = item['Подъезд:']
    sheet[row][6].value = datetime.date.today()
    sheet[row][7].value = item['Цена за квм:']
    sheet[row][8].value = item['Цена общая:']
    # print(apt_number, rooms_quality, apt_S, price_sq_m, price_total, floor, entrance)
    row += 1


book.save('my_book.xlsx')
book.close()


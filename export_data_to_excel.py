# import openpyxl
# import json
# import datetime
#
# # print(datetime.date.today())
#
#
# with open('result_zhana_urpaq.json') as file:
#     data = json.load(file)
# #
# # for item in data:
# #     apt_number = item['Номер квартиры:']
# #     rooms_quality = item['Количество комнат:']
# #     apt_S = item['Площадь:']
# #     price_sq_m = item['Цена за квм:']
# #     price_total = item['Цена общая:']
# #     floor = item['Этаж:']
# #     entrance = item['Подъезд:']
# #     print(apt_number, rooms_quality, apt_S, price_sq_m, price_total, floor, entrance)
#
# book = openpyxl.Workbook()
# sheet = book.active
#
# sheet['A3'] = 'APT_NUMBER'
# sheet['B3'] = 'ROOMS_Q'
# sheet['C3'] = 'APT_S'
# sheet['D3'] = 'FLOOR'
# sheet['E3'] = 'ENTRANCE'
# sheet['G3'] = 'DATE'
# sheet['H3'] = 'PRICE_SQ_M'
# sheet['I3'] = 'PRICE_TOTAL'
#
# row = 4
# for item in data:
#     sheet[row][0].value = item['Номер квартиры:']
#     sheet[row][1].value = item['Количество комнат:']
#     sheet[row][2].value = item['Площадь:']
#     sheet[row][3].value = item['Этаж:']
#     sheet[row][4].value = item['Подъезд:']
#     sheet[row][6].value = datetime.date.today()
#     if sheet[row][7]:
#         sheet[row][7].value = item['Цена за квм:']
#         # sheet[row][8].value = item['Цена общая:']
#         sheet[row][8].value = int(item['Цена за квм:'].replace(' ', '')) * float(item['Площадь:'])
#     # print(apt_number, rooms_quality, apt_S, price_sq_m, price_total, floor, entrance)
#     else:
#         sheet[row][7].value = item['Цена за квм:']
#         sheet[row][8].value = item['Цена общая:']
#     row += 1
#
#
# book.save('my_book.xlsx')
# book.close()
#
# print('done')



####### NEED TO STUDY CODE ############## NEED TO STUDY CODE ############## NEED TO STUDY CODE ############## NEED TO STUDY CODE
# https://stackoverflow.com/questions/67880607/how-to-update-existing-excel-xlsx-file-using-openpyxl
# import arcpy
# import openpyxl as px
#
# def main():
#     wb = px.load_workbook(r"C:\Users\Hp\Desktop\Ejemplo\VINCULACION_S.xlsx")
#     ws = wb['VINCULACION_SH_NUE']
#     in_features = r"C:\Users\Hp\Desktop\Ejemplo\VH_Dissolve.shp"
#
#     row_num = 3
#     with arcpy.da.SearchCursor(
#         in_features,
#         ["COLOR", "INTERNO_DE", "CLASE_DEMA", "COUNT_AREA", "SUM_AREA", "SUM_LENGTH"],
#     ) as cursor:
#         for row in cursor:
#             ws.cell(row=row_num, column=2).value = row[0]
#             ws.cell(row=row_num, column=3).value = row[1]
#             ws.cell(row=row_num, column=4).value = row[2]
#             ws.cell(row=row_num, column=6).value = row[3]
#             ws.cell(row=row_num, column=7).value = row[4]
#             ws.cell(row=row_num, column=8).value = row[5]
#             row_num += 1
#     wb.save(r"C:\Users\Hp\Desktop\Ejemplo\VINCULACION_S.xlsx")
#
#
# if __name__ == "__main__":
#     main()
####### NEED TO STUDY CODE ############## NEED TO STUDY CODE ############## NEED TO STUDY CODE ############## NEED TO STUDY CODE




import openpyxl
import json
import datetime

# print(datetime.date.today())
def main():

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


    book = openpyxl.load_workbook(r'my_new_book.xlsx')

    sheet = book.active

    sheet['A3'] = 'APT_NUMBER'
    sheet['B3'] = 'ROOMS_Q'
    sheet['C3'] = 'APT_S'
    sheet['D3'] = 'FLOOR'
    sheet['E3'] = 'ENTRANCE'
    sheet['G3'] = 'DATE'
    sheet['H3'] = 'PRICE_SQ_M'
    sheet['I3'] = 'PRICE_TOTAL'

    # row = 4
    # for item in data:
    #     sheet[row][0].value = item['Номер квартиры:']
    #     sheet[row][1].value = item['Количество комнат:']
    #     sheet[row][2].value = item['Площадь:']
    #     sheet[row][3].value = item['Этаж:']
    #     sheet[row][4].value = item['Подъезд:']
    #     sheet[row][6].value = datetime.date.today()
    #     if sheet[row][7]:
    #         sheet[row][7].value = item['Цена за квм:']
    #         # sheet[row][8].value = item['Цена общая:']
    #         sheet[row][8].value = int(item['Цена за квм:'].replace(' ', '')) * float(item['Площадь:'])
    #     # print(apt_number, rooms_quality, apt_S, price_sq_m, price_total, floor, entrance)
    #     else:
    #         sheet[row][7].value = item['Цена за квм:']
    #         sheet[row][8].value = item['Цена общая:']
    #     row += 1

    book.save(r'my_new_book.xlsx')
    book.close()
    # book.save('my_book.xlsx')
    # book.close()
    #
    print('done')

if __name__ == "__main__":
    main()
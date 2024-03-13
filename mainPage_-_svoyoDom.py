# import requests
# from bs4 import BeautifulSoup
#
# # url = 'https://svoydom.kz/project/1/1061833/?objview=list&PAGEN_1=1&bxajaxid=ed9cca27dcf034d99c8046454bd163c2'
#
# last_page_pagination = 13
# for i in range(1, last_page_pagination + 1):
#     # print(i)
#     url = f'https://svoydom.kz/project/1/1061833/?objview=list&PAGEN_1={i}&bxajaxid=ed9cca27dcf034d99c8046454bd163c2'
#
# # url = 'https://svoydom.kz/project/1/1061833/?objview=list&PAGEN_1=2&bxajaxid=ed9cca27dcf034d99c8046454bd163c2'
# # url = 'https://svoydom.kz/project/1/1061833/'
#     page = requests.get(url)
#     # print('pageStatus:', page.status_code)
#
#     allInfo = list()
#     filterInfo = list()
#     remove_data = list()
#     resultInfo = list()
#     paginateLimit = int()
#     soup = BeautifulSoup(page.text, "html.parser")
#
#
#     # ################################################
#     # paginateLimitInfo = soup.findAll(class_='bx-pagination-container')
#     # countt = 0
#     # # for i in paginateLimitInfo:
#     # #     for j in i:
#     # #         for k in j:
#     # #             countt += 1
#     # #             print(countt, k)
#     # #         # countt += 1
#     # #         # print(countt, j)
#     # #     break
#     # for i in paginateLimitInfo:
#     #
#     #     print(i)
#     #         # countt += 1
#     #         # print(countt, j)
#     #     break
#     ################################################
#
#     # print('paginateLimit'.upper(), paginateLimit)
#
#     allInfo = soup.findAll(class_='favorites-items')
#     for data in allInfo:
#         if data.find('ul', class_='favorite-info-list') is not None:
#             filterInfo.append(data.text)
#
#
#     for i in filterInfo:
#         # print(i)
#         # print(i.split('\n'))
#         remove_data += i.split('\n')
#
#     for i in remove_data:
#         if i:
#             resultInfo.append(i)
#
#     count = 0
#     for i in resultInfo:
#         count += 1
#
#         print(i, end=' ')
#         if count % 13 == 0:
#             print('')
#
#
#
# # {
# #     'apt_numb': 1,
# #     'info': {
# #         'rooms_q': 3,
# #         'S': 91.11,
# #         'price_full': 31068510,
# #         'price_by_one_sqM': 341,
# #
# #     }
# # }


result = dict()
data = [
    '1-комн, № 42 Площадь: 43.16 м ² Стоимость: 15 235 480 ₸ Цена, м2: 353 000 м ² Этаж:  1 Подъезд: 1 Блок: 1 ',
    '2-комн, № 3 Площадь: 60.5 м ² Стоимость: 20 933 000 ₸ Цена, м2: 346 000 м ² Этаж:  1 Подъезд: 1 Блок: 1 ',
    '1-комн, № 2 Площадь: 37.2 м ² Стоимость: 13 726 800 ₸ Цена, м2: 369 000 м ² Этаж:  1 Подъезд: 1 Блок: 1'
]

for item in data:
    # apt_numb_ind = item.rfind('№')
    apt_numb_ind = str()
    # print(item[apt_numb])

    for j in range(item.find('№') + 2, item.find('№') + 5):
        if item[j] != ' ':
            apt_numb_ind += item[j]
            print(item[j], item[j], item)

        else:
            break

    result[apt_numb_ind] = item

for i in result:
    print(i, result[i])
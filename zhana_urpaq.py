import requests
from bs4 import BeautifulSoup
import os
import json


resulst_list = list()
last_page_pagination = 11
for i in range(1, last_page_pagination + 1):
    # url = f'https://svoydom.kz/project/1/1061833/?objview=list&PAGEN_1={i}&bxajaxid=ed9cca27dcf034d99c8046454bd163c2'
    # url = f'https://svoydom.kz/project/1/1061833/?PAGEN_2={i}&bxajaxid=ad9ace59831b5e8d9f86e087d95a772c'
    url = f'https://svoydom.kz/project/1/1067998/?PAGEN_2={i}&bxajaxid=ad9ace59831b5e8d9f86e087d95a772c'

    page = requests.get(url)
    # print('pageStatus:', page.status_code)

    allInfo = list()
    filterInfo = list()
    remove_data = list()
    resultInfo = list()
    paginateLimit = int()
    soup = BeautifulSoup(page.text, "html.parser")

    # ################################################
    # paginateLimitInfo = soup.findAll(class_='bx-pagination-container')
    # countt = 0
    # # for i in paginateLimitInfo:
    # #     for j in i:
    # #         for k in j:
    # #             countt += 1
    # #             print(countt, k)
    # #         # countt += 1
    # #         # print(countt, j)
    # #     break
    # for i in paginateLimitInfo:
    #
    #     print(i)
    #         # countt += 1
    #         # print(countt, j)
    #     break
    ################################################

    # print('paginateLimit'.upper(), paginateLimit)

    allInfo = soup.findAll(class_='favorites-items')
    for data in allInfo:
        if data.find('ul', class_='favorite-info-list') is not None:
            filterInfo.append(data.text)

    for i in filterInfo:
        remove_data += i.split('\n')

    for i in remove_data:
        if i:
            resultInfo.append(i)

    count = 0
    data_str = str()
    for i in resultInfo:
        count += 1
        data_str += i + ' '
        # print(i, end=' ')

        if count % 14 == 0:
            # print('')
            resulst_list.append(data_str)
            data_str = str()

print(resulst_list)

def collect_result_dict(data):
    result_dict = dict()
    for item in data:
        # apt_numb_ind = item.rfind('№')
        apt_numb_ind = str()

        for j in range(item.find('№') + 2, item.find('№') + 5):
            if item[j] != ' ':
                apt_numb_ind += item[j]
                # print(item[j], item[j], item)
            else:
                break

        result_dict[apt_numb_ind] = item

    return result_dict


result = collect_result_dict(resulst_list)
for item in result:
    print(item, result[item])
print('resulst_list', result)
print('Количество квартир в resulst_list', len(result))


#####################################################





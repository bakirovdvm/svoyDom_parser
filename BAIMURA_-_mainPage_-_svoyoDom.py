import os
import json
import requests
from bs4 import BeautifulSoup
# import collect_full_info_dict

print('URAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
resulst_list = list()
last_page_pagination = 5
for i in range(1, last_page_pagination + 1):
    # url = f'https://svoydom.kz/project/1/1061833/?PAGEN_2={i}&bxajaxid=ad9ace59831b5e8d9f86e087d95a772c'
    # url = 'https://svoydom.kz/project/flat/all/nazvanie_obekta_zhk-is-baimura/stoimost_pomeshcheniya_kvartiry_tenge-from-16630600-to-112179000/ploshchad_pomeshcheniya_kvartiry_m2-from-30-to-185/tsena_za_1_m2_tenge-from-336000-to-860000/etazh-from-1-to-12/apply/?PAGEN_1=2&bxajaxid=f8f26e29099fe0ef7724b58a2b3d2dd9'
    url = 'https://svoydom.kz/project/flat/all/nazvanie_obekta_zhk-is-baimura/stoimost_pomeshcheniya_kvartiry_tenge-from-16630600-to-112179000/ploshchad_pomeshcheniya_kvartiry_m2-from-30-to-185/tsena_za_1_m2_tenge-from-336000-to-860000/etazh-from-1-to-12/apply/?PAGEN_1={i_page}&bxajaxid=f8f26e29099fe0ef7724b58a2b3d2dd9'.format(i_page=i)
    page = requests.get(url)
    # print('pageStatus:', page.status_code)

    allInfo = list()
    filterInfo = list()
    remove_data = list()
    resultInfo = list()
    paginateLimit = int()
    soup = BeautifulSoup(page.text, "html.parser")


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

        if count % 13 == 0:
            # print('')
            resulst_list.append(data_str)
            data_str = str()

print('resulst_list_BAIMURA', type(resulst_list), resulst_list)
print()
print()
print()
for i in resulst_list:
    print(i)
print(len(resulst_list))

# result_for_print = collect_full_info_dict.make_json(resulst_list)
#
# for item in result_for_print:
#     print(item)





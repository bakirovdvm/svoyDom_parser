import os
import json
import requests
from bs4 import BeautifulSoup
# import collect_full_info_dict


resulst_list = list()
last_page_pagination = 24
for i in range(1, last_page_pagination + 1):
    # url = f'https://svoydom.kz/project/1/1783848/?PAGEN_2={i}&bxajaxid=8bdab43975fdf6665c4eff6c7bf719bd'
    url = f'https://svoydom.kz/project/1/2011396/?PAGEN_2={i}&bxajaxid=a57a1e6daa667df8be838cbb9853205d'

    page = requests.get(url)
    # print('pageStatus:', page.status_code)

    allInfo = list()
    filterInfo = list()
    remove_data = list()
    resultInfo = list()
    paginateLimit = int()
    soup = BeautifulSoup(page.text, "html.parser")

    # print('paginateLimit'.upper(), paginateLimit)

    allInfo = soup.findAll('div', class_='text-wrap')
    # print('allInfo'.upper(), allInfo)

    for data in allInfo:
        if data.find('span', class_='black') is not None:
            filterInfo.append(data.text)
    # print('filterInfo'.upper(), filterInfo)

    for i in filterInfo:
        # print('iiiii', i)
        remove_data += i.split('\n')

    # print('remove_data'.upper(), remove_data)

    for i in remove_data:
        if i:
            resultInfo.append(i)
    # print('resultInfo'.upper(), resultInfo)

    resultInfo_clean = list()
    for i in resultInfo:
        if i != ' 3D ':
            resultInfo_clean.append(i)

    count = 0
    data_str = str()
    for i in resultInfo_clean:
        count += 1
        data_str += i + ' '
        print(i, end=' ')

        if count % 13 == 0:
            print('')
            resulst_list.append(data_str)
            data_str = str()


print()
print('resulst_list', type(resulst_list), resulst_list)
print()

#
# file_name = 'resultList_-_DOMBYRA.json'
# path_for_file = os.path.join(file_name)
# with open(file_name, 'w') as f:
#     f.write(json.dumps(resulst_list))


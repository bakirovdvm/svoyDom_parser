import requests
from bs4 import BeautifulSoup
import json
import os


def make_json(project_name, last_page_pagination, url):

    '''
        :param project_name: название проекта
        :param last_page_pagination: количество страниц пагинации
        :param url: главная ссылка
        :return: в итоге будем возвращать готовый словарь со всеми квартирами,
                из словаря будем формировать EXCEL файл

        а на данном этапе получаем список квартир из ссылки
    '''


    print(f'project_name: {project_name}'
          f'\n\nPAGE: DOS_collectFullDataToDict.py - make_json')

    resulst_list = list()

    for i in range(1, last_page_pagination + 1):
        main_url = url.format(i_page=i)
        # url = 'https://svoydom.kz/project/flat/all/nazvanie_obekta_zhk-is-dos/apply/?PAGEN_1={i_page}&bxajaxid=f8f26e29099fe0ef7724b58a2b3d2dd9'.format(i_page=i)
        page = requests.get(main_url)
        # print('pageStatus:', page.status_code)

        allInfo = list()
        filterInfo = list()
        remove_data = list()
        resultInfo = list()
        paginateLimit = int()
        soup = BeautifulSoup(page.text, "html.parser")


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

    print(f'\nresulst_list_{project_name}', type(resulst_list), resulst_list)
    print()

    for i in resulst_list:
        print(i)
    print(len(resulst_list))


    #######################################################################################################
    '''
        Из списка будем получать словарь со всем квартирами
        затем из словаря будем формаировать Excel Файл
    '''

    result = list()


    for item in resulst_list:
        my_dict = dict()

        apt_numb_ind = str()
        for j in range(item.find('№') + 1, item.find('№') + 5):
            if item[j] != ' ':
                apt_numb_ind += item[j]
                # print(item[j], item[j], item)
            else:
                break

        print('Номер квартиры:', apt_numb_ind)

        '''
        Получаем количество комнат
        '''
        room_quantity = str()
        for room_q in range(item.rfind('-комн') - 1, item.rfind('-комн')):
            room_quantity = item[room_q]
        print('Количество комнат:', room_quantity)

        s_ploshad = str()
        for s in range(item.rfind('Площадь ') + 8, item.rfind('Площадь ') + 15):
            # print(item[s], end='')
            if item[s] != ' ':
                s_ploshad += item[s]
            else:
                break
        print('Площадь:', s_ploshad)

        price_kvm = str()
        for price in range(item.rfind('Цена, м2') + 9, item.rfind('м ²')):
            price_kvm += item[price]
        print('Цена за квм:', price_kvm)
        # print()
        # print('float(s_ploshad)', float(s_ploshad))
        # print()
        # print('Цена общая:', round(int(price_kvm.replace(' ', '')) * float(s_ploshad)))

        floor = str()
        for f in range(item.rfind('этаж') + 5, item.rfind('подъезд')):
            floor += item[f]
        print('Этаж:', floor)

        entrance = str()
        for e in range(item.rfind('подъезд') + 8, item.rfind('Блок')):
            # print(item[e], end=' ')
            entrance += item[e]
        print('Подъезд:', entrance)

        block = str()
        for b in range(item.rfind('Блок:') + 6, item.rfind('Блок') + 7):
            # print(item[e], end=' ')
            block += item[b]
        print('Блок:', block)
        print()

        my_dict['Номер квартиры:'] = apt_numb_ind
        my_dict['Количество комнат:'] = room_quantity
        my_dict['Площадь:'] = s_ploshad
        my_dict['Цена за квм:'] = price_kvm
        my_dict['Цена общая:'] = round(int(price_kvm.replace(' ', '')) * float(s_ploshad))
        my_dict['Этаж:'] = floor
        my_dict['Подъезд:'] = entrance
        my_dict['Блок:'] = block

        result.append(my_dict)

    file_name = f'{project_name}.json'
    path_for_file = os.path.join(file_name)
    with open(file_name, 'w') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    with open(file_name) as f:
        data = json.load(f)

        for item in data:
            print(item)

        print('Количество квартир:', len(data))

    return result


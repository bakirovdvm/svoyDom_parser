import os
import json
import requests
from bs4 import BeautifulSoup
import collect_full_info_dict


resulst_list = list()
last_page_pagination = 13
for i in range(1, last_page_pagination + 1):
    url = f'https://svoydom.kz/project/1/1061833/?PAGEN_2={i}&bxajaxid=ad9ace59831b5e8d9f86e087d95a772c'

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

print('resulst_list', type(resulst_list), resulst_list)

result_for_print = collect_full_info_dict.make_json(resulst_list)

for item in result_for_print:
    print(item)

######################################################


# resulst_list = {'244': '3-комн, № 244 Площадь: 91.11 м ² Стоимость: 31 068 510 ₸ Цена, м2: 341 000 м ² Этаж:  9 Подъезд: 4 Блок: 1 ', '241': '1-комн, № 241 Площадь: 35.24 м ² Стоимость: 13 778 840 ₸ Цена, м2: 391 000 м ² Этаж:  9 Подъезд: 4 Блок: 1 ', '239': '2-комн, № 239 Площадь: 60.61 м ² Стоимость: 21 577 160 ₸ Цена, м2: 356 000 м ² Этаж:  9 Подъезд: 4 Блок: 1 ', '238': '3-комн, № 238 Площадь: 91.11 м ² Стоимость: 32 435 160 ₸ Цена, м2: 356 000 м ² Этаж:  8 Подъезд: 4 Блок: 1 ', '235': '1-комн, № 235 Площадь: 35.24 м ² Стоимость: 14 483 640 ₸ Цена, м2: 411 000 м ² Этаж:  8 Подъезд: 4 Блок: 1 ', '234': '2-комн, № 234 Площадь: 70.97 м ² Стоимость: 24 910 470 ₸ Цена, м2: 351 000 м ² Этаж:  8 Подъезд: 4 Блок: 1 ', '232': '3-комн, № 232 Площадь: 91.11 м ² Стоимость: 32 799 600 ₸ Цена, м2: 360 000 м ² Этаж:  7 Подъезд: 4 Блок: 1 ', '228': '2-комн, № 228 Площадь: 70.97 м ² Стоимость: 25 123 380 ₸ Цена, м2: 354 000 м ² Этаж:  7 Подъезд: 4 Блок: 1 ', '227': '2-комн, № 227 Площадь: 60.61 м ² Стоимость: 22 607 530 ₸ Цена, м2: 373 000 м ² Этаж:  7 Подъезд: 4 Блок: 1 ', '226': '3-комн, № 226 Площадь: 91.11 м ² Стоимость: 32 981 820 ₸ Цена, м2: 362 000 м ² Этаж:  6 Подъезд: 4 Блок: 1 ', '222': '2-комн, № 222 Площадь: 70.97 м ² Стоимость: 25 265 320 ₸ Цена, м2: 356 000 м ² Этаж:  6 Подъезд: 4 Блок: 1 ', '216': '2-комн, № 216 Площадь: 68.24 м ² Стоимость: 24 293 440 ₸ Цена, м2: 356 000 м ² Этаж:  5 Подъезд: 4 Блок: 1 ', '214': '3-комн, № 214 Площадь: 89.51 м ² Стоимость: 32 402 620 ₸ Цена, м2: 362 000 м ² Этаж:  4 Подъезд: 4 Блок: 1 ', '210': '2-комн, № 210 Площадь: 68.24 м ² Стоимость: 24 293 440 ₸ Цена, м2: 356 000 м ² Этаж:  4 Подъезд: 4 Блок: 1 ', '209': '2-комн, № 209 Площадь: 59.6 м ² Стоимость: 22 350 000 ₸ Цена, м2: 375 000 м ² Этаж:  4 Подъезд: 4 Блок: 1 ', '204': '2-комн, № 204 Площадь: 68.24 м ² Стоимость: 24 293 440 ₸ Цена, м2: 356 000 м ² Этаж:  3 Подъезд: 4 Блок: 1 ', '203': '2-комн, № 203 Площадь: 59.6 м ² Стоимость: 22 350 000 ₸ Цена, м2: 375 000 м ² Этаж:  3 Подъезд: 4 Блок: 1 ', '198': '2-комн, № 198 Площадь: 68.24 м ² Стоимость: 24 156 960 ₸ Цена, м2: 354 000 м ² Этаж:  2 Подъезд: 4 Блок: 1 ', '197': '2-комн, № 197 Площадь: 59.6 м ² Стоимость: 22 230 800 ₸ Цена, м2: 373 000 м ² Этаж:  2 Подъезд: 4 Блок: 1 ', '196': '1-комн, № 196 Площадь: 38.16 м ² Стоимость: 14 195 520 ₸ Цена, м2: 372 000 м ² Этаж:  1 Подъезд: 4 Блок: 1 ', '193': '2-комн, № 193 Площадь: 59.6 м ² Стоимость: 20 740 800 ₸ Цена, м2: 348 000 м ² Этаж:  1 Подъезд: 4 Блок: 1 ', '190': '2-комн, № 190 Площадь: 64.47 м ² Стоимость: 22 500 030 ₸ Цена, м2: 349 000 м ² Этаж:  12 Подъезд: 3 Блок: 1 ', '189': '1-комн, № 189 Площадь: 41.92 м ² Стоимость: 15 342 720 ₸ Цена, м2: 366 000 м ² Этаж:  12 Подъезд: 3 Блок: 1 ', '187': '3-комн, № 187 Площадь: 91.74 м ² Стоимость: 32 659 440 ₸ Цена, м2: 356 000 м ² Этаж:  12 Подъезд: 3 Блок: 1 ', '186': '1-комн, № 186 Площадь: 43.96 м ² Стоимость: 15 825 600 ₸ Цена, м2: 360 000 м ² Этаж:  12 Подъезд: 3 Блок: 1 ', '185': '1-комн, № 185 Площадь: 44.28 м ² Стоимость: 16 029 360 ₸ Цена, м2: 362 000 м ² Этаж:  12 Подъезд: 3 Блок: 1 ', '184': '2-комн, № 184 Площадь: 64.47 м ² Стоимость: 23 144 730 ₸ Цена, м2: 359 000 м ² Этаж:  11 Подъезд: 3 Блок: 1 ', '182': '1-комн, № 182 Площадь: 37.02 м ² Стоимость: 14 733 960 ₸ Цена, м2: 398 000 м ² Этаж:  11 Подъезд: 3 Блок: 1 ', '181': '3-комн, № 181 Площадь: 91.74 м ² Стоимость: 33 943 800 ₸ Цена, м2: 370 000 м ² Этаж:  11 Подъезд: 3 Блок: 1 ', '180': '1-комн, № 180 Площадь: 43.96 м ² Стоимость: 16 572 920 ₸ Цена, м2: 377 000 м ² Этаж:  11 Подъезд: 3 Блок: 1 ', '179': '1-комн, № 179 Площадь: 44.28 м ² Стоимость: 16 737 840 ₸ Цена, м2: 378 000 м ² Этаж:  11 Подъезд: 3 Блок: 1 ', '178': '2-комн, № 178 Площадь: 64.47 м ² Стоимость: 23 338 140 ₸ Цена, м2: 362 000 м ² Этаж:  10 Подъезд: 3 Блок: 1 ', '176': '1-комн, № 176 Площадь: 37.02 м ² Стоимость: 14 733 960 ₸ Цена, м2: 398 000 м ² Этаж:  10 Подъезд: 3 Блок: 1 ', '175': '3-комн, № 175 Площадь: 91.74 м ² Стоимость: 34 310 760 ₸ Цена, м2: 374 000 м ² Этаж:  10 Подъезд: 3 Блок: 1 ', '174': '1-комн, № 174 Площадь: 43.96 м ² Стоимость: 16 572 920 ₸ Цена, м2: 377 000 м ² Этаж:  10 Подъезд: 3 Блок: 1 ', '173': '1-комн, № 173 Площадь: 44.28 м ² Стоимость: 16 737 840 ₸ Цена, м2: 378 000 м ² Этаж:  10 Подъезд: 3 Блок: 1 ', '172': '2-комн, № 172 Площадь: 64.47 м ² Стоимость: 23 338 140 ₸ Цена, м2: 362 000 м ² Этаж:  9 Подъезд: 3 Блок: 1 ', '170': '1-комн, № 170 Площадь: 37.02 м ² Стоимость: 14 733 960 ₸ Цена, м2: 398 000 м ² Этаж:  9 Подъезд: 3 Блок: 1 ', '169': '3-комн, № 169 Площадь: 91.74 м ² Стоимость: 34 310 760 ₸ Цена, м2: 374 000 м ² Этаж:  9 Подъезд: 3 Блок: 1 ', '167': '1-комн, № 167 Площадь: 44.28 м ² Стоимость: 16 737 840 ₸ Цена, м2: 378 000 м ² Этаж:  9 Подъезд: 3 Блок: 1 ', '166': '2-комн, № 166 Площадь: 63.43 м ² Стоимость: 22 961 660 ₸ Цена, м2: 362 000 м ² Этаж:  8 Подъезд: 3 Блок: 1 ', '164': '1-комн, № 164 Площадь: 36.27 м ² Стоимость: 14 435 460 ₸ Цена, м2: 398 000 м ² Этаж:  8 Подъезд: 3 Блок: 1 ', '163': '3-комн, № 163 Площадь: 90.15 м ² Стоимость: 33 716 100 ₸ Цена, м2: 374 000 м ² Этаж:  8 Подъезд: 3 Блок: 1 ', '162': '1-комн, № 162 Площадь: 43.3 м ² Стоимость: 16 324 100 ₸ Цена, м2: 377 000 м ² Этаж:  8 Подъезд: 3 Блок: 1 ', '161': '1-комн, № 161 Площадь: 42.72 м ² Стоимость: 16 148 160 ₸ Цена, м2: 378 000 м ² Этаж:  8 Подъезд: 3 Блок: 1 ', '160': '2-комн, № 160 Площадь: 63.43 м ² Стоимость: 22 961 660 ₸ Цена, м2: 362 000 м ² Этаж:  7 Подъезд: 3 Блок: 1 ', '157': '3-комн, № 157 Площадь: 90.15 м ² Стоимость: 33 716 100 ₸ Цена, м2: 374 000 м ² Этаж:  7 Подъезд: 3 Блок: 1 ', '155': '1-комн, № 155 Площадь: 42.72 м ² Стоимость: 16 148 160 ₸ Цена, м2: 378 000 м ² Этаж:  7 Подъезд: 3 Блок: 1 ', '154': '2-комн, № 154 Площадь: 63.43 м ² Стоимость: 23 088 520 ₸ Цена, м2: 364 000 м ² Этаж:  6 Подъезд: 3 Блок: 1 ', '152': '1-комн, № 152 Площадь: 36.27 м ² Стоимость: 14 508 000 ₸ Цена, м2: 400 000 м ² Этаж:  6 Подъезд: 3 Блок: 1 ', '151': '3-комн, № 151 Площадь: 90.15 м ² Стоимость: 33 896 400 ₸ Цена, м2: 376 000 м ² Этаж:  6 Подъезд: 3 Блок: 1 ', '149': '1-комн, № 149 Площадь: 42.72 м ² Стоимость: 16 233 600 ₸ Цена, м2: 380 000 м ² Этаж:  6 Подъезд: 3 Блок: 1 ', '148': '2-комн, № 148 Площадь: 63.43 м ² Стоимость: 23 088 520 ₸ Цена, м2: 364 000 м ² Этаж:  5 Подъезд: 3 Блок: 1 ', '146': '1-комн, № 146 Площадь: 36.27 м ² Стоимость: 14 508 000 ₸ Цена, м2: 400 000 м ² Этаж:  5 Подъезд: 3 Блок: 1 ', '145': '3-комн, № 145 Площадь: 90.15 м ² Стоимость: 33 896 400 ₸ Цена, м2: 376 000 м ² Этаж:  5 Подъезд: 3 Блок: 1 ', '142': '2-комн, № 142 Площадь: 63.43 м ² Стоимость: 23 088 520 ₸ Цена, м2: 364 000 м ² Этаж:  4 Подъезд: 3 Блок: 1 ', '140': '1-комн, № 140 Площадь: 36.27 м ² Стоимость: 14 508 000 ₸ Цена, м2: 400 000 м ² Этаж:  4 Подъезд: 3 Блок: 1 ', '136': '2-комн, № 136 Площадь: 63.43 м ² Стоимость: 23 088 520 ₸ Цена, м2: 364 000 м ² Этаж:  3 Подъезд: 3 Блок: 1 ', '134': '1-комн, № 134 Площадь: 36.27 м ² Стоимость: 14 508 000 ₸ Цена, м2: 400 000 м ² Этаж:  3 Подъезд: 3 Блок: 1 ', '130': '2-комн, № 130 Площадь: 63.43 м ² Стоимость: 22 961 660 ₸ Цена, м2: 362 000 м ² Этаж:  2 Подъезд: 3 Блок: 1 ', '128': '1-комн, № 128 Площадь: 36.27 м ² Стоимость: 14 435 460 ₸ Цена, м2: 398 000 м ² Этаж:  2 Подъезд: 3 Блок: 1 ', '127': '3-комн, № 127 Площадь: 90.15 м ² Стоимость: 33 716 100 ₸ Цена, м2: 374 000 м ² Этаж:  2 Подъезд: 3 Блок: 1 ', '125': '1-комн, № 125 Площадь: 42.72 м ² Стоимость: 16 062 720 ₸ Цена, м2: 376 000 м ² Этаж:  2 Подъезд: 3 Блок: 1 ', '121': '2-комн, № 121 Площадь: 63.43 м ² Стоимость: 21 693 060 ₸ Цена, м2: 342 000 м ² Этаж:  1 Подъезд: 3 Блок: 1 ', '118': '2-комн, № 118 Площадь: 67.1 м ² Стоимость: 23 686 300 ₸ Цена, м2: 353 000 м ² Этаж:  12 Подъезд: 2 Блок: 1 ', '117': '1-комн, № 117 Площадь: 38.56 м ² Стоимость: 14 691 360 ₸ Цена, м2: 381 000 м ² Этаж:  12 Подъезд: 2 Блок: 1 ', '116': '1-комн, № 116 Площадь: 38.41 м ² Стоимость: 14 634 210 ₸ Цена, м2: 381 000 м ² Этаж:  12 Подъезд: 2 Блок: 1 ', '115': '3-комн, № 115 Площадь: 93.18 м ² Стоимость: 32 706 180 ₸ Цена, м2: 351 000 м ² Этаж:  12 Подъезд: 2 Блок: 1 ', '114': '1-комн, № 114 Площадь: 39.55 м ² Стоимость: 15 464 050 ₸ Цена, м2: 391 000 м ² Этаж:  11 Подъезд: 2 Блок: 1 ', '113': '2-комн, № 113 Площадь: 67.1 м ² Стоимость: 24 357 300 ₸ Цена, м2: 363 000 м ² Этаж:  11 Подъезд: 2 Блок: 1 ', '112': '1-комн, № 112 Площадь: 38.56 м ² Стоимость: 15 346 880 ₸ Цена, м2: 398 000 м ² Этаж:  11 Подъезд: 2 Блок: 1 ', '111': '1-комн, № 111 Площадь: 38.41 м ² Стоимость: 15 210 360 ₸ Цена, м2: 396 000 м ² Этаж:  11 Подъезд: 2 Блок: 1 ', '110': '3-комн, № 110 Площадь: 93.18 м ² Стоимость: 34 010 700 ₸ Цена, м2: 365 000 м ² Этаж:  11 Подъезд: 2 Блок: 1 ', '109': '1-комн, № 109 Площадь: 39.55 м ² Стоимость: 15 464 050 ₸ Цена, м2: 391 000 м ² Этаж:  10 Подъезд: 2 Блок: 1 ', '108': '2-комн, № 108 Площадь: 67.1 м ² Стоимость: 24 558 600 ₸ Цена, м2: 366 000 м ² Этаж:  10 Подъезд: 2 Блок: 1 ', '107': '1-комн, № 107 Площадь: 38.56 м ² Стоимость: 15 346 880 ₸ Цена, м2: 398 000 м ² Этаж:  10 Подъезд: 2 Блок: 1 ', '106': '1-комн, № 106 Площадь: 38.41 м ² Стоимость: 15 210 360 ₸ Цена, м2: 396 000 м ² Этаж:  10 Подъезд: 2 Блок: 1 ', '105': '3-комн, № 105 Площадь: 93.18 м ² Стоимость: 34 383 420 ₸ Цена, м2: 369 000 м ² Этаж:  10 Подъезд: 2 Блок: 1 ', '104': '1-комн, № 104 Площадь: 39.55 м ² Стоимость: 15 464 050 ₸ Цена, м2: 391 000 м ² Этаж:  9 Подъезд: 2 Блок: 1 ', '103': '2-комн, № 103 Площадь: 67.1 м ² Стоимость: 24 558 600 ₸ Цена, м2: 366 000 м ² Этаж:  9 Подъезд: 2 Блок: 1 ', '102': '1-комн, № 102 Площадь: 38.56 м ² Стоимость: 15 346 880 ₸ Цена, м2: 398 000 м ² Этаж:  9 Подъезд: 2 Блок: 1 ', '101': '1-комн, № 101 Площадь: 38.41 м ² Стоимость: 15 210 360 ₸ Цена, м2: 396 000 м ² Этаж:  9 Подъезд: 2 Блок: 1 ', '100': '3-комн, № 100 Площадь: 93.18 м ² Стоимость: 34 383 420 ₸ Цена, м2: 369 000 м ² Этаж:  9 Подъезд: 2 Блок: 1 ', '99': '1-комн, № 99 Площадь: 38.93 м ² Стоимость: 15 221 630 ₸ Цена, м2: 391 000 м ² Этаж:  8 Подъезд: 2 Блок: 1 ', '98': '2-комн, № 98 Площадь: 66.07 м ² Стоимость: 24 181 620 ₸ Цена, м2: 366 000 м ² Этаж:  8 Подъезд: 2 Блок: 1 ', '97': '1-комн, № 97 Площадь: 37.75 м ² Стоимость: 15 024 500 ₸ Цена, м2: 398 000 м ² Этаж:  8 Подъезд: 2 Блок: 1 ', '96': '1-комн, № 96 Площадь: 37.61 м ² Стоимость: 14 893 560 ₸ Цена, м2: 396 000 м ² Этаж:  8 Подъезд: 2 Блок: 1 ', '95': '3-комн, № 95 Площадь: 91.58 м ² Стоимость: 33 793 020 ₸ Цена, м2: 369 000 м ² Этаж:  8 Подъезд: 2 Блок: 1 ', '93': '2-комн, № 93 Площадь: 66.07 м ² Стоимость: 24 181 620 ₸ Цена, м2: 366 000 м ² Этаж:  7 Подъезд: 2 Блок: 1 ', '91': '1-комн, № 91 Площадь: 37.61 м ² Стоимость: 14 893 560 ₸ Цена, м2: 396 000 м ² Этаж:  7 Подъезд: 2 Блок: 1 ', '90': '3-комн, № 90 Площадь: 91.58 м ² Стоимость: 33 793 020 ₸ Цена, м2: 369 000 м ² Этаж:  7 Подъезд: 2 Блок: 1 ', '89': '1-комн, № 89 Площадь: 38.93 м ² Стоимость: 15 299 490 ₸ Цена, м2: 393 000 м ² Этаж:  6 Подъезд: 2 Блок: 1 ', '88': '2-комн, № 88 Площадь: 66.07 м ² Стоимость: 24 313 760 ₸ Цена, м2: 368 000 м ² Этаж:  6 Подъезд: 2 Блок: 1 ', '87': '1-комн, № 87 Площадь: 37.75 м ² Стоимость: 15 100 000 ₸ Цена, м2: 400 000 м ² Этаж:  6 Подъезд: 2 Блок: 1 ', '86': '1-комн, № 86 Площадь: 37.61 м ² Стоимость: 14 968 780 ₸ Цена, м2: 398 000 м ² Этаж:  6 Подъезд: 2 Блок: 1 ', '85': '3-комн, № 85 Площадь: 91.58 м ² Стоимость: 33 976 180 ₸ Цена, м2: 371 000 м ² Этаж:  6 Подъезд: 2 Блок: 1 ', '83': '2-комн, № 83 Площадь: 66.07 м ² Стоимость: 24 313 760 ₸ Цена, м2: 368 000 м ² Этаж:  5 Подъезд: 2 Блок: 1 ', '81': '1-комн, № 81 Площадь: 37.61 м ² Стоимость: 14 968 780 ₸ Цена, м2: 398 000 м ² Этаж:  5 Подъезд: 2 Блок: 1 ', '80': '3-комн, № 80 Площадь: 91.58 м ² Стоимость: 33 976 180 ₸ Цена, м2: 371 000 м ² Этаж:  5 Подъезд: 2 Блок: 1 ', '79': '1-комн, № 79 Площадь: 38.93 м ² Стоимость: 15 299 490 ₸ Цена, м2: 393 000 м ² Этаж:  4 Подъезд: 2 Блок: 1 ', '78': '2-комн, № 78 Площадь: 66.07 м ² Стоимость: 24 313 760 ₸ Цена, м2: 368 000 м ² Этаж:  4 Подъезд: 2 Блок: 1 ', '77': '1-комн, № 77 Площадь: 37.75 м ² Стоимость: 15 100 000 ₸ Цена, м2: 400 000 м ² Этаж:  4 Подъезд: 2 Блок: 1 ', '75': '3-комн, № 75 Площадь: 91.58 м ² Стоимость: 33 976 180 ₸ Цена, м2: 371 000 м ² Этаж:  4 Подъезд: 2 Блок: 1 ', '74': '1-комн, № 74 Площадь: 38.93 м ² Стоимость: 15 299 490 ₸ Цена, м2: 393 000 м ² Этаж:  3 Подъезд: 2 Блок: 1 ', '73': '2-комн, № 73 Площадь: 66.07 м ² Стоимость: 24 313 760 ₸ Цена, м2: 368 000 м ² Этаж:  3 Подъезд: 2 Блок: 1 ', '71': '1-комн, № 71 Площадь: 37.61 м ² Стоимость: 14 968 780 ₸ Цена, м2: 398 000 м ² Этаж:  3 Подъезд: 2 Блок: 1 ', '70': '3-комн, № 70 Площадь: 91.58 м ² Стоимость: 33 976 180 ₸ Цена, м2: 371 000 м ² Этаж:  3 Подъезд: 2 Блок: 1 ', '69': '1-комн, № 69 Площадь: 38.93 м ² Стоимость: 15 221 630 ₸ Цена, м2: 391 000 м ² Этаж:  2 Подъезд: 2 Блок: 1 ', '68': '2-комн, № 68 Площадь: 66.07 м ² Стоимость: 24 181 620 ₸ Цена, м2: 366 000 м ² Этаж:  2 Подъезд: 2 Блок: 1 ', '67': '1-комн, № 67 Площадь: 37.75 м ² Стоимость: 14 911 250 ₸ Цена, м2: 395 000 м ² Этаж:  2 Подъезд: 2 Блок: 1 ', '66': '1-комн, № 66 Площадь: 37.61 м ² Стоимость: 14 893 560 ₸ Цена, м2: 396 000 м ² Этаж:  2 Подъезд: 2 Блок: 1 ', '65': '3-комн, № 65 Площадь: 91.58 м ² Стоимость: 33 793 020 ₸ Цена, м2: 369 000 м ² Этаж:  2 Подъезд: 2 Блок: 1 ', '63': '2-комн, № 63 Площадь: 60.79 м ² Стоимость: 20 972 550 ₸ Цена, м2: 345 000 м ² Этаж:  1 Подъезд: 2 Блок: 1 ', '60': '2-комн, № 60 Площадь: 61.51 м ² Стоимость: 21 897 560 ₸ Цена, м2: 356 000 м ² Этаж:  12 Подъезд: 1 Блок: 1 ', '59': '2-комн, № 59 Площадь: 66.88 м ² Стоимость: 23 140 480 ₸ Цена, м2: 346 000 м ² Этаж:  12 Подъезд: 1 Блок: 1 ', '56': '1-комн, № 56 Площадь: 44.73 м ² Стоимость: 16 102 800 ₸ Цена, м2: 360 000 м ² Этаж:  12 Подъезд: 1 Блок: 1 ', '55': '2-комн, № 55 Площадь: 61.51 м ² Стоимость: 22 512 660 ₸ Цена, м2: 366 000 м ² Этаж:  11 Подъезд: 1 Блок: 1 ', '54': '2-комн, № 54 Площадь: 66.88 м ² Стоимость: 23 876 160 ₸ Цена, м2: 357 000 м ² Этаж:  11 Подъезд: 1 Блок: 1 ', '53': '2-комн, № 53 Площадь: 54.09 м ² Стоимость: 20 337 840 ₸ Цена, м2: 376 000 м ² Этаж:  11 Подъезд: 1 Блок: 1 ', '52': '2-комн, № 52 Площадь: 49.93 м ² Стоимость: 18 374 240 ₸ Цена, м2: 368 000 м ² Этаж:  11 Подъезд: 1 Блок: 1 ', '51': '1-комн, № 51 Площадь: 44.73 м ² Стоимость: 16 818 480 ₸ Цена, м2: 376 000 м ² Этаж:  11 Подъезд: 1 Блок: 1 ', '50': '2-комн, № 50 Площадь: 61.51 м ² Стоимость: 22 697 190 ₸ Цена, м2: 369 000 м ² Этаж:  10 Подъезд: 1 Блок: 1 ', '49': '2-комн, № 49 Площадь: 66.88 м ² Стоимость: 24 076 800 ₸ Цена, м2: 360 000 м ² Этаж:  10 Подъезд: 1 Блок: 1 ', '48': '2-комн, № 48 Площадь: 54.09 м ² Стоимость: 20 500 110 ₸ Цена, м2: 379 000 м ² Этаж:  10 Подъезд: 1 Блок: 1 ', '47': '2-комн, № 47 Площадь: 49.93 м ² Стоимость: 18 524 030 ₸ Цена, м2: 371 000 м ² Этаж:  10 Подъезд: 1 Блок: 1 ', '46': '1-комн, № 46 Площадь: 44.73 м ² Стоимость: 16 818 480 ₸ Цена, м2: 376 000 м ² Этаж:  10 Подъезд: 1 Блок: 1 ', '45': '2-комн, № 45 Площадь: 61.51 м ² Стоимость: 22 697 190 ₸ Цена, м2: 369 000 м ² Этаж:  9 Подъезд: 1 Блок: 1 ', '44': '2-комн, № 44 Площадь: 66.88 м ² Стоимость: 24 076 800 ₸ Цена, м2: 360 000 м ² Этаж:  9 Подъезд: 1 Блок: 1 ', '43': '2-комн, № 43 Площадь: 54.09 м ² Стоимость: 20 500 110 ₸ Цена, м2: 379 000 м ² Этаж:  9 Подъезд: 1 Блок: 1 ', '42': '2-комн, № 42 Площадь: 49.93 м ² Стоимость: 18 524 030 ₸ Цена, м2: 371 000 м ² Этаж:  9 Подъезд: 1 Блок: 1 ', '41': '1-комн, № 41 Площадь: 44.73 м ² Стоимость: 16 818 480 ₸ Цена, м2: 376 000 м ² Этаж:  9 Подъезд: 1 Блок: 1 ', '40': '2-комн, № 40 Площадь: 60.5 м ² Стоимость: 22 324 500 ₸ Цена, м2: 369 000 м ² Этаж:  8 Подъезд: 1 Блок: 1 ', '39': '2-комн, № 39 Площадь: 64.23 м ² Стоимость: 23 122 800 ₸ Цена, м2: 360 000 м ² Этаж:  8 Подъезд: 1 Блок: 1 ', '38': '2-комн, № 38 Площадь: 52.83 м ² Стоимость: 20 022 570 ₸ Цена, м2: 379 000 м ² Этаж:  8 Подъезд: 1 Блок: 1 ', '36': '1-комн, № 36 Площадь: 43.16 м ² Стоимость: 16 228 160 ₸ Цена, м2: 376 000 м ² Этаж:  8 Подъезд: 1 Блок: 1 ', '35': '2-комн, № 35 Площадь: 60.5 м ² Стоимость: 22 324 500 ₸ Цена, м2: 369 000 м ² Этаж:  7 Подъезд: 1 Блок: 1 ', '33': '2-комн, № 33 Площадь: 52.83 м ² Стоимость: 20 022 570 ₸ Цена, м2: 379 000 м ² Этаж:  7 Подъезд: 1 Блок: 1 ', '31': '1-комн, № 31 Площадь: 43.16 м ² Стоимость: 16 228 160 ₸ Цена, м2: 376 000 м ² Этаж:  7 Подъезд: 1 Блок: 1 ', '30': '2-комн, № 30 Площадь: 60.5 м ² Стоимость: 22 445 500 ₸ Цена, м2: 371 000 м ² Этаж:  6 Подъезд: 1 Блок: 1 ', '29': '2-комн, № 29 Площадь: 64.23 м ² Стоимость: 23 251 260 ₸ Цена, м2: 362 000 м ² Этаж:  6 Подъезд: 1 Блок: 1 ', '27': '2-комн, № 27 Площадь: 48.28 м ² Стоимость: 18 008 440 ₸ Цена, м2: 373 000 м ² Этаж:  6 Подъезд: 1 Блок: 1 ', '26': '1-комн, № 26 Площадь: 43.16 м ² Стоимость: 16 314 480 ₸ Цена, м2: 378 000 м ² Этаж:  6 Подъезд: 1 Блок: 1 ', '25': '2-комн, № 25 Площадь: 60.5 м ² Стоимость: 22 445 500 ₸ Цена, м2: 371 000 м ² Этаж:  5 Подъезд: 1 Блок: 1 ', '24': '2-комн, № 24 Площадь: 64.23 м ² Стоимость: 23 251 260 ₸ Цена, м2: 362 000 м ² Этаж:  5 Подъезд: 1 Блок: 1 ', '19': '2-комн, № 19 Площадь: 64.23 м ² Стоимость: 23 251 260 ₸ Цена, м2: 362 000 м ² Этаж:  4 Подъезд: 1 Блок: 1 ', '18': '2-комн, № 18 Площадь: 52.83 м ² Стоимость: 20 128 230 ₸ Цена, м2: 381 000 м ² Этаж:  4 Подъезд: 1 Блок: 1 ', '16': '1-комн, № 16 Площадь: 43.16 м ² Стоимость: 16 314 480 ₸ Цена, м2: 378 000 м ² Этаж:  4 Подъезд: 1 Блок: 1 ', '14': '2-комн, № 14 Площадь: 64.23 м ² Стоимость: 23 251 260 ₸ Цена, м2: 362 000 м ² Этаж:  3 Подъезд: 1 Блок: 1 ', '12': '2-комн, № 12 Площадь: 48.28 м ² Стоимость: 18 008 440 ₸ Цена, м2: 373 000 м ² Этаж:  3 Подъезд: 1 Блок: 1 ', '11': '1-комн, № 11 Площадь: 43.16 м ² Стоимость: 16 314 480 ₸ Цена, м2: 378 000 м ² Этаж:  3 Подъезд: 1 Блок: 1 ', '10': '2-комн, № 10 Площадь: 60.5 м ² Стоимость: 22 324 500 ₸ Цена, м2: 369 000 м ² Этаж:  2 Подъезд: 1 Блок: 1 ', '9': '2-комн, № 9 Площадь: 64.23 м ² Стоимость: 23 122 800 ₸ Цена, м2: 360 000 м ² Этаж:  2 Подъезд: 1 Блок: 1 ', '7': '2-комн, № 7 Площадь: 48.28 м ² Стоимость: 17 911 880 ₸ Цена, м2: 371 000 м ² Этаж:  2 Подъезд: 1 Блок: 1 ', '4': '1-комн, № 4 Площадь: 43.16 м ² Стоимость: 15 235 480 ₸ Цена, м2: 353 000 м ² Этаж:  1 Подъезд: 1 Блок: 1 ', '3': '2-комн, № 3 Площадь: 60.5 м ² Стоимость: 20 933 000 ₸ Цена, м2: 346 000 м ² Этаж:  1 Подъезд: 1 Блок: 1 ', '2': '1-комн, № 2 Площадь: 37.2 м ² Стоимость: 13 726 800 ₸ Цена, м2: 369 000 м ² Этаж:  1 Подъезд: 1 Блок: 1 '}
#
# file_name = 'resultList.json'
# path_for_file = os.path.join(file_name)
# # with open(file_name, 'w') as f:
# #     f.write(json.dumps(resulst_list))
#
# with open(file_name) as f:
#     data = json.load(f)
#
#     for key, value in resulst_list.items():
#         print(key, value)
#     # print(data)
#     print(len(data))
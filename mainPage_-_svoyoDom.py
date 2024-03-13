import requests
from bs4 import BeautifulSoup

# url = 'https://svoydom.kz/project/1/1061833/?objview=list&PAGEN_1=1&bxajaxid=ed9cca27dcf034d99c8046454bd163c2'

last_page_pagination = 13
for i in range(1, last_page_pagination + 1):
    # print(i)
    url = f'https://svoydom.kz/project/1/1061833/?objview=list&PAGEN_1={i}&bxajaxid=ed9cca27dcf034d99c8046454bd163c2'

# url = 'https://svoydom.kz/project/1/1061833/?objview=list&PAGEN_1=2&bxajaxid=ed9cca27dcf034d99c8046454bd163c2'
# url = 'https://svoydom.kz/project/1/1061833/'
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
        # print(i)
        # print(i.split('\n'))
        remove_data += i.split('\n')

    for i in remove_data:
        if i:
            resultInfo.append(i)

    count = 0
    for i in resultInfo:
        count += 1

        print(i, end=' ')
        if count % 13 == 0:
            print('')

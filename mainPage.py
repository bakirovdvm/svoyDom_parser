from collectFullDataToDict import make_json
from exportDataToExcel import make_excel


project_name = 'GAKKU'
last_page_pagination = 2
url = 'https://svoydom.kz/project/flat/all/nazvanie_obekta_zhk-is-gakku/apply/?PAGEN_1={i_page}&bxajaxid=f8f26e29099fe0ef7724b58a2b3d2dd9'


def main():
    make_json(project_name, last_page_pagination, url)
    make_excel(project_name)


if __name__ == "__main__":
    main()



import requests
from bs4 import BeautifulSoup
import json

def getUrls():
    # 定义超链接内容
    base_url = "https://www.kylc.com/stats/global/yearly/"
    kind_url = "g_gdp/"
    year_min = 1960
    year_max = 2024
    suffix_url = ".html"

    # 定义urls数组用于存储超链接
    urls = list()

    # 循环遍历所有年份
    while year_min <= year_max:
        urls.append(base_url + kind_url + str(year_min) + suffix_url)
        year_min = year_min + 1
    return urls


def parser(urls):
    result = {}
    # 遍历urls数组
    for url in urls:
        r = requests.get(url)
        result_year = {}
        # result_year.update("1960":[])

        # 若html内容获取成功
        if r.status_code == 200:
            # 此处需使用decode解码，否则中文显示不正确
            soup = BeautifulSoup(r.content.decode("utf-8"), "html.parser")
            # print(soup)
            # 查询tbody标签中的区块
            table_node = soup.find("tbody")
            # print(table_node)
            # print("="*30)
            # 查询该区块中的td标签
            contents = table_node.find_all("td")
            # 定义数组索引号
            i = 0
            # 定义数据序列号
            count = 1
            # print(len(contents))
            while i < len(contents):
                # print(contents[i].get_text())
                #匹配当前标签内容为数据序列号，按照网页规则提取相应内容
                if contents[i].get_text() == str(count):
                    # print(contents[i].get_text() + " " + contents[i + 1].get_text() + " " + contents[i + 3].get_text())
                    count = count + 1
                    list = list()
                    list.append(contents[i].get_text())
                    list.append(contents[i+1].get_text())
                    list.append(contents[i+3].get_text())

                    json_str = json.dumps(result_year)


                    json.dump(result_year.update(axis),result_year)
                    i = i + 5
                else:
                    i = i + 1
            result_year = 123123


            print(result_year)
            #测试环境下仅提取一份数据
            break
        else:
            continue


if __name__ == '__main__':
    # 1.获取待爬取urls
    urls = list()
    urls = getUrls()

    # r = requests.get("https://www.kylc.com/stats/global/yearly/g_gdp/1960.html")
    # #解码
    # print(r.content.decode("utf-8"))

    # print(urls)
    # 2.解析urls.content
    parser(urls)

    pass

import requests
from bs4 import BeautifulSoup


def get_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.132 Safari/537.36 ',
        'Host': 'movie.douban.com'
    }
    index = 0
    for i in range(10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        response = requests.get(link, headers=headers, timeout=10)
        # print('第%s页响应状态码:' % str(i + 1), response.status_code)
        soup = BeautifulSoup(response.text, "lxml")
        div_list = soup.find_all('div', class_='info')
        for each in div_list:
            index += 1
            print('-----获取第 %d 部电影信息-----' % index)
            # print(each)
            # 电影名
            title = each.find('div', class_='hd').a.span.text.strip()
            print(title)
            # 演职员信息
            # info = each.find('div', class_='bd').p.text.strip()
            # # print(info)
            # info = info.replace("\n", " ").replace("\xa0", " ")
            # info = ' '.join(info.split())
            # print(info)
            # 评分
            rating = each.find('span', class_='rating_num').text.strip()
            print(rating)
            # 评分人数
            # num_rating = each.find('div', class_='star').contents[7].text.strip()
            # print(num_rating)
            # 简介
            try:
                quote = each.find('span', class_='inq').text.strip()
            except:
                quote = '无简介'
            print(quote)

            with open('./douban_movie250.txt', 'a+', encoding='utf-8') as f:
                f.write('\t'.join([title, rating, quote]))
                f.write('\n')
            print('\n')


get_movies()

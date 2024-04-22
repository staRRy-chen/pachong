import requests
from bs4 import BeautifulSoup
import re
import csv
url = "http://www.gev.org.cn/news/8201.html"
pattern = r'\b\d{4}/\d{2}/\d{2}\b'
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析HTML内容
    print(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('div', attrs={'class': 'e_box e_box-000 p_TitleBoxA'})
    print(title.text.strip())
    # time = soup.find('div', attrs={'class': 'e_box e_box-000 p_AssistInfo'})
    # matches = re.findall(pattern, time.text.strip())
    news = soup.find('div', attrs={'id': 'c_news_detail-15858303195441036'})
    contents = news.find('article', attrs={'class': 'e_HtmlEditor e_HtmlEditor-001 p_articles'})
    # print(contents)
    if contents:
        paras=contents.find_all('p')
        for para in paras:
            if para.find('img'):
                break
            print(para.text.strip())
    # print(contents)
    # 或者获取页面的所有段落内容：
    # policy=soup.find('div', attrs={'id': 'c_breadcrumb_nav-15477036596541707'})
    # print(policy)
else:
    print(f"请求失败，状态码: {response.status_code}")


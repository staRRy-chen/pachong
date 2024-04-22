import requests
from bs4 import BeautifulSoup
import re
import csv
# url = "http://www.gev.org.cn/news/8201.html"
# response = requests.get(url)
pattern = r'\b\d{4}/\d{2}/\d{2}\b'

with open("D:/zzh/data1.csv", "w",newline='',encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile,delimiter=',')
    writer.writerow(["日期", "标题", "正文"])
    for i in range(4000,8250):
        url = f"http://www.gev.org.cn/news/{i}.html"
        response = requests.get(url)
        if response.status_code == 200:
            # 解析HTML内容
            soup = BeautifulSoup(response.text, 'html.parser')
            policy = soup.find('div', attrs={'id': 'c_breadcrumb_nav-15477036596541707'})
            if policy == None:
                continue
            print(url)
            time = soup.find('div', attrs={'class': 'e_box e_box-000 p_AssistInfo'})
            matches = re.findall(pattern, time.text.strip())
            if(matches!=[]):
                date=matches[0]
            else:
                date='最近'
            content=str(soup.head.find('meta', attrs={'name': 'description'})['content'])
            title=str(soup.head.find('meta', attrs={'name': 'keywords'})['content'])
            print(title)
            writer.writerow([date, title, content])
        # else:
        #     print(f"请求失败，状态码: {response.status_code}")

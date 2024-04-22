import csv
import re
import requests
import time
from bs4 import BeautifulSoup
pattern = r'\b\d{4}/\d{2}/\d{2}\b'

with open("D:/zzh/pageAll_500-519.csv", "w", newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["日期", "标题", "正文"])
    for i in range(500,519):
        url = f"http://www.gev.org.cn/comp/news/list.do?compId=news_list-15476985505928450&cid=14&pageSize=6&currentPage={i}"
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Cookie': 'Hm_lvt_12c82fd986185fa98069bb62619762c0=1713183170; JSESSIONID=73D5E06E75E897E0D49CB6C5225B909A; sensorsdata2015jssdkcrossZQSensorsObj=%7B%22distinct_id%22%3A%2218ee1ac9f6d10d8-064216e561b1c28-4c657b58-2073600-18ee1ac9f6e104d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22http%3A%2F%2Fwww.gev.org.cn%2Fnews33.html%23c_news_list-15476985505928450-3%22%7D%2C%22%24device_id%22%3A%2218ee1ac9f6d10d8-064216e561b1c28-4c657b58-2073600-18ee1ac9f6e104d%22%7D; Hm_lpvt_12c82fd986185fa98069bb62619762c0=1713199230',
            'Host': 'www.gev.org.cn',
            'Origin': 'http://www.gev.org.cn',
            'Referer': 'http://www.gev.org.cn/news33.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
        }
        print(url)
        response = requests.post(url, headers=headers)

        # 检查请求是否成功
        if response.status_code == 200:
            time.sleep(1)
            soup = BeautifulSoup(response.text, 'html.parser')
            news_list = soup.find('div', attrs={'class': 'e_box e_articles-001 p_Newslist'}).find('div', attrs={'class': 'e_box e_box-000 p_news'})
            card_list= news_list.find_all('div', attrs={'class': 'e_box e_ListBox-001 p_articles'})
            for card in card_list:
                herf = card.find('a')['href']
                urlA = f"http://www.gev.org.cn{herf}"
                print(urlA)
                headersA = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Cookie': 'Hm_lvt_12c82fd986185fa98069bb62619762c0=1713183170; sensorsdata2015jssdkcrossZQSensorsObj=%7B%22distinct_id%22%3A%2218ee1ac9f6d10d8-064216e561b1c28-4c657b58-2073600-18ee1ac9f6e104d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22http%3A%2F%2Fwww.gev.org.cn%2Fnews%2F8154.html%22%7D%2C%22%24device_id%22%3A%2218ee1ac9f6d10d8-064216e561b1c28-4c657b58-2073600-18ee1ac9f6e104d%22%7D; JSESSIONID=5E8EE67F70CA65686109EA77120AD408; Hm_lpvt_12c82fd986185fa98069bb62619762c0=1713230411',
                    'Host': 'www.gev.org.cn',
                    'Referer': 'http://www.gev.org.cn/news33.html',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
                }
                responseA = requests.get(urlA,headers=headersA)
                if responseA.status_code == 200:
                    # 解析HTML内容
                    #print(urlA)
                    soupA = BeautifulSoup(responseA.text, 'html.parser')
                    timeA = soupA.find('div', attrs={'class': 'e_box e_box-000 p_AssistInfo'})
                    matches = re.findall(pattern, timeA.text.strip())
                    if (matches != []):
                        date = matches[0]
                    else:
                        date = '最近'
                    content = str(soupA.head.find('meta', attrs={'name': 'description'})['content'])
                    # news = soupA.find('div', attrs={'class': 'c_news_detail-01001'})
                    # contents = news.find('article', attrs={'class': 'e_HtmlEditor e_HtmlEditor-001 p_articles'})
                    # content=''
                    # if contents:
                    #     paras = contents.find_all('p')
                    #     for para in paras:
                    #         if para.find('img'):
                    #             break
                    #         content+=para.text.strip()
                    #title = str(soupA.head.find('meta', attrs={'name': 'keywords'})['content'])
                    title = soupA.find('div', attrs={'class': 'e_box e_box-000 p_TitleBoxA'}).text.strip()
                    print(title)
                    writer.writerow([date, title, content])
                    time.sleep(1)
                else:
                    print(f"请求失败，状态码: {responseA.status_code}")
                    time.sleep(1)

        else:
            print(f"请求失败，状态码: {response.status_code}")
            time.sleep(1)
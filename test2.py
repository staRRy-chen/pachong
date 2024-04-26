import csv
import re
import jieba
import pandas as pd
import gensim
from gensim import corpora
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import warnings

import pyLDAvis.gensim

warnings.filterwarnings('ignore')  # To ignore all warnings that arise here to enhance clarity

from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel

def chinese_word_cut(mytext):
    # jieba.load_userdict('自定义词典.txt')  # 这里你可以添加jieba库识别不了的网络新词，避免将一些新词拆开
    jieba.initialize()  # 初始化jieba
    # 文本预处理 ：去除一些无用的字符只提取出中文出来
    new_data = re.findall('[\u4e00-\u9fa5]+', mytext, re.S)
    new_data = " ".join(new_data)
    new_data = new_data.replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
    # 文本分词
    seg_list_exact = jieba.lcut(new_data)
    result_list = []
    # 读取停用词库
    with open('hit_stopwords.txt', encoding='utf-8') as f:  # 可根据需要打开停用词库，然后加上不想显示的词语
        con = f.readlines()
        stop_words = set()
        for i in con:
            i = i.replace("\n", "")  # 去掉读取每一行数据的\n
            stop_words.add(i)
    # 去除停用词并且去除单字
    for word in seg_list_exact:
        if word not in stop_words and len(word) > 1:
            result_list.append(word)
    return result_list


def get_text(path):
    with open(path, 'r', encoding='GBK') as f,open('D:/zzh/seg2.txt', 'a+', encoding='utf-8') as targetFile:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            if row[0] != 'appln_id':
                text = row[6]
                result_list = chinese_word_cut(text)
                data_set.append(result_list)
                output = ' '.join(result_list)
                targetFile.write(output)
                targetFile.write('\n')
                print('写入成功！')
                i += 1

data_set=[]
path = 'D:/zzh/out.csv'
targetTxt = 'D:/zzh/seg.txt'
get_text(path)
print(data_set)
# result_list = chinese_word_cut(text)
# with open(targetTxt, 'a+', encoding = 'utf-8') as targetFile:
#     # 分好词之后之间用空格隔断
#     output = ' '.join(result_list)
#     targetFile.write(output)
#     targetFile.write('\n')
#     print('写入成功！')
# print(result_list)

dictionary = corpora.Dictionary(data_set)  # 构建词典
corpus = [dictionary.doc2bow(text) for text in data_set]  #表示为第几个单词出现了几次
print(dictionary.token2id)
lda = LdaModel(corpus=corpus, num_topics=6, id2word = dictionary, passes=30,random_state = 1)
for topic in lda.print_topics(num_words=6):
    print(topic)
# for i in lda.get_document_topics(corpus)[:]:
#     listj = []
#     for j in i:
#         listj.append(j[1])
#     bz = listj.index(max(listj))
#     print(i[bz][0])

data = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
pyLDAvis.save_html(data, 'D:/zzh/topic2.html')
print("success!")

# 创建一个空的 DataFrame 以存储主题概率
topic_columns = [f"Topic_{i}" for i in range(lda.num_topics)]
result_df = pd.DataFrame(columns=topic_columns)

# 遍历文本
for i, doc in enumerate(corpus):
    doc_topics = lda.get_document_topics(doc)

    # 创建一个字典，表示主题概率
    topic_prob_dict = {f"Topic_{index}": prob for index, prob in doc_topics}

    # 如果主题不存在，将其概率设置为0
    missing_topics = set(topic_columns) - set(topic_prob_dict.keys())
    for missing_topic in missing_topics:
        topic_prob_dict[missing_topic] = 0.0

    # 将主题概率添加到 DataFrame
    result_df = pd.concat([result_df, pd.DataFrame(topic_prob_dict, index=[i])], ignore_index=True)

# 重置索引
result_df = result_df.reset_index(drop=True)
result_df.to_excel('D:/zzh/result2.xlsx', index=False)
print("success!")
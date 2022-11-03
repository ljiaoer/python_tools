# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 20:27:15 2022

@author: lijiaojiao
"""

import jieba
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud



# 读取停用词列表
def get_stopword_list(stopwordfile):
    with open(stopwordfile, 'r', encoding='utf-8') as f:    # 
        stopword_list = [word.strip('\n') for word in f.readlines()]
    return stopword_list


# 分词 然后清除停用词语
def clean_stopword(processfile, stopword_list):
    result = ''
    with open(processfile,encoding = "utf-8") as f:
        mytext = f.read()
    word_list = jieba.lcut(mytext)
    for w in word_list:
        if w not in stopword_list:
            result = result + " " + w
    return result

# 词频统计

def word_count(cleantext):
    df = pd.DataFrame(cleantext.split( ),columns =["words"])
    res_count = df.groupby(["words"]).size().sort_values(ascending=False)
    res_count.to_excel("result_count.xlsx")


# 绘制词云图
def word_cloud(cleantext):
    wordcloud = WordCloud(font_path = "simsun.ttf",stopwords = stopword_list).generate(cleantext)
    #%pylab inline
    plt.imshow(wordcloud, interpolation = "bilinear")
    plt.axis("off")




if __name__ == '__main__':
    stopword_file = 'E:/Tools/stopwords/hit_stopwords.txt'
    process_file = 'E:/Tools/Chinese_Text_Split_Wordcloud/report20.txt'
    stopword_list = get_stopword_list(stopword_file)    # 获得停用词列表
    cleanwords = clean_stopword(process_file, stopword_list)
    word_count(cleanwords)
    word_cloud(cleanwords)
    
   
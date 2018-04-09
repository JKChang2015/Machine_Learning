# -*- coding: utf-8 -*-
# news classifier
# Created by JKChang
# 09/04/2018, 21:03
# Tag:
# Description: 

import jieba
import pandas as pd

df_news = pd.read_table('./resources/val.txt', names=['category', 'theme', 'URL', 'content'], encoding='utf-8')
df_news = df_news.dropna()

content = df_news.content.values.tolist()

content_S = []
for line in content:
    current_segment = jieba.lcut(line)  # term splitor
    if len(current_segment) > 1 and current_segment != '\r\n':
        content_S.append(current_segment)

df_content = pd.DataFrame({'content_S': content_S})
stopwords = pd.read_csv(
    "./resources/stopwords.txt",
    index_col=False,
    sep="\t",
    quoting=3,
    names=['stopword'],
    encoding='utf-8')

def drop_stopwords(contents, stopwords):
    contents_clean = []
    all_words = []
    for line in contents:
        line_clean = []
        for word in line:
            print(word)
            if word in stopwords:
                continue
            line_clean.append(word)
            all_words.append(str(word))  # bag of words
        contents_clean.append(line_clean)
    return contents_clean, all_words


contents = df_content.content_S.values.tolist()
stopwords = stopwords.stopword.values.tolist()
contents_clean, all_words = drop_stopwords(contents, stopwords)

print(contents_clean)
print(all_words)
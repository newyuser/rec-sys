# -*- coding: utf-8 -*-
"""
这里主要实现一些工具类的函数
"""
import re
import sys
sys.path.append("../../")
import jieba
import jieba.analyse
from conf.proj_path import stop_words_path

def get_key_words(words_str):
    """提取中文中的关键词
    """
    # 字符串进行清洗
    # 去除一些符号
    words_str.replace('\n', '').replace('\u3000', '').replace('\u00A0', '') 
    # 去除数字，特殊字符
    words_str = re.sub('[a-zA-Z0-9.。:：,，]', '', words_str)  
    # 切词
    words_list = jieba.cut(words_str)
    
    # 加载停用词
    stopword_set = set()
    with open(stop_words_path, encoding="utf-8") as f:
        line = f.readline().rstrip()
        stopword_set.add(line)
    
    # 去除停用词
    new_words_list = []
    for word in words_list:
        if word in stopword_set:
            continue
        new_words_list.append(word)
    
    new_words_str = " ".join(new_words_list)

    # 提取关键词   
    # 默认是TF-IDF
    key_words_list_tfidf = jieba.analyse.extract_tags(new_words_str, topK=10, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
    key_words_list_textrank = jieba.analyse.textrank(new_words_str, topK=10, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
    
    tfidf_textrank_list = list(set(key_words_list_tfidf) & set(key_words_list_textrank))[:3]

    return tfidf_textrank_list

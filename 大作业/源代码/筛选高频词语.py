from jieba import *
from jieba.analyse import *

text = ''
# 对爬取的结果“网页文档提取结果.txt”进行了格式上的修改，后者命名为"网页文档提取结果_修改后.txt"
# '网页文档提取结果_修改后.txt'对应上传数据集'2307385106杜净瑶数据科学231_2.txt'
with open('网页文档提取结果_修改后.txt', 'r', encoding='utf-8') as file:
    text = file.read()
word_dict = {}
words = lcut(text)
for word in words:
    if len(word) < 3:
        continue
    else:
        word_dict[word] = word_dict.get(word, 0) + 1
sort_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
for word, count in sort_list:
    print(f'{word:}:{count:}')

# 将前30的词语写进文档
with open('高频词.txt', 'w', encoding='utf-8') as file:
    i = 0
    for word, count in sort_list:
        if i > 29:
            break
        file.write(f'{word:}:{count:}')
        file.write('\n')
        i += 1

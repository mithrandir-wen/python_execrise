
'''针对txt文件中的关键字进行筛选，将输入句子的关键字全部换成**
   Written by mithrandir-wen'''

import nltk

PATH = "D:\python_workspace\word.txt"

sentence = input("Please input your sentence: ")
sentence_list = nltk.word_tokenize(sentence)

f = open(PATH, "r")
dirty_word_dict = {}
while True:
    
    dict_key = f.readline().rstrip("\n")
    if len(dict_key) == 0:
        print ("Dirty_word_dictionary is done")
        break
    else:
        dirty_word_dict[dict_key] = "**"
f.close()

new_sentence_list = [dirty_word_dict[x] if x in dirty_word_dict else x for x in sentence_list]
new_sentence = " ".join(new_sentence_list)
print (new_sentence)

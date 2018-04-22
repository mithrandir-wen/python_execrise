
'''从微信中爬取数据进行好友数据分析
   Written by mithrandir-wen'''

import itchat
import pandas
import re
import jieba

itchat.login()
friends = itchat.get_friends(update=True)[0:] 

def wechat_get_data(var):
    data_list = []
    for i in friends[1:]:
        data_list.append(i[var])
    return data_list

male = 0
female = 0
other = 0

sex_data_list = wechat_get_data("Sex")
for i in sex_data_list:
    if i == 1:
        male += 1
    elif i == 2:
        female += 1
    else:
        other += 1
total = len(sex_data_list)

print ("I have %d boys in my WeChat, about %.2f%%" %(male,float(male)/total*100))
print ("I have %d girls in my WeChat, about %.2f%%" %(female,float(female)/total*100))
print ("And %d unknown sex people exist in my Wechat, about %.2f%%" %(other,float(other/total*100)))

city_data_list = wechat_get_data("City")
nickname_data_list = wechat_get_data("NickName")
province_data_list = wechat_get_data("Province")
signature_data_list = wechat_get_data("Signature")

summary_data = {"Nickname":nickname_data_list,
                "Sex":sex_data_list,
                "City":city_data_list,
                "Province":province_data_list,
                "Signature":signature_data_list}

PATH = "D:\wechat_data.csv"

frame = pandas.DataFrame(summary_data)
frame.to_csv(PATH,index=True)

signature_new_list = []

for i in signature_data_list:
    signature = i.strip().replace("span","").replace("emoji","").replace("class","")
    pattern = re.compile("1f\d+\w*|[<>/=]")
    signature = pattern.sub("",signature)
    signature_new_list.append(signature)
signature_text = "".join(signature_new_list)

signature_wordlist = jieba.cut(signature_text)
signature_wordlist = " ".join(signature_wordlist)
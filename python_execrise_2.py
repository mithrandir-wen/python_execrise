
'''从微信中爬取数据进行好友数据分析
   Written by mithrandir-wen'''

import itchat

itchat.login()

friends = itchat.get_friends(update=True)[0:] 
#print (friends)

def wechat_get_data(var):
    city = []
    for i in friends[1:]:
        city.append(i[var])
    return city

male = 0
female = 0
other = 0

for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
total = len(friends[1:])

print ("I have %d boys in my WeChat, about %.2f%%" %(male,float(male)/total*100))
print ("I have %d girls in my WeChat, about %.2f%%" %(female,float(female)/total*100))
print ("And %d unknown sex people exist in my Wechat, about %.2f%%" %(other,float(other/total*100)))

'''for i in friends[1:]:
    sex = i["Sex"]
    name = i["NickName"]
    if sex != 1 and i != 2:
        print ("They are: {0}".format(name))'''

print (wechat_get_data("City"))


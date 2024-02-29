# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:12:49 2020
學習重點
1. 字串的應用，字串位置讀取，
6. 
@author: e010
"""

#字串相加
string7 = '01234'
string8 = '56789'
string9 = string7 + string8
print(string9)

#字串重複，python的特別用法。
string10 = string7 * 2
print(string10)

#讀取字串的位置
string11 = '零一二三四五六七八九十'
print('s=', string11, 's[0]=', string11[0])
print('s=', string11, 's[1]=', string11[1])
print('s=', string11, 's[-1]=', string11[-1])
print('s=', string11, 's[-2]=', string11[-2])
print('s=', string11, 's[:]=', string11[:])
print('s=', string11, 's[5:]=', string11[5:])
print('s=', string11, 's[-2:]=', string11[-2:])
print('s=', string11, 's[:5]=', string11[:5])
print('s=', string11, 's[:-2]=', string11[:-2])
print('s=', string11, 's[7:9]=', string11[7:9])
print('s=', string11, 's[-4:-1]=', string11[-4:-1])
print('s=', string11, 's[5:-2]=', string11[5:-2])
print('s=', string11, 's[2:10:2]=', string11[2:10:2])
print('s=', string11, 's[::-1]=', string11[::-1])
print('s=', string11, 's[-1::-1]=', string11[-1::-1])

'''****************************************************************************
上課練習，請自行設定一個字串，1. 找出第四個字元，2. 將字串順序倒過來呈現
***************************************************************************'''

#使用跳脫字元例如\n, \t來處理字串。
http://coscell.molerat.net/python/02escape.txt
#參考網址
string12 = '春眠不覺曉，處處聞啼鳥。\n\
夜來風雨聲，花落知多少。\n\
\t作者"孟浩然" 詩名"春曉"'
print(string12)

#http://tw.gitbook.net/python/string_split.html
'''解釋說明
split()用來切割字串，預設兩個參數，
split(str="", 行數)
使用str=""作為分隔符(如果未指定預設為空格)，
'''
#第一種
string13="""春眠不覺曉 
處處聞啼鳥，
夜來風雨聲，
花落知多少。"""
#使用逗點分格
list13=string13.split()
print(list13)
#第二種
string13="""春眠不覺曉 
處處聞啼鳥，
夜來風雨聲，
花落知多少。"""
#使用逗點分格
list13=string13.split('，')
print(list13)#\n代表換行符號
#將分割的字串還原，以上的例子常用在處理地址、姓名等
string14='，'.join(list13)
print(string14)
#字串取代，將字串的春用冬來代替
string15=string13.replace('春','冬')
print(string15)
'''****************************************************************************
上課練習，請自行找一個字A用字B來取代
***************************************************************************'''
#介紹find函數、rfind函數。
#用法:找出某一個字串在整個字串的位置
#這邊的位置是描述從字串0到最後一個字n當中的位置編號
print("string13", string13, '在string13的', string13.find('花落'), '位置發現"花落"')
#找出某一個字串在從最右邊尋找整個字串的位置，比較rfind與find的差異
print("string13為", string13, '在string13中從右邊數過來第一個出現"處"的位置為', string13.find('處'))
print("string13為", string13, '在string13中從右邊數過來第一個出現"處"的位置為', string13.rfind('處'))
#檢查春眠是不是字串開頭
print(string13.startswith('春眠'))
#檢查多少。是不是字串結尾
print(string13.endswith('多少。'))
'''***************************************************************************
上課練習，請自行判斷不覺曉是不是字串的開頭，風雨聲是不是字串的結尾。
***************************************************************************'''
print('string13=', string13,"string13.count('處')等於", string13.count('處'))
#移動字串在左邊右邊中間
string16='春眠不覺曉'
print(string16.center(10))
print(string16.rjust(10))
print(string16.ljust(10))

#調整字串的大寫小寫或是大寫變小寫小寫變大寫
string17='An Apple a day.'
#調整字串只有開頭為大寫
print(string17.capitalize())
#調整字串每一個字母開頭為大寫
print(string17.title())
#調整字串大寫變小寫小寫變大寫
print(string17.swapcase())
#調整字串全部大寫
print(string17.upper())
#調整字串全部小寫
print(string17.lower())

#讓字串長度等長不足的長度補0
string18='123'
print(string18.zfill(5))

#移動字串在左邊右邊中間
string19=' HeHllo,Mary.  '
#將空白拿掉
print(string19.strip())
#將最左邊的特定字元X拿掉，這邊H為例
print(string19.lstrip(' H'))
#將最右邊的特定字元X拿掉，這邊H為例 .
print(string19.rstrip(' .'))
#==============================================================================

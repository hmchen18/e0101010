# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:38:02 2020

@author: e010
Spyder Editor
1. 寫程式記得要練習寫註解。
2. 學會不同的容器使用，容器代表程式語言不同存放變數的方法
3. 容器類型:Tuple-小括號，list-中括號，dictionary-大括號成對，集合-大括號不成對
4. while迴圈的初次介紹與隨機變數的使用。
5. 在程式語言如何定義一個函數。
"""

"""
第一種容器Tuple元組，使用小括號來儲存元素。
"""
'''=======================Tuple====================================='''

Tuple1 = ()
print(Tuple1)

#第一種用法
#可以使用括號也可以不使用括號
Tuple2 = 1, 2 ,3
print(Tuple2)
#第二種用法
Tuple3 = (1, 2, 3)
print(Tuple3)

#提取某一個元素
print(Tuple3[0])

Tuple3 = (1, 2, 3)
#將變數指定為tulpe的值
a, b, c= Tuple3
print('a=', a, ',b=', b, ',c=', c)
#變數對調
a = 10
b = 20
print('交換前','a=', a, ',b=', b)
a, b = b, a
print('交換後','a=', a, ',b=', b)
#型態的轉換，需要按照程式語言的定義，因此不一定每一種型態都可以輕易轉換，
#在寫程式的時候，方便簡單可以執行出結果為原則。
#list轉為tuple
list1=[1,2,3,4]
Tuple4 = tuple(list1)
print(Tuple4)
#巢狀概念:Tuple包含Tuple中，
Tuple4 = (1,2,3,4)
Tuple5 = (Tuple4,5,6)
print(Tuple5)

#len函數為計算容器的大小，並將結果透由print顯示
print(len(Tuple5))

print(Tuple5[0][0])

'''************************************************************************
上課練習，請使用變數Tuple5 回答以下兩題 1. 找出Tuple5[0][2]，2. 找出Tuple5[1][1]
比較兩者的差異。
***************************************************************************'''
#可以包含空白
Tuple6 = ('z', )
print(Tuple6)


"""
第二種容器list串列，使用中括號來儲存元素。
"""
'''=======================list====================================='''
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨', 5]
print('購物清單shoplist為')
print(shoplist)

#顯示list中的某一個元素，此處為0
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
print('顯示shoplist[0]為',shoplist[0])

#顯示list中的長度:len(變數)
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
print('購物清單shoplist的長度為', len(shoplist))

#改變list中的蛋變為皮蛋
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
shoplist[1] = '皮蛋'
print("執行 shoplist[1] = '皮蛋' 後")
print(shoplist)

#改變list中的某個值的編號
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
index=shoplist.index('咖啡豆')
print("執行 index=shoplist.index('咖啡豆') 後")
print('index=', index)

#list中的加入某個元素在最後面
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
shoplist.append('麵包')
print("執行 shoplist.append('麵包')後")
print(shoplist)

#list中插入某個元素在指定的位置後面
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
shoplist.insert(4, '蘋果')
print("執行 shoplist.insert(4, '蘋果') 後")
print(shoplist)

#list中移除某一個元素
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
shoplist.remove('蛋')
print("執行 shoplist.remove('蛋') 後")
print(shoplist)

#使用del的內建函數刪除掉某一個list值
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
del shoplist[0]
print("執行 del shoplist[0] 後")
print(shoplist)
#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
shoplist.pop(0)
print("執行 shoplist.pop(0) 後")
print(shoplist)

#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
shoplist.pop()
print("執行 shoplist.pop() 後")
print(shoplist)

#pop() 函数用于移除列表中的特定元素。
shoplist.pop(-1)
print("執行 shoplist.pop(-1) 後")
print(shoplist)

#排序按照字典順序
shoplist = ['milk', 'egg', 'coffee', 'watermelon']
shoplist.sort()
print("執行 shoplist.sort() 後")
print(shoplist)

#串列可以包含各種資料型別的元素
list = [1,2.0,3,'Python']
print("串列可以包含各種資料型別的元素")
print(list)

#串列可以透由迴圈顯示出個別元素
shoplist = ['milk', 'egg', 'coffee', 'watermelon']
for item in shoplist:
    print(item)
"""
第三種容器dict字典，使用大括號來儲存成對的元素，類似x:y，x表示你的指令，y結果。
"""
'''=======================dict====================================='''
dict1={}
print(dict1)

lang={'早安':'Good Morning', '你好':'Hello'}
print(lang)

lang={'早安':'Good Morning', '你好':'Hello'}
print('「你好」的英文為',lang['你好'])
#錯誤範例，如果設錯參數救無法執行。
lang={'早安':'Good Morning', '你好':'Hello'}
print('「你好嗎」的英文為',lang['你好嗎'])

lang={'早安':'Good Morning', '你好':'Hello'}

lang1={'早安':'Good Morning', '你好':'Hello','你好嗎':'Hello 2'}
#指定第2個字典元素
print('「你好」的英文為',lang1.get('你好'))
#指定第3個字典元素
print('「你好嗎」的英文為',lang1.get('你好嗎'))
#指定非字典元素
print('「你好嗎」的英文為',lang1.get('你好11嗎','不在字典內'))
#改變字典裡面的值
lang={'早安':'Good Morning', '你好':'Hello'}
lang['你好']='Hi'
print(lang)
#增加字典裡面新的元素
lang['學生']='Student'
print(lang)
#刪除字典元素
lang={'早安':'Good Morning', '你好':'Hello'}
del lang['早安']
print(lang)
#清空字典元素使用clear指令
lang={'早安':'Good Morning', '你好':'Hello'}
lang.clear()
print(lang)

"""範例指定字典元素，並透過鍵盤輸入。
鍵盤輸入的指令為:input(描述字串)
"""
lang['早安']='Good Morning'
lang['你好']='Hello'
lang['學生']='Student'
a = input("input:")
print('你輸入的字串為',a,'English word is',lang.get(a))

'''************************************************************************
上課練習，請自行定一個字典，並至少有三個不同的元素類似
lang['定義1']='對映的值1'
lang['定義2']='對映的值2'
lang['定義3']='對映的值3'
print(你的結果)
***************************************************************************'''


'''=======================set====================================='''
#集合
setempty={0}
set1 = {1,2,3,4}
print(set1)
#集合可以存放文字與數字
set2 = set(('a',1,'b',2))
print(set2)
#集合只會顯示不重複的元素
set3 = set(['apple', 'banana', 'apple'])
print(set3)

set4 = set({'早安':'Good Morning', '你好':'Hello'})
print(set4)
set5 = set('racecar')
print(set5)
#將字串轉變成集合的元素
set6 = set('tiger')
print(set6)
#增加集合的元素
set6.add('z')
print(set6)
#移除集合的元素
set6.remove('t')
print(set6)

''' ======================= python的應用 丟骰子使用while迴圈 ======================= '''
#載入隨機函數庫
import random

#模擬丟骰子設定最小值1
min = 1
#模擬丟骰子設定最大值6
max = 6
#要不要繼續骰骰子，yes or y都代表要骰骰子
roll_again = "yes"
#yes or y都代表要骰骰子
while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))
    roll_again = input("Roll the dices again?")
#函數範例，定義一個函數來畫出圖形來。
#早期電腦螢幕畫圖都是透過這樣的函數來畫圖，現在已經進階到透過更簡單的指令控制了。
#原理還是一樣喔
def triangle(n): 
      
    # 設定多少個空格
    k = 2*n - 2
  
    # 外部迴圈處理列數
    for i in range(0, n): 
      
        # 內迴圈處理空格數目
        for j in range(0, k): 
            print(end=" ") 
      
        # 每個循環後遞減k
        k = k - 1
      
         # 內迴圈處理行的位置
        for j in range(0, i+1): 
          
            # 列印出符號*，此處可以用不同符號代替，比如ABC
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 10
triangle(n) 
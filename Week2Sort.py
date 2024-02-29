# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:30:05 2020
程式語言的基礎應用，資料排序的方法。
任何資料都會需要用到排序，因此如何透過程式語言讓資料可以排序，很常用來研究的一個方法。
我們舉例排序法，是讓同學可以知道，原來程式語言的基礎是可以這樣。
而因為我們剛開始學習，因此要先訓練語法為主，進一步有基本語法，下半學期我們會介紹比較多的使用。
@author: User
"""
'''定義一個泡沫排序法'''
def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swappedFlag = True#初始交換旗標判斷為真
    while swappedFlag:#使用迴圈
        swappedFlag = False#交換旗標判斷為False讓程式可以執行
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:#如果條件成立則執行下列結果，將nums[i + 1], nums[i]資料做交換
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # 將旗標設回True，執行下一次迴圈，直到都排序結束，則不用設定
                swappedFlag = True


# 範例檢驗
random_list_of_nums = [5, 2, 1, 8, 4]#定義一個亂數的串列list
bubble_sort(random_list_of_nums)#使用函數
print(random_list_of_nums)#列印結果

#載入隨機函數的工具
import random
#從1到100的數中，抽取十個隨機亂數。
SortData=random.sample(range(1,100), 10)
print('未排序前\r\n',SortData)
bubble_sort(SortData)
print('排序後\r\n',SortData)

"""
上課練習:
    請使用上述的程式，從50到999，抽取5個隨機數，並且使用bubble_sort來排序。
"""


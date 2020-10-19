#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for i in range(2):
    try:
        number = int(input("文字列を入力してください:"))
    except ValueError:
        print("エラー：数字で入力してください")
    else:
        print("あなたの好きな数字は",number,"です")


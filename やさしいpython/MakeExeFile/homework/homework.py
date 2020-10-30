#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import msvcrt
import sys

while True:
    for i in range(2):
        try:
            number = int(input("文字列を入力してください:"))
        except ValueError:
            print("エラー：数字で入力してください")
        else:
            print("あなたの好きな数字は",number,"です")
    print("終了するにはescを押してください。")
        
    ch = ord(msvcrt.getch())
    if ch == 27:
        sys.exit()


# In[ ]:





# In[ ]:





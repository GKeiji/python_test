# -*- coding: utf-8 -*-
from selenium import webdriver
import pandas

"""***************************************
�����̐ݒ�
***************************************"""
browser = webdriver.Chrome(executable_path='/mnt/c/workspace/pydev/chromedriver.exe') 
df = pandas.read_csv('default.csv', index_col=0) #���D���E���D�̉摜URL����ɓ����Ă���
url = "http://wav.tv/actresses/" #�G���T�C�g�̏��D���X�g�̃y�[�W

"""******************************
CSS SELECTOR�̐ݒ�
******************************"""

PAGER_NEXT = "a.m-pagination--next.is-last.step" #���փ{�^��
POSTS = "div.m-actress-wrap"
ACTRESS_NAME = ".m-actress--title" #���D��
IMAGE = ".m-actress--thumbnail-img img" #�T���l�C���摜��URL�Asrc�ŉ摜�t�@�C����擾�ł���

"""***************************************
���s����
***************************************"""

browser.get(url)

while True: #continue until getting the last page

   #5-1

   if len(browser.find_elements_by_css_selector(PAGER_NEXT)) > 0:
       print("Starting to get posts...")
       posts = browser.find_elements_by_css_selector(POSTS) #�y�[�W��̃^�C�g������
       print (len(posts))
       for post in posts:
           try:
               name = post.find_element_by_css_selector(ACTRESS_NAME).text
               print(name)
               thumnailURL = post.find_element_by_css_selector(IMAGE).get_attribute("src")
               print(thumnailURL)
               se = pandas.Series([name,thumnailURL],["name", "image"])    
               df = df.append(se, ignore_index=True)
           except Exception as e:
               print(e)

       btn = browser.find_element_by_css_selector(PAGER_NEXT).get_attribute("href")
       print("next url:{}".format(btn))
       browser.get(btn)
       print("Moving to next page......")
   else:
       print("no pager exist anymore")
       break
#6
print("Finished Scraping. Writing CSV.......")
df.to_csv("output.csv")
print("DONE")
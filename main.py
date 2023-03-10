# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import os
import random




# browser = webdriver.Chrome(executable_path=r"/Users/vladislav/Downloads/")

import undetected_chromedriver.v2 as uc
import random,time,os,sys
from selenium.webdriver.common.keys import Keys




GMAIL = 'vlad5brykov@gmail.com'
PASSWORD = 'ViperZS200'

chrome_options = uc.ChromeOptions()

chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument("--disable-popup-blocking")

chrome_options.add_argument("--profile-directory=Default")

chrome_options.add_argument("--ignore-certificate-errors")

chrome_options.add_argument("--disable-plugins-discovery")

chrome_options.add_argument("--incognito")

chrome_options.add_argument("user_agent=DN")

driver = uc.Chrome(options=chrome_options)

driver.delete_all_cookies()

driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
time.sleep(5)

driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(GMAIL)
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(Keys.RETURN)
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button' ).click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(PASSWORD)
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button' ).click()
time.sleep(5)

driver.get('https://www.youtube.com/watch?v=66_r-7t3ot0')
time.sleep(5)
driver.execute_script("window.scrollTo(0, 400);")
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, 'ytd-comments ytd-comment-simplebox-renderer div#placeholder-area' ).click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="contenteditable-root"]' ).send_keys("Очень интересно")
driver.find_element(By.XPATH, '//*[@id="contenteditable-root"]' ).send_keys(Keys.CONTROL, Keys.ENTER)

time.sleep(2)



# creation-box
# driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div[2]/div/div[2]/tp-yt-paper-input-container/div[2]/div/div[1]/ytd-emoji-input/yt-user-mention-autosuggest-input/yt-formatted-string/div' ).send_keys(PASSWORD)

# /html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div[2]/div/div[2]/tp-yt-paper-input-container/div[2]/div/div[1]/ytd-emoji-input/yt-user-mention-autosuggest-input/yt-formatted-string/div

time.sleep(100)


# browser = webdriver.Safari()
# browser.get('https://www.olx.ua/d/post-new-ad/?bs=homepage_adding')

# browser = webdriver.Chrome()

# browser.get('https://www.youtube.com/watch?v=Frazx5zxScE')
# time.sleep(5)
# browser.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div').click()
# time.sleep(2)
# browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys("vlad5brykov@gmail.com")
# time.sleep(2)
# browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button' ).click()
#
# time.sleep(2000)
#
# browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input').send_keys("vlad5brykov@gmail.com")
# browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input').send_keys("Vladislav5")
#
# browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button' ).click()
#
# time.sleep(20)
          

#########################################################                      Харьков
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################


# browser.get('https://www.olx.ua/d/post-new-ad/')
#
# time.sleep(20)
#
# path_images = "/Users/vladislav/Desktop/kat_1/"
#
# images = os.listdir(path_images)
# r1 = random.choice(images)
# r2 = random.choice(images)
# r3 = random.choice(images)
# r4 = random.choice(images)
# r5 = random.choice(images)
# r6 = random.choice(images)
# r7 = random.choice(images)
# r8 = random.choice(images)
# img1 = "/Users/vladislav/Desktop/kat_1/" + r1
# img2 = "/Users/vladislav/Desktop/kat_1/" + r2
# img3 = "/Users/vladislav/Desktop/kat_1/" + r3
# img4 = "/Users/vladislav/Desktop/kat_1/" + r4
# img5 = "/Users/vladislav/Desktop/kat_1/" + r5
# img6 = "/Users/vladislav/Desktop/kat_1/" + r6
# img7 = "/Users/vladislav/Desktop/kat_1/" + r7
# img8 = "/Users/vladislav/Desktop/kat_1/" + r8
#
# time.sleep(20)
#
#
# # browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[2]/div/div/div/div/div[1]/input').send_keys(img1 + "\n" + img2 + "\n" + img3 + "\n" + img4 + "\n" + img5+ "\n" + img6 + "\n" + img7 + "\n" + img8)
#
# # time.sleep(10)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div').click()
#
# time.sleep(20)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div/div[2]/section/ul/button[6]/div/div[2]/p').click()
#
# time.sleep(7)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div/div[2]/div/section[2]/ul/li[3]/div/section/p').click()
#
# time.sleep(5)
#
# # Чтоб вводило русский текст
# elem = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[1]/div/div/div[1]/div/textarea')
# elem.send_keys(u"Котенок мальчики девочка вислоухий котенок, котята фолд ")
#
# time.sleep(7)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[2]/div/div/div/div/div[1]/input').send_keys(img1 + "\n" + img2 + "\n" + img3 + "\n" + img4 + "\n" + img5+ "\n" + img6 + "\n" + img7 + "\n" + img8)
#
# time.sleep(10)
#
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[3]/div/div[1]/div/div/div/textarea')
# about.send_keys(u"Котята от чистокровных породистых родителей. Красивый окрас. Без паразитов. Мальчик и девочка, одинаковые. Максимально качественные котята. Не шерсть, а пушек. Очень плотный, котенок медвеженок. Окрас равномерный, посторонних цветов нет. Ушки полностью прижаты к голове. Характер очень нежный, любвеобильная лапочка кошка. Не шкодит, не гадит, очень смышленная. Все запоминает с первого раза. Когти только об когтеточку. Лоток без промахов. Всегда хочет быть рядом (социальный) Мальчик Котята имеют плюшевую шубку (не жесткая шерсть) Вообщем, останетесь довольны. Возраст 2 месяца В Харьков привезу на жд вокзал, Оплата при получении котёнка в руки.")
#
# time.sleep(6)
# browser.execute_script("window.scrollTo(0, 1000);")
# time.sleep(6)
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[1]/div/div/div/div/div[1]/div/div/input')
# about.send_keys(u"1300")
# time.sleep(10)
# browser.execute_script("window.scrollTo(0, 1400);")
#
# time.sleep(7)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[1]/div/div/div[1]/button').click()
# browser.execute_script("window.scrollTo(0, 1400);")
#
# time.sleep(2)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/a').click()
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/ul/div/li[26]/a').click()
#
# time.sleep(6)
# browser.execute_script("window.scrollTo(0, 1800);")
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[2]/div/div/div/div/div/div/div/div/div/input')
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# time.sleep(6)
# about.send_keys(u"Харьков ")
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[2]/div/div/div/div/div/div[2]/li[9]').click()
#
# time.sleep(6)
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[5]/div/div/div/div/input')
# about.send_keys("0665778722")
#
# #опубликовать
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[6]/div/button[2]').click()
#
#
# #без рекламы
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div[1]/section/div[1]/ul/li[1]/div/div[3]/a[2]').click()


################

# time.sleep(600)
# #########################################################                     Днепр
# ##################################################################################################################
# ##################################################################################################################
# ##################################################################################################################
# ##################################################################################################################
# ##################################################################################################################
# ##################################################################################################################
#
#
# browser.get('https://www.olx.ua/d/post-new-ad/')
#
# time.sleep(20)
#
# path_images = "/Users/vladislav/Desktop/kat_1/"
#
# images = os.listdir(path_images)
# r1 = random.choice(images)
# r2 = random.choice(images)
# r3 = random.choice(images)
# r4 = random.choice(images)
# r5 = random.choice(images)
# r6 = random.choice(images)
# r7 = random.choice(images)
# r8 = random.choice(images)
# img1 = "/Users/vladislav/Desktop/kat_1/" + r1
# img2 = "/Users/vladislav/Desktop/kat_1/" + r2
# img3 = "/Users/vladislav/Desktop/kat_1/" + r3
# img4 = "/Users/vladislav/Desktop/kat_1/" + r4
# img5 = "/Users/vladislav/Desktop/kat_1/" + r5
# img6 = "/Users/vladislav/Desktop/kat_1/" + r6
# img7 = "/Users/vladislav/Desktop/kat_1/" + r7
# img8 = "/Users/vladislav/Desktop/kat_1/" + r8
#
# time.sleep(20)
#
#
# # browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[2]/div/div/div/div/div[1]/input').send_keys(img1 + "\n" + img2 + "\n" + img3 + "\n" + img4 + "\n" + img5+ "\n" + img6 + "\n" + img7 + "\n" + img8)
#
# # time.sleep(10)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div').click()
#
# time.sleep(20)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div/div[2]/section/ul/button[6]/div/div[2]/p').click()
#
# time.sleep(7)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div/div[2]/div/section[2]/ul/li[3]/div/section/p').click()
#
# time.sleep(5)
#
# # Чтоб вводило русский текст
# elem = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[1]/div/div/div[1]/div/textarea')
# elem.send_keys(u"Котята вислоухие мальчик и девочка шотландские, котенок фолд ")
#
# time.sleep(7)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[2]/div/div/div/div/div[1]/input').send_keys(img1 + "\n" + img2 + "\n" + img3 + "\n" + img4 + "\n" + img5+ "\n" + img6 + "\n" + img7 + "\n" + img8)
#
# time.sleep(10)
#
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[3]/div/div[1]/div/div/div/textarea')
# about.send_keys(u"Котята от чистокровных шотландских породистых родителей. Красивый окрас. Без паразитов. Мальчик и девочка, Выглядят одиноково. Мальчик немного крупнее. Максимально качественный котёнок. Не шерсть, а пушек. Очень плотный, котенок медвеженок. Окрас равномерный, посторонних цветов нет. Ушки полностью прижаты к голове. Характер очень нежный, любвеобильная лапочка кошка. Не шкодит, не гадит, очень смышленная. Все запоминает с первого раза. Когти только об когтеточку. Лоток без промахов. Всегда хочет быть рядом (социальный) Мальчик Котята имеют плюшевую шубку (не жесткая шерсть) Вообщем, останетесь довольны. Возраст 2 месяца В Днепр привезу на жд вокзал, Оплата при получении котёнка в руки.")
#
# time.sleep(6)
# browser.execute_script("window.scrollTo(0, 1000);")
# time.sleep(6)
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[1]/div/div/div/div/div[1]/div/div/input')
# about.send_keys(u"1300")
# time.sleep(10)
# browser.execute_script("window.scrollTo(0, 1400);")
#
# time.sleep(7)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[1]/div/div/div[1]/button').click()
# browser.execute_script("window.scrollTo(0, 1400);")
#
# time.sleep(2)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/a').click()
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/ul/div/li[26]/a').click()
#
# time.sleep(6)
# browser.execute_script("window.scrollTo(0, 1800);")
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[2]/div/div/div/div/div/div/div/div/div/input')
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# time.sleep(6)
# about.send_keys(u"Днепр ")
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[2]/div/div/div/div/div/div[2]/li[7]').click()
#
# time.sleep(6)
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[5]/div/div/div/div/input')
# about.send_keys("0665778722")
#
# #опубликовать
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[6]/div/button[2]').click()
#
#
# #без рекламы
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div[1]/section/div[1]/ul/li[1]/div/div[3]/a[2]').click()
#
#
# time.sleep(600)
#
# ########################################################                      Одесса
# #################################################################################################################
# #################################################################################################################
# #################################################################################################################
# #################################################################################################################
# #################################################################################################################
#
#
# browser.get('https://www.olx.ua/d/post-new-ad/')
#
# time.sleep(20)
#
# path_images = "/Users/vladislav/Desktop/kat_1/"
#
# images = os.listdir(path_images)
# r1 = random.choice(images)
# r2 = random.choice(images)
# r3 = random.choice(images)
# r4 = random.choice(images)
# r5 = random.choice(images)
# r6 = random.choice(images)
# r7 = random.choice(images)
# r8 = random.choice(images)
# img1 = "/Users/vladislav/Desktop/kat_1/" + r1
# img2 = "/Users/vladislav/Desktop/kat_1/" + r2
# img3 = "/Users/vladislav/Desktop/kat_1/" + r3
# img4 = "/Users/vladislav/Desktop/kat_1/" + r4
# img5 = "/Users/vladislav/Desktop/kat_1/" + r5
# img6 = "/Users/vladislav/Desktop/kat_1/" + r6
# img7 = "/Users/vladislav/Desktop/kat_1/" + r7
# img8 = "/Users/vladislav/Desktop/kat_1/" + r8
#
# time.sleep(20)
#
#
# # browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[2]/div/div/div/div/div[1]/input').send_keys(img1 + "\n" + img2 + "\n" + img3 + "\n" + img4 + "\n" + img5+ "\n" + img6 + "\n" + img7 + "\n" + img8)
#
# # time.sleep(10)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div').click()
#
# time.sleep(20)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div/div[2]/section/ul/button[6]/div/div[2]/p').click()
#
# time.sleep(7)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div/div[2]/div/section[2]/ul/li[3]/div/section/p').click()
#
# time.sleep(5)
#
# # Чтоб вводило русский текст
# elem = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[1]/div/div/div[1]/div/textarea')
# elem.send_keys(u"Котята 2 мес мальчик и девоча вислоухие, котенок на подарок")
#
# time.sleep(7)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[2]/div/div/div/div/div[1]/input').send_keys(img1 + "\n" + img2 + "\n" + img3 + "\n" + img4 + "\n" + img5+ "\n" + img6 + "\n" + img7 + "\n" + img8)
#
# time.sleep(10)
#
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[3]/div/div[1]/div/div/div/textarea')
# about.send_keys(u"Котята от чистокровных породистых родителей. Ушки плотно прижаты к голове (не самолеты) Красивый окрас. Без паразитов. Максимально качественный котёнок. Не шерсть, а пушек. Очень плотный, котенок медвеженок. Окрас равномерный, посторонних цветов нет. Ушки полностью прижаты к голове. Характер очень нежный, любвеобильная лапочка кошка. Не шкодит, не гадит, очень смышленная. Все запоминает с первого раза. Когти только об когтеточку. Лоток без промахов. Всегда хочет быть рядом (социальный) Мальчик Котята имеют плюшевую шубку (не жесткая шерсть) Вообщем, останетесь довольны. Возраст 2 месяца В Харьков привезу на жд вокзал, Оплата при получении котёнка в руки.")
#
# time.sleep(6)
# browser.execute_script("window.scrollTo(0, 1000);")
# time.sleep(6)
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[1]/div/div/div/div/div[1]/div/div/input')
# about.send_keys(u"1300")
# time.sleep(10)
# browser.execute_script("window.scrollTo(0, 1400);")
#
# time.sleep(7)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[1]/div/div/div[1]/button').click()
# browser.execute_script("window.scrollTo(0, 1400);")
#
# time.sleep(2)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/a').click()
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/ul/div/li[26]/a').click()
#
# time.sleep(6)
# browser.execute_script("window.scrollTo(0, 1800);")
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[2]/div/div/div/div/div/div/div/div/div/input')
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# time.sleep(6)
# about.send_keys(u"Одесса ")
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[2]/div/div/div/div/div/div[2]/li[3]').click()
#
# time.sleep(6)
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[5]/div/div/div/div/input')
# about.send_keys("0665778722")
#
# #опубликовать
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[6]/div/button[2]').click()
#
#
# #без рекламы
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div[1]/section/div[1]/ul/li[1]/div/div[3]/a[2]').click()
#
#
# ################
#
# time.sleep(600)
# #########################################################                      Киев
# ##################################################################################################################
# ##################################################################################################################
# ##################################################################################################################
# ##################################################################################################################
# ##################################################################################################################
#
#
# browser.get('https://www.olx.ua/d/post-new-ad/')
#
# time.sleep(20)
#
# path_images = "/Users/vladislav/Desktop/kat_1/"
#
# images = os.listdir(path_images)
# r1 = random.choice(images)
# r2 = random.choice(images)
# r3 = random.choice(images)
# r4 = random.choice(images)
# r5 = random.choice(images)
# r6 = random.choice(images)
# r7 = random.choice(images)
# r8 = random.choice(images)
# img1 = "/Users/vladislav/Desktop/kat_1/" + r1
# img2 = "/Users/vladislav/Desktop/kat_1/" + r2
# img3 = "/Users/vladislav/Desktop/kat_1/" + r3
# img4 = "/Users/vladislav/Desktop/kat_1/" + r4
# img5 = "/Users/vladislav/Desktop/kat_1/" + r5
# img6 = "/Users/vladislav/Desktop/kat_1/" + r6
# img7 = "/Users/vladislav/Desktop/kat_1/" + r7
# img8 = "/Users/vladislav/Desktop/kat_1/" + r8
#
# time.sleep(20)
#
#
# # browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[2]/div/div/div/div/div[1]/input').send_keys(img1 + "\n" + img2 + "\n" + img3 + "\n" + img4 + "\n" + img5+ "\n" + img6 + "\n" + img7 + "\n" + img8)
#
# # time.sleep(10)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div').click()
#
# time.sleep(20)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div/div[2]/section/ul/button[6]/div/div[2]/p').click()
#
# time.sleep(7)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div/div[2]/div/section[2]/ul/li[3]/div/section/p').click()
#
# time.sleep(5)
#
# # Чтоб вводило русский текст
# elem = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[1]/div/div/div[1]/div/textarea')
# elem.send_keys(u"Котенок девочка и парень вислоухие шотландские, котята фолд ")
#
# time.sleep(7)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[2]/div/div/div/div/div[1]/input').send_keys(img1 + "\n" + img2 + "\n" + img3 + "\n" + img4 + "\n" + img5+ "\n" + img6 + "\n" + img7 + "\n" + img8)
#
# time.sleep(10)
#
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[3]/div/div[1]/div/div/div/textarea')
# about.send_keys(u"Котята от чистокровных породистых родителей. Красивый окрас. Без паразитов. Мальчик. Максимально качественный котёнок. Не шерсть, а пушек. Очень плотный, котенок медвеженок. Окрас равномерный, посторонних цветов нет. Ушки полностью прижаты к голове. Характер очень нежный, любвеобильная лапочка кошка. Не шкодит, не гадит, очень смышленная. Все запоминает с первого раза. Когти только об когтеточку. Лоток без промахов. Всегда хочет быть рядом (социальный) Мальчик Котята имеют плюшевую шубку (не жесткая шерсть) Вообщем, останетесь довольны. Возраст 2 месяца В Харьков привезу на жд вокзал, Оплата при получении котёнка в руки.")
#
# time.sleep(6)
# browser.execute_script("window.scrollTo(0, 1000);")
# time.sleep(6)
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[1]/div/div/div/div/div[1]/div/div/input')
# about.send_keys(u"1300")
# time.sleep(10)
# browser.execute_script("window.scrollTo(0, 1400);")
#
# time.sleep(7)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[1]/div/div/div[1]/button').click()
# browser.execute_script("window.scrollTo(0, 1400);")
#
# time.sleep(2)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/a').click()
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/ul/div/li[26]/a').click()
#
# time.sleep(6)
# browser.execute_script("window.scrollTo(0, 1800);")
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[2]/div/div/div/div/div/div/div/div/div/input')
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# time.sleep(6)
# about.send_keys(u"Киев ")
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/div/div/div/div/div/div[2]/li[10]').click()
#
# time.sleep(6)
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[5]/div/div/div/div/input')
# about.send_keys("0665778722")
#
# #опубликовать
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[6]/div/button[2]').click()
#
#
# #без рекламы
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div[1]/section/div[1]/ul/li[1]/div/div[3]/a[2]').click()
#
#
# ################
#
#
#
# time.sleep(600)
# #########################################################                      Николаев
# ##################################################################################################################
# ##################################################################################################################
# ##################################################################################################################
# ##################################################################################################################
# ##################################################################################################################
#
#
# browser.get('https://www.olx.ua/d/post-new-ad/')
#
# time.sleep(20)
#
# path_images = "/Users/vladislav/Desktop/kat_1/"
#
# images = os.listdir(path_images)
# r1 = random.choice(images)
# r2 = random.choice(images)
# r3 = random.choice(images)
# r4 = random.choice(images)
# r5 = random.choice(images)
# r6 = random.choice(images)
# r7 = random.choice(images)
# r8 = random.choice(images)
# img1 = "/Users/vladislav/Desktop/kat_1/" + r1
# img2 = "/Users/vladislav/Desktop/kat_1/" + r2
# img3 = "/Users/vladislav/Desktop/kat_1/" + r3
# img4 = "/Users/vladislav/Desktop/kat_1/" + r4
# img5 = "/Users/vladislav/Desktop/kat_1/" + r5
# img6 = "/Users/vladislav/Desktop/kat_1/" + r6
# img7 = "/Users/vladislav/Desktop/kat_1/" + r7
# img8 = "/Users/vladislav/Desktop/kat_1/" + r8
#
# time.sleep(20)
#
#
# # browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[2]/div/div/div/div/div[1]/input').send_keys(img1 + "\n" + img2 + "\n" + img3 + "\n" + img4 + "\n" + img5+ "\n" + img6 + "\n" + img7 + "\n" + img8)
#
# # time.sleep(10)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div').click()
#
# time.sleep(20)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div/div[2]/section/ul/button[6]/div/div[2]/p').click()
#
# time.sleep(7)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[2]/div/div[2]/div/section[2]/ul/li[3]/div/section/p').click()
#
# time.sleep(5)
#
# # Чтоб вводило русский текст
# elem = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[1]/div[1]/div/div/div[1]/div/textarea')
# elem.send_keys(u"Элитные котята фолд на подарок, мальчик и девочка котенок")
#
# time.sleep(7)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[2]/div/div/div/div/div[1]/input').send_keys(img1 + "\n" + img2 + "\n" + img3 + "\n" + img4 + "\n" + img5+ "\n" + img6 + "\n" + img7 + "\n" + img8)
#
# time.sleep(10)
#
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[3]/div/div[1]/div/div/div/textarea')
# about.send_keys(u"Котята от чистокровных породистых родителей. Красивый окрас. Плюшевая мягкая шерсть, Без паразитов. Мальчик более крупный, девчка поменьше. Максимально качественный котёнок. Не шерсть, а пушек. Очень плотный, котенок медвеженок. Окрас равномерный, посторонних цветов нет. Ушки полностью прижаты к голове. Характер очень нежный, любвеобильная лапочка кошка. Не шкодит, не гадит, очень смышленная. Все запоминает с первого раза. Когти только об когтеточку. Лоток без промахов. Всегда хочет быть рядом (социальный) Мальчик Котята имеют плюшевую шубку (не жесткая шерсть) Вообщем, останетесь довольны. Возраст 2 месяца В Харьков привезу на жд вокзал, Оплата при получении котёнка в руки.")
#
# time.sleep(6)
# browser.execute_script("window.scrollTo(0, 1000);")
# time.sleep(6)
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[1]/div/div/div/div/div[1]/div/div/input')
# about.send_keys(u"1300")
# time.sleep(10)
# browser.execute_script("window.scrollTo(0, 1400);")
#
# time.sleep(7)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[1]/div/div/div[1]/button').click()
# browser.execute_script("window.scrollTo(0, 1400);")
#
# time.sleep(2)
#
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/a').click()
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/ul/div/li[26]/a').click()
#
# time.sleep(6)
# browser.execute_script("window.scrollTo(0, 1800);")
#
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[2]/div/div/div/div/div/div/div/div/div/input')
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# about.send_keys(Keys.BACKSPACE)
# time.sleep(6)
# about.send_keys(u"Николаев ")
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[4]/div[2]/div/div/div/div/div/div[2]/li[5]').click()
#
# time.sleep(6)
# about = browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[5]/div[5]/div/div/div/div/input')
# about.send_keys("0665778722")
#
# #опубликовать
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div/div[1]/form/main/div[1]/div[6]/div/button[2]').click()
#
#
# #без рекламы
# time.sleep(6)
# browser.find_element(By.XPATH, '/html/body/div[1]/section/div[1]/ul/li[1]/div/div[3]/a[2]').click()
#
#
# ################
#
# time.sleep(20)
#
#
# print("hello world")






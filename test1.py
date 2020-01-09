from selenium import webdriver
from time import sleep
import time
import os
from selenium.webdriver.common.keys import Keys
import datetime
# from pywinauto import application
# from pywinauto import timings

browser = webdriver.Ie(r'C:\selenium-webguard\IEDriverServer.exe')
webguard_address = "10.0.113.29"
webguard_port = "12088"

browser.get("http://" + webguard_address + ":" + webguard_port) ##Login Page
# window_login = browser.window_handles[0]
login_title = browser.title
print(browser.title)
print(browser.current_window_handle)
print(browser.window_handles)
# print(browser.session_id)
 
input_id = browser.find_element_by_css_selector("#loginUserId") ##ID/PW 입력
input_pw = browser.find_element_by_css_selector("#loginPassword")

input_id.send_keys("admin")
input_pw.send_keys("qwerty0-")

browser.find_element_by_css_selector("#login_back > img").click()

time.sleep(10)
# window_watch = browser.window_handles[1]
# browser.switch_to.window(window_watch)
browser.switch_to.window(browser.window_handles[1])

# browser.get_window_position(browser.window_handles[1])
watch_title = browser.title
print(browser.title)

if watch_title == login_title:
    browser.switch_to.window(browser.window_handles[1])

print(browser.title)
print(browser.current_window_handle)
print(browser.window_handles)
# print(browser.session_id)

time.sleep(5) ##Live 화면 스크린샷
screenshot_name = "screenshots/watch.png"
browser.save_screenshot(screenshot_name)
time.sleep(3)

suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
os.rename("screenshots/watch.png", "screenshots/" + webguard_address + "_watch_" + suffix + ".png") ##스크린샷 저장
# os.rename("screenshots/watch.png", "screenshots/" + webguard_address + "_watch.png") ##스크린샷 저장
time.sleep(3)
print("Watch Screenshot(" + suffix + ") is done.")


watch_clock = browser.find_element_by_id("watch_clock") ##현재 시간 (Watch)
print (watch_clock.text)

user = browser.find_element_by_id("watch_user_id") ##User
print (user.text)

ipaddress = browser.find_element_by_id("watch_ipaddress") ##IP 주소
print (ipaddress.text)

version = browser.find_element_by_id("version") ##Webguard 버전 정보
print (version.get_attribute("title"))

# browser.switch_to.window(window_watch)
# time.sleep(5)

browser.find_element_by_css_selector("#function_search").click() ##Webguard Search
time.sleep(5)
saerch_title = browser.title
print(browser.title)

if saerch_title == watch_title:
    browser.find_element_by_id("function_search").click() 
# browser.find_element_by_id("function_search").click()
time.sleep(5)
# window_search = browser.window_handles[2]
# browser.switch_to.window(window_search)
print(browser.title)
print(browser.current_window_handle)
print(browser.window_handles)
# print(browser.session_id)

browser.find_element_by_id("search_btn_play").click() ##재생
time.sleep(20)

screenshot_name = "screenshots/search.png" ##Play 화면 스크린샷
browser.save_screenshot(screenshot_name)
time.sleep(3)

suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
os.rename("screenshots/search.png", "screenshots/" + webguard_address + "_search_" + suffix + ".png") ##스크린샷 저장
time.sleep(3)
print("Search Screenshot(" + suffix + ") is done.")

browser.find_element_by_id("search_btn_stop").click() ##정지

search_clock = browser.find_element_by_id("search_clock") ##현재 시간 (Search)
print (search_clock.text)

time.sleep(5)
browser.find_element_by_id("function_savemovie").click() ##clip-Copy 

from autoit import *

win_wait_active("[CLASS : #32770; TITLE : 저장 형식]", 200)
time.sleep(10)
control_click("[CLASS : #32770; TITLE : 저장 형식]", "Button1")

# sleep(5)
# browser.quit()





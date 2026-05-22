import time
from time import sleep

from pages.auth_page import AuthPage
from pages.home_page import HomePage
from pages.lessons_page import LessonsPage



def test_auth_chrome(driver_chrome):
    driver_chrome.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_chrome)
    auth_page.click_btn_uz()
    time.sleep(2)
    auth_page.enter_login('')
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password('')
    time.sleep(2)
    auth_page.click_btn_submit()
    time.sleep(3)
    try:
        auth_page.click_dropdown_session()
        time.sleep(2)
        auth_page.click_btn_finish()
        time.sleep(5)
    except:
        pass

    home_page = HomePage(driver_chrome)
    # home_page.click_video_instruction()
    # time.sleep(2)
    # home_page.click_btn_fullscreen()
    # time.sleep(10)
    # home_page.click_press_video()
    # time.sleep(2)
    # home_page.click_btn_pause()
    # time.sleep(2)
    # home_page.click_fullscreen_exit()
    # time.sleep(3)
    # home_page.click_logo()
    time.sleep(2)
    home_page.click_group_card()
    time.sleep(2)

    lessons_page = LessonsPage(driver_chrome)
    lessons_page.click_btn_lessons()
    time.sleep(2)
    lessons_page.click_lesson_card()
    time.sleep(2)
    lessons_page.click_btn_play_video()
    time.sleep(2)
    lessons_page.click_btn_fullscreen()
    time.sleep(10)
    lessons_page.click_press_video()
    time.sleep(2)
    lessons_page.click_btn_pause()
    time.sleep(2)
    lessons_page.click_fullscreen_exit()
    time.sleep(2)
    lessons_page.click_btn_back()
    time.sleep(2)

    home_page.click_profile_icon()
    time.sleep(2)
    home_page.click_btn_exit()
    time.sleep(2)
    home_page.click_btn_confirm_exit()


def test_invalid_auth_chrome(driver_chrome):
    driver_chrome.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_chrome)
    auth_page.click_btn_uz()
    time.sleep(2)
    auth_page.enter_login('')
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password('')
    time.sleep(2)
    auth_page.click_btn_submit()
    try:
        auth_page.click_dropdown_session()
        time.sleep(2)
        auth_page.click_btn_finish()
    except:
        pass


def test_auth_edge(driver_edge):
    driver_edge.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_edge)
    auth_page.click_btn_uz()
    time.sleep(2)
    auth_page.enter_login('')
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password('')
    time.sleep(2)
    auth_page.click_btn_submit()
    try:
        auth_page.click_dropdown_session()
        time.sleep(2)
        auth_page.click_btn_finish()
    except:
        pass

    home_page = HomePage(driver_edge)
    home_page.click_video_instruction()
    time.sleep(2)
    home_page.click_btn_fullscreen()
    time.sleep(10)
    home_page.click_press_video()
    time.sleep(2)
    home_page.click_btn_pause()
    time.sleep(2)
    home_page.click_fullscreen_exit()
    time.sleep(2)
    home_page.click_logo()
    time.sleep(2)
    home_page.click_group_card()
    time.sleep(2)

    lessons_page = LessonsPage(driver_edge)
    lessons_page.click_btn_lessons()
    time.sleep(2)
    lessons_page.click_lesson_card()
    time.sleep(2)
    lessons_page.click_btn_play_video()
    time.sleep(2)
    lessons_page.click_btn_fullscreen()
    time.sleep(10)
    lessons_page.click_press_video()
    time.sleep(2)
    lessons_page.click_btn_pause()
    time.sleep(2)
    lessons_page.click_fullscreen_exit()
    time.sleep(2)
    lessons_page.click_btn_back()
    time.sleep(2)

    home_page.click_profile_icon()
    time.sleep(2)
    home_page.click_btn_exit()
    time.sleep(2)
    home_page.click_btn_confirm_exit()




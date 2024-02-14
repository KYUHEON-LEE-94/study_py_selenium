from selenium import webdriver
from selenium.webdriver.common.by import By #HTML 요소 찾기
from selenium.webdriver.common.keys import Keys #엔터와 같은 특수키 사용
from selenium.webdriver.chrome.options import Options
import time

def login(browser, input_id, input_password):
    # ID 입력
    id_input = browser.find_element(By.ID, "id")
    id_input.send_keys(input_id)

    # 1초 대기
    time.sleep(2)

    # 비밀번호 입력
    pw_input = browser.find_element(By.ID, "psw")
    pw_input.send_keys(input_password)

        # 전송
    submit_button = browser.find_element(By.ID, "btn_login")
    submit_button.submit()

def check_alert(browser, input_id, input_password):
    # alert 확인
    try:
        alert = browser.switch_to.alert
        print("로그인 세션 만료 alert 확인")
        alert.accept()
        time.sleep(2)
        login(browser, input_id, input_password)
    except:
        print("정상 동작")

def setting_browser():
    user_agent = "user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # 불필요한 에러 메시지 없애기
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # user_agent 설정
    chrome_options.add_argument(user_agent)

    return chrome_options


def start_scrap():
    input_manage_site = input("관리자 사이트 url 입력: ")
    input_id = input("id 입력: ")
    input_password = input("password 입력: ")

    chrome_options = setting_browser()

    # 브라우저 생성
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(input_manage_site) 

    # 1초 대기
    time.sleep(2)

    login(browser, input_id, input_password)

    time.sleep(2)

    check_alert(browser, input_id, input_password)
    time.sleep(3) 

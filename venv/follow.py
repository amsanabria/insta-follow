import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run(username, passw, origin_username):

    #Set up the browser
    browser = webdriver.Chrome("C:\Chromedriver\chromedriver")
    browser.get('https://www.instagram.com/accounts/login/')

    #Accept cookies
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Aceptar todas']"))).click()

    #Login
    user_form = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    user_form.send_keys(username)
    browser.find_element_by_xpath("//input[@name=\"password\"]").send_keys(passw)
    browser.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[3]/button").click()

    #Disable notifications
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Ahora no']"))).click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Ahora no']"))).click()

    #Go to origin profile
    browser.get('https://www.instagram.com/'+ origin_username +'')

    #find number of followers
    sleep(2)
    allfoll = browser.find_element_by_xpath("//li[3]/a/span").text
    allfoll = int(float(allfoll))
    print(allfoll)

    #Go to following
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[3]"))).click()


    #scroll down the page
    sleep(2)
    dialog = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")

    for i in range(int(allfoll/7)):
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
        sleep(random.randint(500,1000)/1000)

        #Click all follow buttons
        while True:
            buttons = browser.find_elements_by_xpath("//button[contains(.,'Seguir')]")
            for btn in buttons:
                # Use the Java script to click on follow because after the scroll down the buttons will be un clickeable unless you go to it's location
                browser.execute_script("arguments[0].click();", btn)

                siguiendo = browser.find_elements_by_xpath("//button[contains(.,'Siguiendo')]")
                solicitado = browser.find_elements_by_xpath("//button[contains(.,'Solicitado')]")

                cont = len(siguiendo) + len(solicitado)

                print("Extract followers ", round(cont/allfoll*100, 2), "% from 100 %")
                sleep(random.randint(500,1000)/1000)

            sleep(5)
            buttons = browser.find_elements_by_xpath("//button[contains(.,'Seguir')]")

            if buttons:
                pop_up = browser.find_elements_by_xpath("//button[contains(.,'Aceptar')]")
                if pop_up:
                    pop_up.pop().click()
                print("Cooling down...")
                sleep(180)
                continue
            else:
                break

    siguiendo = browser.find_elements_by_xpath("//button[contains(.,'Siguiendo')]")
    solicitado = browser.find_elements_by_xpath("//button[contains(.,'Solicitado')]")
    print("From", allfoll, " you are following ", len(siguiendo), "users and you have to be accepted by", len(solicitado), "users")


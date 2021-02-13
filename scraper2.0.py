from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = 'D:\Chrome Driver\chromedriver.exe'

browser = webdriver.Chrome(path)
url = 'https://github.com/login'
browser.get(url)

loginid = input("Give your login id : ")
login = browser.find_element_by_id("login_field")
login.send_keys(loginid)

l2 = input("Give your password : ")
password = browser.find_element_by_id("password")
password.send_keys(l2)
browser.find_element_by_name("commit").click()



code = input("Have you give the code y/n. It may not also come. If it has came then please give the code and write y/n : ")
if code=='y':
    choice = input("do you want to create repository y/n: ")
    if choice =='y':
        browser.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a').click()
        repo_name = input("Give repository name : ")
        repo = browser.find_element_by_id("repository_name")
        repo.send_keys(repo_name)

        pp = input("Private or Public : ")
        if pp=='Private' or pp=='private':
            browser.find_element_by_id("repository_visibility_private").click()
            read_me = input("Do you want to add read me y/n : ")
            if read_me=='y':
                browser.find_element_by_id("repository_auto_init").click()
                browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button").click()
            elif read_me=='n':
                browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button").click()

        elif pp=='Public' or pp=='public':
            browser.find_element_by_id("repository_visibility_public").click()
            read_me1 = input("Do you want to add read me y/n : ")
            if read_me1=='y':
                browser.find_element_by_id("repository_auto_init").click()
                browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button").click()
            elif read_me1=='n':
                browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button").click()

    else:
        print("bye bye")
        browser.quit()
else:
    print("Bye bye")
    browser.quit()
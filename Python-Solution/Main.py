from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
import re,string,random,time

options = Options()
options.add_experimental_option("detach",True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options=options)


class Login:
    def __init__(self,website):
        self.website = website
        print("Getting Website")
        driver.get(self.website)    
        print("Generating Username")
        user = [random.choice(string.ascii_letters) for i in range(7)]
        self.username = ''.join(user)
        print("Generating Password")
        pass1 = [random.choice(string.ascii_letters) for i in range(7)]
        self.password = ''.join(pass1)
        time.sleep(2)#Pause's for 2 second
        
    def Login(self):
        # Username Field
        uerfiled = driver.find_element("xpath",value="//*[@id=\"username\"]")
        uerfiled.send_keys(self.username)
        # Password Field
        pasw = driver.find_element("xpath",value="//*[@id=\"password\"]")
        pasw.send_keys(self.password)
        # Click to Login
        login  = driver.find_element("xpath",value="//*[@id=\"log-in\"]")
        time.sleep(1)#Pause's for a second
        login.click()
        time.sleep(2)#Pause's for 2 second
        print("Login Completed............. \nLoading DashBoard..........\nSorting Amount..........  ")
    def Sort(self):
        arr = []
        containers= driver.find_elements("xpath",value ="//tbody/tr/td[5]")
        # print(containers)
        for container in containers:
            title =container.find_element("xpath",value='./span').text
            title = re.findall("[-\d]",title)
            lStr = ''.join([str(elem) for elem in title])
            arr.append(int(lStr))
        if(arr != arr.sort()):
            button = driver.find_element("xpath",value="//*[@id=\"amount\"]")
            button.click()
        print("Sorting Completed.")
        print("program.Closed();")

nw =Login("https://sakshingp.github.io/assignment/login.html")
nw.Login()
nw.Sort()

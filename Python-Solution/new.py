from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
import re,string,random,time

website = 'https://sakshingp.github.io/assignment/login.html'
options = Options()
options.add_experimental_option("detach",True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options=options)

driver.get(website)

user = [random.choice(string.ascii_letters) for i in range(7)]
username = ''.join(user)
pass1 = [random.choice(string.ascii_letters) for i in range(7)]
password = ''.join(pass1)
time.sleep(2)
uerfiled = driver.find_element("xpath",value="//*[@id=\"username\"]")
uerfiled.send_keys(username)

pasw = driver.find_element("xpath",value="//*[@id=\"password\"]")
pasw.send_keys(password)

login  = driver.find_element("xpath",value="//*[@id=\"log-in\"]")
time.sleep(1)
login.click()
time.sleep(2)

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
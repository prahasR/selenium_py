from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time 
import os
PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe" 
driver = webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php") 
cap = driver.find_element_by_id("login").text
st= cap[44:]
words= st.split(' ') 
user = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
check=driver.find_element_by_id("rememberusername")
btn=driver.find_element_by_id("loginbtn")
capt=driver.find_element_by_id("valuepkg3") 
user.send_keys("mt1200768") 

temp = re.findall(r'\d+', st) 
l = list(map(int, temp))
do=0
for i in words:
    if (i.isdigit()==True):
        continue
    elif(i=="add"):
        do=1
    elif(i=="subtract"):
        do=2
    elif(i=="first"):
        do=3
    elif (i=="second"):
        do=4
out=l[0]

if(do==1):
    out+=l[1]
elif(do==2):
    out-=l[1]
elif(do==4):
    out=l[1]
capt.send_keys(Keys.BACKSPACE)
capt.send_keys(out)
check.click()
print(os.environ)
s = os.environ.get('PASS')
password.send_keys(s) 
btn.click()  
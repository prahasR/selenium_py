from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

#getting contest number as input from user
contest=input("contest no.: ")
PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

con_name=contest+"/"
site = "https://codeforces.com/contest/"+contest+"/problems"
driver.get(site) 

#defining the location where for saving files
#the files will be saved in your C drive with file_name as contest_number
#change parent_dir if want to save at another location
parent_dir="C:/"              
path = os.path.join(parent_dir, con_name)  
os.mkdir(path)
no = driver.find_element_by_class_name("problem-frames")
prob=no.find_elements_by_class_name("problem-statement")
store=[]

for i in range(0,len(prob)):
    header=prob[i].find_element_by_class_name("header")
    title = header.find_element_by_class_name("title").text
    ti= title.split('.')
    
    #getting tag of each problem of a contest
    tag=ti[0]
    store.append(tag)
    temp_path=os.path.join(path,tag)
    os.mkdir(temp_path)
    
    st=prob[i].find_element_by_class_name("sample-test")
    inpt=st.find_elements_by_class_name("input")
    otpt=st.find_elements_by_class_name("output")
    #print(len(inpt))
    for j in range(0,len(inpt)):
        num=str(j+1)
        file1="input"+num+".txt"
        file2="output"+num+".txt"
        inpuut=inpt[j].text
        otpuut=otpt[j].text
        
        with open(os.path.join(temp_path, file1), 'w') as fp1:
            pass
            fp1.write(inpuut[11:])
        with open(os.path.join(temp_path, file2), 'w') as fp2:
            pass
            fp2.write(otpuut[11:])
for p in range(0,len(prob)):
    driver.get("https://codeforces.com/problemset/problem/"+contest+"/"+store[p])
    #na=driver.find_element_by_class_name("ttypography")
    #driver.save_screenshot(parent_dir+"/"+contest+"/"+store[p]+"/"+"problem"+store[p]+".png")

    try:
        na=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ttypography"))
        )
        na.screenshot(parent_dir+"/"+contest+"/"+store[p]+"/"+"problem"+store[p]+".png")

    finally:
        continue
driver.quit()
  

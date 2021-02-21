from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image 
import os

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
contest=input("contest no.: ")
con_name=contest+"/"
site = "https://codeforces.com/contest/"+contest+"/problems"
driver.get(site) 

parent_dir="C:/"
path = os.path.join(parent_dir, con_name)  
os.mkdir(path)
no = driver.find_element_by_class_name("problem-frames")
prob=no.find_elements_by_class_name("problem-statement")

for i in range(0,len(prob)):
    header=prob[i].find_element_by_class_name("header")
    title = header.find_element_by_class_name("title").text
    ti= title.split('.')
    tag=ti[0]
    temp_path=os.path.join(path,tag)
    os.mkdir(temp_path)
    
    #location = prob[i].location 
    #size = prob[i].size 
    #driver.save_screenshot("full_img.png")
    #x = location['x'] 
    #y = location['y'] 
    #w = x + size['width'] 
    #h = y + size['height']
    #fullImg = Image.open("full_img.png") 
    #cropImg = fullImg.crop(x, y, w, h) 
    #cropImg.save('cropImage.png')
    #element = prob[i].find_element_by_class_name("problem-statement")
    #img='problem_img.png' 
    #prob[i].screenshot(img)
    #os.path.join(temp_path, img) 
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

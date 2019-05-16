from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
import time
import requests
import urllib
import csv
from collections import defaultdict
n=int(input("Enter no.of users you want to add : "))
global s
def x():
    driver=webdriver.Chrome()
    driver.get('http://www.advaita.io/event/ml')
    pay_later=driver.find_element_by_id('pay-later')
    pay_later.click()

    def phone_no():
            k="".join([random.choice(string.digits) for i in range(9)])
            return "9" + k

    def college_name():
        a=["ITER",'CET','KIIT','SOA','BGU','IIT BHUBANESWAR','IIT KGP','NIT ROURKELA' ]
        b=random.choice(a)
        return b
    l=[]
    s=''
    with open('india.csv') as f:
        reader = csv.DictReader(f) 
        for i in reader:
            for (k,j) in i.items():
                if k=='name':
                    l.append(j)

    g=str(random.choice(l)) 
    def stdn_name():
        return g
    
    def chk_email():
        t="".join([random.choice(string.ascii_lowercase) for i in range(3)]) 
        return t+'@gmail.com'
    time.sleep(5)

    p_no= driver.find_element_by_xpath("//input[@name='phoneno']")
    p_no.send_keys(phone_no())
    name= driver.find_element_by_xpath("//input[@name='name']")
    name.send_keys(stdn_name())
    e_id= driver.find_element_by_xpath("//input[@name='emailid']")
    e_id.send_keys(chk_email())

    clname= driver.find_element_by_xpath("//input[@name='clgname']")
    clname.send_keys(college_name())
    #btn=driver.find_element_by_xpath('')
    #btn.click()
    clname.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.close()


for i in range(n):
    x()

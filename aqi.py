# -*- coding: utf-8 -*-
#author: Nilesh Sengupta
from selenium import *
from selenium.webdriver.support.ui import Select
import time
s=input("enter state ")
c=""
st=""
#the if block is incomplete and needs addition of states , cities and stations which can be found in the website https://app.cpcbccr.com/AQI_India/
if(s=="West Bengal"):
    print("Cities: Asansol , Kolkata , Howrah , Siliguri , Haldia , Durgapur ")
    c=input("enter city ")
    if(c=="Kolkata"):
        print("Station: Ballygaunge, Kolkata - WBPCB")
        print("Station: Fort William, Kolkata - WBPCB")
        print("Station: Jadavpur, Kolkata - WBPCB")
        print("Station: Rabindra Bharati University, Kolkata - WBPCB")
        print("Station: Rabindra Sarobar, Kolkata - WBPCB")
        print("Station: Victoria, Kolkata - WBPCB")
        print("Station: Bidhannagar, Kolkata - WBPCB")
        st=input("enter station ")
driver = webdriver.Chrome("C:\\Users\\lenovo\\Desktop\\python projects\\chromedriver.exe")
driver.get("https://app.cpcbccr.com/AQI_India/")
time.sleep(5)
dropdown1 = Select(driver.find_element_by_id('states'))
dropdown1.select_by_visible_text(s)
dropdown2 = Select(driver.find_element_by_id('cities'))
dropdown2.select_by_visible_text(c)
dropdown3 = Select(driver.find_element_by_id('stations'))
dropdown3.select_by_visible_text(st)
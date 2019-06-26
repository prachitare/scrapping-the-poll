from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unicodecsv as csv
from bs4 import BeautifulSoup
import requests
import os, os.path


link = "http://psleci.nic.in/Default.aspx"
browser = webdriver.Chrome(executable_path = 'C:/users/prachi/Desktop/chromedriver')
browser.get(link)

page=requests.get("http://psleci.nic.in/Default.aspx")
soup=BeautifulSoup(page.content, 'lxml')
soup.find_all('span')
soup.get_text()

elem = browser.find_element_by_id("ddlState").send_keys(Keys.ENTER)

#with open('submission.csv','a') as file:
#elem = browser.find_element_by_id("ddlState").send_keys(Keys.ENTER)
    #for rows in soup.find_all("td"):

        
            #state = rows.find_all("td").a.get_text()
from selenium.webdriver.support.ui import Select

#select = Select(browser.find_element_by_id('ddlState'))

# select by visible text
val = ['Arunachal Pradesh', 'Andhra Pradesh','Assam','Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra & Nagar Haveli', 'Daman & Diu', 'Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala', 'Madhya Pradesh','Maharashtra','Manipur','Meghalaya']

for j in range(len(val)):
    #b = "'%s'" % str(val[j])
    b = val[j]
    select = Select(browser.find_element_by_id('ddlState'))

    select.select_by_visible_text(b)
    district = []
    ac = []
    poll_station = []

    i = 1
    while True:
        try:
            select1 = Select(browser.find_element_by_id('ddlDistrict'))
            select_b1 = browser.find_element_by_id('ddlDistrict')
            xpath = "/html/body/form/div[4]/table/tbody/tr/td[2]/fieldset/table/tbody/tr[1]/td[4]/select/option[%s]" % str(i+1)
            dist = select_b1.find_element_by_xpath(xpath)
            district.append(dist.text)
            select1.select_by_visible_text(dist.text)

            
            count = 1
            while True:
                try:
                    select_ac1 = Select(browser.find_element_by_id('ddlAC'))
                    select_ac = browser.find_element_by_id('ddlAC')
                    xpath_ac = "/html/body/form/div[4]/table/tbody/tr/td[2]/fieldset/table/tbody/tr[2]/td[2]/select/option[%s]" % str(count+1)
                    constituency = select_ac.find_element_by_xpath(xpath_ac)
                    ac.append(constituency.text)
                    select_ac1.select_by_visible_text(constituency.text)

                    count+=1
                    #print ac

                    count_ps = 1
                    while True:
                        try:
                            #select_ps1 = Select(browser.find_element_by_id('ddlPS'))
                            select_ps = browser.find_element_by_id('ddlPS')
                            xpath_ps = "/html/body/form/div[4]/table/tbody/tr/td[3]/fieldset/table/tbody/tr[1]/td[2]/select/option[%s]" % str(count_ps+1)
                            ps = select_ps.find_element_by_xpath(xpath_ps)
                            poll_station.append(ps.text)
                            count_ps+=1
                        except:
                            break

                        with open('file.csv', mode='w') as myfile:
                            writer = csv.writer(myfile)
                            for row in poll_station:
                                writer.writerows([[row]])
                                #writer.writerows([district])
                        myfile.close()
                    poll_station = []
                    # for y in range(len(poll_station)):
                    #     print poll_station[y]

                    
                except:
                    break
            #print ac
            for y in range(len(ac)):
                print (ac[y])
            print ('--------------------------------------------------------------------------')
            ac = []
            i+=1
            
        except:
            break

    #print district
    # for y in range(len(district)):
    #     print (district[y])
    print('***********STATE CHANGE**************************************')
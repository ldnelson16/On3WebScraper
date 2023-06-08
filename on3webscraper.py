import requests
import pandas
#!pip install selenium
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

class Player:
    def __init__(self,name,ratingon3,rating247,ratingespn,ratingrivals,position,city,state,committed,team = False):
        self.name = name
        self.ron3 = ratingon3
        self.r247 = rating247
        self.respn = ratingespn
        self.rrivals = ratingrivals
        self.position = position
        self.city = city
        self.state = state
        self.committed = committed
        self.team = team
    def __str__(self):
        if self.committed == True:
            ret_format = "{}: Ratings - On3:{}, 247:{}, ESPN:{}, Rivals:{}\nPos: {}, City: {}, State: {}\n{} commit"
            return ret_format.format(self.name,self.ron3,self.r247,self.respn,self.rrivals,self.position,self.city,self.state,self.team)
        else:
            ret_format = "{}: Ratings - On3:{}, 247:{}, ESPN:{}, Rivals:{}\nPos: {}, City: {}, State: {}"
            return ret_format.format(self.name,self.ron3,self.r247,self.respn,self.rrivals,self.position,self.city,self.state)

results = []
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
for y in range (1,11):
    url = 'https://www.on3.com/db/rankings/industry-comparison/football/2024/?page='+str(y)
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    for x in range (0,50):
        try:
            xpath_name = '/html/body/div[1]/div[1]/section/main/section/section/ul/li[' + str(1+x) + ']/div[1]/div[1]/div/a'
            xpath_on3 = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[1]/a/div[1]/div[2]/div/span[2]/span"
            xpath_247 = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[2]/a/div[1]/div[2]/div/span[2]/span"
            xpath_espn = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[3]/a/div[1]/div[2]/div/span[2]/span"
            xpath_rivals = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[4]/a/div[1]/div[2]/div/span[2]/span"
            xpath_pos = "/html/body/div[1]/div[1]/section/main/section/section/ul/li["+ str(1+x) +"]/div[1]/div[1]/p[1]/span[1]"
            xpath_city = "/html/body/div[1]/div[1]/section/main/section/section/ul/li["+ str(1+x) +"]/div[1]/div[1]/p[2]/span[2]"
            xpath_state = "/html/body/div[1]/div[1]/section/main/section/section/ul/li["+ str(1+x) +"]/div[1]/div[1]/p[2]/span[2]"
            xpath_committed = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[3]/div/a"
            name = browser.find_element("xpath", xpath_name).text
            try:
                ron3 = browser.find_element("xpath", xpath_on3).text
            except:
                try:
                    xpath_on3 = "/html/body/div/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[1]/a/div[1]/div[2]/div/span[2]/span"
                    ron3 = browser.find_element("xpath", xpath_on3).text
                except:
                    try:
                        xpath_on3 = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[1]/a/div[3]/h6[1]"
                        ron3 = browser.find_element("xpath", xpath_on3).text
                    except:
                        xpath_on3 = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[1]/div/div[3]/h6[1]"
                        ron3 = browser.find_element("xpath", xpath_on3).text
            if ron3 != "-":
                ron3 = int(ron3)
            try:
                r247 = browser.find_element("xpath", xpath_247).text
            except:
                try:
                    xpath_247 = "/html/body/div/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[2]/a/div[1]/div[2]/div/span[2]/span"
                    r247 = browser.find_element("xpath", xpath_247).text
                except:
                    try:
                        xpath_247 = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[2]/a/div[3]/h6[1]"
                        r247 = browser.find_element("xpath", xpath_247).text
                    except:
                        xpath_247 = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[2]/div/div[3]/h6[1]"
                        r247 = browser.find_element("xpath", xpath_247).text
            if r247 != "-":
                r247 = int(r247)
            try:
                respn = browser.find_element("xpath", xpath_espn).text
            except:
                try:
                    xpath_espn = "/html/body/div/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[3]/div/div[1]/div[2]/div/span[2]/span"
                    respn = browser.find_element("xpath", xpath_espn).text                     
                except:
                    try:
                        xpath_espn = "/html/body/div/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[3]/a/div[3]/h6[1]"
                        respn = browser.find_element("xpath", xpath_espn).text 
                    except:
                        xpath_espn = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[3]/div/div[3]/h6[1]"
                        respn = browser.find_element("xpath",xpath_espn).text
            if respn != "-":
                respn = int(respn)
            try:
                rrivals = browser.find_element("xpath", xpath_rivals).text
            except:
                try:
                    xpath_rivals = "/html/body/div/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[4]/a/div[1]/div[2]/div/span[2]/span"
                    rrivals = browser.find_element("xpath", xpath_rivals).text
                except:
                    try:
                        xpath_rivals = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[4]/a/div[3]/h6[1]"
                        rrivals = browser.find_element("xpath", xpath_rivals).text
                    except:
                        xpath_rivals = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[4]/div/div[3]/h6[1]"
                        rrivals = browser.find_element("xpath", xpath_rivals).text
            if rrivals != "-":
                rrivals = float(rrivals)
            pos = browser.find_element("xpath", xpath_pos).text
            city_state = browser.find_element("xpath", xpath_city).text
            committed = browser.find_element("xpath",xpath_committed).text
            try:
                if committed[:11] == "HARD COMMIT":
                    committed = True
                    team = browser.find_element("xpath",xpath_committed).get_attribute('href')
                    team = " ".join(str(team).split("/")[4].split("-")).title()
                else:
                    committed = False
                    team = False
            except:
                committed = False
                team = False
            player = Player(name,ron3,r247,respn,rrivals,pos,city_state[:-4],city_state[-2:],committed,team)
            results+=[player]
        except:
            print("Nothing at player #",x+y*50-49)
            pass
    browser.close()
for result in results:
    print(result)

file = open("2023-06-08_RecruitData_Cl24.txt","w")
file.write("Name\tOn3 Rating\t247 Rating\tESPN Rating\tRivals Rating\tPosition\tCity\tState\tCommit Status\tCommit Team\n")
for result in results:
    file.write(result.name+"\t"+str(result.ron3)+"\t"+str(result.r247)+"\t"+str(result.respn)+"\t"+str(result.rrivals)+"\t"+result.position+"\t"+result.city+"\t"+result.state+"\t"+str(result.committed)+"\t"+str(result.team)+"\t"+"\n")
from AutoGMeet import AutoGMeet
import time
import datetime

getTime = str(datetime.datetime.today().time())
currentTime = getTime[:2] + getTime[3:5]
getDay = int(datetime.datetime.today().weekday())


times = [[1624, 1625], [1626, 1628], [1342, 1343]]  #Enter the starting time and ending time sample [[1100,1200][1200,1300]]
ack = [False,False,False]

usrname = "Enter then email address"
passwrd = "Enter the password"
text = "Enter the text you want to type in chatbox"
LEC1 = "Enter the url"
LEC2 = "Enter the meet url"
LEC3 = "Enter the meet url"
LEC4 = "Enter the meet url" 
LEC5 = "Enter the meet url" 

monday = [LEC1, LEC1, LEC2]
tuesday = [LEC1, LEC2, LEC3]
wednersday = [LEC1, LEC2, LEC3]
thursday = [LEC3, LEC1, LEC2]
friday = [LEC2, LEC3, LEC1]

days = [monday, tuesday, wednersday, thursday, friday]




while True:
    getTime = str(datetime.datetime.today().time())
    currentTime = int(getTime[:2] + getTime[3:5])

    day = days[getDay]
    # print(day)
    for i in range(len(times)):
        if times[i][0] <= currentTime < times[i][1]:
            print(day[i])
            if not ack[i]:
                auto = AutoGMeet(usrname,passwrd,"{}".format(day[i]),text,times[i][1])
                auto.automeetX()
                ack[i] = True
                #AutoMeet.browser.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div/span/span").click()
    print("HOLD")
    time.sleep(30)


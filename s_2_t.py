import speech_recognition as sr
from selenium import webdriver
import pyttsx3
from datetime import date


def ui_path_fun():
    engine = pyttsx3.init()

    # engine.say("Hello, Welcome to the Smart Automation.")
    # engine.say("How can I help you ?")
    # engine.runAndWait()

    r = sr.Recognizer()
    # this one is for flag this is decide your flow 

    engine.say("I am going to book bus for you.")
    engine.runAndWait()
    url = "http://127.0.0.1/Uipath_project/bus_book.php"
    driver = webdriver.Chrome()
    driver.get(url)

    def fun():
        with sr.Microphone() as source:
            while (1):
                print('now say  >>>>>')
                audio = r.listen(source)
                try:
                    _data = r.recognize_google(audio)
                    print('You said : {}'.format(_data))
                    return _data
                    break
                except:
                    print('Sorry could not recognize your voice')
                    engine.say('Sorry could not recognize your voice, Please say it again')
                    engine.runAndWait()

    # this is for departure city 
    print("Departure City?")
    engine.say("Which is the departure city?")
    engine.runAndWait()
    frm = fun()
    driver.find_element_by_id('frm').send_keys(frm)

    # this is for destination city
    print("Destination City?")
    engine.say("Which is the destination city?")
    engine.runAndWait()
    t_o = fun()
    driver.find_element_by_id('t_o').send_keys(t_o)

    # this is for bus type
    print("Bus type?")
    engine.say("Your preferance for bus type?")
    engine.runAndWait()
    b_type = fun()
    driver.find_element_by_id('b_type').send_keys(b_type)

    # this is for day in date
    print("Tell me Date dd/mm/yyyy ?")
    engine.say("On which day you like to book?")
    engine.say("Tell me day in date ")
    engine.runAndWait()
    dd = fun()
    print("Month?")
    engine.say("In which month you like to book?")
    engine.runAndWait()
    mm = fun()
    x = date.today()
    if mm == "in next month" or mm == "Next month" or mm == "Next Month" or mm == "next Month":
        try:
            mm_ = x.replace(month=x.month + 1).strftime("%B")
            print(mm_)
        except ValueError:
            if x.month == 12:
                mm_ = x.replace(year=x.year + 1, month=1)
            else:
                # next month is too short to have "same date"
                raise
    else:
        mm_ = x.strftime("%B")

    driver.find_element_by_id('dd').send_keys(dd)
    driver.find_element_by_id('mm').send_keys(mm_)

    engine.say("I will pick current year.")
    engine.runAndWait()
    yyyy = x.strftime("%Y")
    driver.find_element_by_id('yyyy').send_keys(yyyy)

    print(" Date is {}/{}/{} ".format(dd, mm, yyyy))

    # for bus time

    print("Want Return Ticket?")
    engine.say("You want return ticket?")
    engine.runAndWait()
    rtn = fun()

    if rtn == "no":
        driver.find_element_by_id('noCheck').click()
        r_dd = '0'
        r_mm = '0'
        r_yyyy = '0'
        r_hh = '0'
    elif rtn == "yes":
        driver.find_element_by_id('yesCheck').click()

        # this is for day return date
        print("Return date?")
        print("Day in date dd/mm/yyyy dd?")
        engine.say("On which day you like to book for return?")
        engine.say("Tell me day only!")
        engine.runAndWait()
        r_dd = fun()
        driver.find_element_by_id('r_dd').send_keys(r_dd)

        # this is for return month
        print("Now tell me month only?")
        engine.say("Now tell me month?")
        engine.say("In which month ?")
        engine.runAndWait()
        r_mm = fun()
        if r_mm == "in next month" or r_mm == "Next month" or r_mm == "Next Month" or r_mm == "next Month":
            try:
                r_mm_ = x.replace(month=x.month + 1).strftime("%B")
            except ValueError:
                if x.month == 12:
                    r_mm_ = x.replace(year=x.year + 1, month=1)
                else:
                    # next month is too short to have "same date"
                    raise
        else:
            r_mm_ = x.strftime("%B")

        driver.find_element_by_id('r_mm').send_keys(r_mm_)

        # this is for return date year
        engine.say("i will pick current year.")
        engine.runAndWait()
        r_yyyy = x.strftime("%Y")
        print("Return date is %d/%d/%d" % (r_dd, r_mm, r_yyyy))
        driver.find_element_by_id('r_yyyy').send_keys(r_yyyy)

    driver.find_element_by_id('sub').click()

    engine.say("Okay let me do some work, I have your data")
    engine.say("I will send ticket to your mail")
    engine.runAndWait()

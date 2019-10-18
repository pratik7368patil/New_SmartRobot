import speech_recognition as sr
import pyttsx3
from datetime import date

# book bus for me from Mumbai to Pune bus type ordinary on 23 next month


def Extract_query():
    engine = pyttsx3.init()
    r = sr.Recognizer()

    def recog_voice():
        with sr.Microphone() as source:
            while 1:
                engine.say("Hello, How can I help You?")
                engine.runAndWait()
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

    _data = recog_voice()
    # filter data (remove unwanted chars )
    bad_stm = ['/', '|', ';', '.', '!', '*', "'", ':', '?', '(', ')', '[', ']', '{', '}', '@', '#', "$", '%', "&", 'and', 'is', 'or']
    for i in bad_stm:
        _data = _data.replace(i, '')
        # separate each word from another

    _data_arr = _data.split()
    print(_data_arr)

    if _data_arr.index('book') == 0 and _data_arr.index('bus') == 1:
        # Destination data
        frm_idx = _data_arr.index('from')
        des_idx = frm_idx + 1
        des_city = _data_arr[des_idx]
        print(des_city)
        # Arrival city data
        to_idx = _data_arr.index('to')
        arr_idx = to_idx + 1
        arr_city = _data_arr[arr_idx]
        print(arr_city)
        # Bus type
        bt_idx = _data_arr.index('type')
        b_type_idx = bt_idx + 1
        b_type = _data_arr[b_type_idx]
        print(b_type)
        # get date
        dte_idx = _data_arr.index('on')
        dd_idx = dte_idx + 1
        dd = _data_arr[dd_idx]
        print(dd)
        # for month
        mm_idx = dte_idx + 2
        mm = _data_arr[mm_idx]

        x = date.today()
        yyyy = x.strftime("%Y")
        if mm == "next" or mm == "month":
            try:
                mm = x.replace(month=x.month + 1).strftime("%B")
                print(mm)
            except ValueError:
                if x.month == 12:
                    mm = x.replace(year=x.year + 1, month=1)
                else:
                    # next month is too short to have "same date"
                    raise
        else:
            mm

        print("Date is {}/{}/{} ".format(dd, mm, yyyy))




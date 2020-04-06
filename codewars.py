def camel_case(string):

    string = string.strip(' ')

    s = string.split(' ')
    str1 = ''
    for x in s:
        x = x.capitalize()
        str1 +=  x
    return str1




def to_camel_case(text):


    if '_' in text or '-' in text:

        textStrip = (text.replace('-','_')).split("_")

        
        

        str1 = textStrip[0] 
        n = False
        for x in textStrip:
            if n == False:
                n = True
                continue
            str1 = str1 + x.capitalize()

        
    

        return str1


    return ""




def bouncingBall(h, bounce, window):
    
    i = 0
    while h > window:
        i += 1
        if h > window:
            h *= bounce
            i += 1
        else:
            return i+1
        


    return i+1




def countBits(n):

 #
    b = ''
    i = 0
    g = 0
    #Перевод в двоичный
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    

    str1 = str(b)
    #сложение всех элементов строки
    while i != len(str1):
        g += int(str1[i]) 
        i += 1

    return g
# вообще мождно было проще
# b = bin(n) #это перевод в двоичный
# return b.count("1") # возращаем колличество 1 в строке И ВСЕЕЕЕЕЕЕЕЕЕЕ
# Я узнал о этих двух методов(PS раньше вообще их незнал)




def make_readable(seconds):

    if seconds <= 59:
        if seconds > 9:

            m = seconds
            if (m>9)and(m<20)or(m>110)or((m % 10)>4)or((m % 10)==0):
                print(m,"секунд")
            else:
                if (m % 10)==1: print(m,"секунда")
                else: print(m,"секунды")
        

    
    minuts = seconds // 60

    if minuts <= 59:

        if seconds == 60:
            return "00:0"+str(seconds // 60)+":0"+str((seconds-(minuts*60)))

        if minuts > 9:
            return "00:"+str(seconds // 60)+":"+str((seconds-(minuts*60)))
        else:
            return "00:0"+str(seconds // 60)+":"+str((seconds-(minuts*60)))


    hour = minuts // 60
    if hour > 9:
        hour = "0"+str(hour)

    minuts = minuts - (hour*60)
    if minuts > 9:
        minuts = "0"+str(minuts)

    sec = (seconds - (hour*60*60)) - (minuts*60)
    if sec > 9:
        sec = "0"+str(sec)



    return str(hour)+":"+str(minuts)+":"+str(sec)
        

def pluralRusVariant(x):

    latTwoDigits = x % 100
    tens = latTwoDigits / 10
    if tens == 1:
        return 2
    ones = latTwoDigits % 10
    if ones == 1:
        return 0
    if ones >= 2 and ones <= 4:
        return 1
    return 2

def showHours(hours):
    suffix = [ "час", "часа", "часов" ] [pluralRusVariant(hours)]
    return "{0} {1}".format(hours, suffix)



def format_duration(s):
    
    if s == 0:
        return "now"
        
    
    strDay =""
    strHour=""
    strMinute=""
    strSecond=""
    strYear=""
    
    day = s // 86400

    hour = s // 3600 - day * 24

    minute = s // 60 % 60

    second = s % 60

    

    year = day // 365


    if second != 0:
        m = second
        if (m>9)and(m<20)or(m>110)or((m % 10)>4)or((m % 10)==0):
            strSecond = str(m)+" seconds"
        else:
            if (m % 10)==1: strSecond = str(m)+" second"
            else: strSecond = str(m)+" seconds"

    if minute != 0:
        m = minute
        if (m>9)and(m<20)or(m>110)or((m % 10)>4)or((m % 10)==0):
            strMinute= str(m)+" minutes"
        else:
            if (m % 10)==1: strMinute = str(m)+" minute"
            else: strMinute = str(m)+" minutes"

    if hour != 0:
        m = hour
        if (m>9)and(m<20)or(m>110)or((m % 10)>4)or((m % 10)==0):
            strHour = str(m)+" hours"
        else:
            if (m % 10)==1: strHour = str(m)+" hour"
            else: strHour = str(m)+" hours"


    if day != 0:
        m = day
        if (m>9)and(m<20)or(m>110)or((m % 10)>4)or((m % 10)==0):
            strDay = str(m)+" days"
        else:
            if (m % 10)==1: strDay = str(m)+" days"
            else: strDay = str(m)+" days"


    if year != 0:
        m = year
        if (m>9)and(m<20)or(m>110)or((m % 10)>4)or((m % 10)==0):
            strYear = str(m)+"секунд"
        else:
            if (m % 10)==1: strYear = str(m)+"секунда"
            else: strYear = str(m)+"секунды"

    strM = [strYear, strDay, strHour, strMinute, strSecond]
    strM_new = []
    for x in strM:
        if x != "":
            strM_new.append(x)
    
    k = len(strM_new) - 1
    strOutput = ""
    for i in strM_new:

        if i == k:
            strOutput += i + " and "
            #строим строку по другому
        else:
            strOutput += i + ", "


    while i != len(strM_new):

        if i == k:
            strOutput += i + " and "
            #строим строку по другому
        else:
            strOutput += i + ", "

        i += 1

    
    

    return strOutput

    
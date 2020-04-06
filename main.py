import codewars






#Нужно спарсить сылку с сетвого города 
#потом с этой ссылки произвести авторизацию
#и мы попадем в сетевой город

#import authorization

#authorization.loginbot('login','password')

print(codewars.showHours(int(input())))

s= 3

strDay =""
strHour=""
strMinute=""
strSecond=""
strYear=""

hour = s // 3600
minute = s // 60 % 60
second = s % 60
day = hour // 24
year = day // 365


if second != 0:
    m = second
    if (m>9)and(m<20)or(m>110)or((m % 10)>4)or((m % 10)==0):
        strSecond = str(m)+" секунд"
    else:
        if (m % 10)==1: strSecond = str(m)+" секунда"
        else: strSecond = str(m)+" секунды"

if minute != 0:
    m = minute
    if (m>9)and(m<20)or(m>110)or((m % 10)>4)or((m % 10)==0):
        strMinute= str(m)+"минут"
    else:
         if (m % 10)==1: strMinute = str(m)+"минута"
         else: strMinute = str(m)+"минуты"

if hour != 0:
    m = hour
    if (m>9)and(m<20)or(m>110)or((m % 10)>4)or((m % 10)==0):
        strHour = str(m)+"час"
    else:
        if (m % 10)==1: strHour = str(m)+"часа"
        else: strHour = str(m)+"часы"


if day != 0:
    m = day
    if (m>9)and(m<20)or(m>110)or((m % 10)>4)or((m % 10)==0):
        strDay = str(m)+"день"
    else:
        if (m % 10)==1: strDay = str(m)+"день"
        else: strDay = str(m)+"секунды"


if year != 0:
    m = year
    if (m>9)and(m<20)or(m>110)or((m % 10)>4)or((m % 10)==0):
        strYear = str(m)+"секунд"
    else:
        if (m % 10)==1: strYear = str(m)+"секунда"
        else: strYear = str(m)+"секунды"



    

print(strYear+strDay+strHour + strMinute + strSecond)


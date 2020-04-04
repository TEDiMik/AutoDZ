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
            return "00:00:"+str(seconds)
        else:
            return "00:00:0"+str(seconds)
        

    
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
        





def format_duration(s):

    hour = s // 3600
    minute = s // 60 % 60
    second = s % 60

    

    return '{:02}:{:02}:{:02}'.format(hour, minute, second)

    
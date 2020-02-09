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
        if '_' in text:
            textStrip = text.split("_")
        else:
            textStrip = text.split("-")
        
        textStrip = text.split()

        str1 = textStrip[0] 
        n = False
        for x in textStrip:
            if n == False:
                n = True
                continue
            str1 = str1 + x.capitalize()

        
    

        return str1


    return ""


        
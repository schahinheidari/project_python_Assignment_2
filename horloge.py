#Assignment 2

def horloge(sec):
    a = str(sec//3600)
    b = str((sec%3600)//60)
    c = str((sec%3600)%60)
    d = print(a, ":", b, ":", c)
    return d

sec = int(input("please input your second: "))

horloge(sec)

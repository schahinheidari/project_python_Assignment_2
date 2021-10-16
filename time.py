#Assignment 2

#second = int(input("please entered SECOND: "))
#minute = int(input("please entered MINUTE: "))
#hour = int(input("please entered HOUR: "))
#if minute:
#    minute = 60
#elif hour:
#    hour = 60 * 60
#print(hour+minute+second, "second")

time_str = input('Time in hh:mm:ss:')
def get_seconds(time_str):
    hh, mm, ss = time_str.split(':')
    return int(hh) * 3600 + int(mm) * 60 + int(ss)

print('Time in Seconds:', get_seconds(time_str))

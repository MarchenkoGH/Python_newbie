import time



def what_time_is_it_now():
    secunds = 3
    for i in range(1, secunds + 1):
        print(i)
        time.sleep(1)
    return time.strftime("%H:%M")


print(what_time_is_it_now())

import time


def countdown():
    secunds = 3
    for i in range(1, secunds + 1):
        print(i)
        time.sleep(1)



@countdown()
def what_time_is_it_now():
    print(time.strftime("%H:%M"))

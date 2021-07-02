import time
t = int(input("how many seconds do you want to set the timer for?"))
while t:
# Devasree_Gopakumar-Batch1-Countdown
# to print number without getting decimal values
    mins = t // 60
# to print # the remainder values
    secs = t % 60
# for showing the format of the timer
    timer = "{:02d}:{:02d}".format(mins, secs)
# to show the result
    print(timer)
    time.sleep(1)
    t -= 1

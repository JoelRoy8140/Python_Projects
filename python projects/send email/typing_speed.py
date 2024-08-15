from time import *
import random as r


def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest:
                error = error + 1
        except :
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)





test = ["Learning to code is not only a valuable skill but also an exciting journey that allows you to solve complex problems",
"My name is joel roy","welcome to python tutorial"]
test1 = r.choice(test)
print("*****typing speed calculator*****")
print(test1)
print()
print()
time_1 = time()
testinput = input(" Enter : ")
time_2 = time()

print('Speed : ' ,speed_time(time_1,time_2,testinput), " w/sec")
print("Error : ", mistake(test1,testinput))


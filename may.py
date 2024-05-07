import time
desired_message = "IT'S FINALLY MAY, SO MAY I BE YOURS?"

chars = "'?,abcdefghijklmnopqrstuvwxyz "

message = ""
for i in desired_message: 
    if(i == " "):
        message += i
        continue
    for j in chars:
        if(j == " "):
            message += i

        print(j.upper() + message)
        time.sleep(0.04)

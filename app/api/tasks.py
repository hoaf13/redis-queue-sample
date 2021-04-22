import time 

def count_word(message):
    delay = 5
    print("Message: {}".format(message))
    print("Process was delayed in {} seconds.".format(delay))
    time.sleep(delay)
    count = message.split(" ")
    return len(count)
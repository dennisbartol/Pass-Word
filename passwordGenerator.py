# (Python3) PassWord Generator

import random
import sys

lower = "abcdefdghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_-"

all = lower + upper + numbers + symbols

length = 10

password = "" .join(random.sample(all, length))
#print(password)
sys.stdout.write("Hoi, je nieuwe password is :" + password)

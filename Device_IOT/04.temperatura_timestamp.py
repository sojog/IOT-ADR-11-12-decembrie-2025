import time
import random


print(time.time())

time.sleep(1)
print(time.time())

print(time.strftime("%Y-%m-%d %H:%M:%S"))


MIN_TEMP = 1
MAX_TEMP = 50
temperatura = random.randint(MIN_TEMP, MAX_TEMP)
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")


payload = f'''{{
    "timestamp" : "{timestamp}",
    "temperatura" : {temperatura}
}}'''

print(payload)
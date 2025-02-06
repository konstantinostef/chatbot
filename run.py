
from Event import *

for _ in range(1000):
    event = Event()
    data = event.create_event()
    print("prompt in english: ")
    print(event.prompt['en'])
    print("data in english: ")
    print(data['en'])
    print("prompt in greek: ")
    print(event.prompt['gr'])
    print("data in greek: ")
    print(data['gr'])
    print(40*"-")

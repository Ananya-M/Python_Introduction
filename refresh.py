import os, time
import keyboard as ky
import inflect

p=inflect.engine()
i=1
try:
    while (i<=500000000001):
            f=open("C:\\Users\\20031748\\Desktop\\sleep.txt", "w+")
            j=p.number_to_words(i)
            f.write(j+" seconds")
            i=i+1
except KeyboardInterrupt:
    pass

f.close()
ky.press_and_release('win+r')
time.sleep(1)
ky.write('C:\\Users\\20031748\\Desktop\\sleep.txt')
ky.press_and_release('enter')

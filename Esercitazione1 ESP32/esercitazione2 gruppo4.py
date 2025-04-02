from machine import Pin
from time import sleep, ticks_ms, ticks_diff,sleep_ms

ledR = Pin(2,Pin.OUT)
ledG = Pin(15,Pin.OUT)
ledB = Pin(16,Pin.OUT)
bt = Pin(14,Pin.IN, Pin.PULL_UP)

ledR.off()
ledB.off()
#ledG.on()
ledG.off()

flag = False 
last_click = 0
delay=2

def switch(pin):
    global last_click
    global delay
    global flag
    current_click = ticks_ms()
    delta = ticks_diff(current_click,last_click)
    if delta<200:
        return
    if delta <500:
        delay=1
        flag = not flag
    else:
        delay=2
    last_click = current_click
    flag = not flag
    global start
    start = ticks_ms()
    
    
bt.irq(handler=switch, trigger = Pin.IRQ_FALLING)

start=ticks_ms()

while True:
    curr=ticks_ms()
    if flag:
        if ticks_diff(curr,start) > delay*2000:
            ledG.off()
            ledR.on()
        elif ticks_diff(curr,start) > delay*1000:
            ledG.on()
            ledB.off()
        else:
            ledB.on()
    else:
        ledB.off()
        ledG.off()
        ledR.off()
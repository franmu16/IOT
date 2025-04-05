from machine import Pin, PWM
import math
import time
from time import sleep, ticks_ms, ticks_diff,sleep_ms

class BUZZER:
    def __init__(self, sig_pin):
        self.pwm = PWM(Pin(sig_pin, Pin.OUT))
        self.pwm.duty(0)  # Inizialmente spento
        self.wait=500
        
    def play(self, melodies, duty):
        for note in melodies:
            if note == 0:
                self.pwm.duty(0) # Pausa
            else:
                self.pwm.freq(note)
                self.pwm.duty(duty) # Imposta il volume del suono
            sleep_ms(self.wait) # Durata della nota
        self.stop() # Ferma il suono alla fine
        
    def stop(self):
        self.pwm.duty(0)

last_click = 0
   

A4 = 440
CS5 = 550
E5 = 660
A5 = 880

btn0 = Pin(0,Pin.IN, Pin.PULL_UP)
buzzer = BUZZER(14)

def switch(self):
    global buzzer
    global last_click
    current_click = ticks_ms()
    delta = ticks_diff(current_click,last_click)
    if delta<200:
        return
    if delta <500:
        buzzer.wait = 250
    else:
        buzzer.wait = 500
    last_click = current_click 

btn0.irq(handler=switch, trigger = Pin.IRQ_FALLING)

song = [A4,CS5,E5,A5,A5,E5,CS5,A4]
while True:
    buzzer.play(song,512)
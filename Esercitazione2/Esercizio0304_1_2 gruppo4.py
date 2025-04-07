from machine import Pin, PWM
import math
import time

# Uso della costante matematica pi greco
PI = math.pi

led = Pin(4,Pin.OUT)
# Configurazione del pin del buzzer
pinB = Pin(14, Pin.OUT)
passiveBuzzer = PWM(pinB, freq=2000)
passiveBuzzer.duty(0)

while True:
    passiveBuzzer.duty(512)
    led.on()
    time.sleep(2) gruppo
    passiveBuzzer.duty(0)
    led.off()
    time.sleep(1)

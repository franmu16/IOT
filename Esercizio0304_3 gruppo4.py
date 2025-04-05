from machine import Pin, PWM
import math
import time
from time import sleep_ms

# Uso della costante matematica pi greco
PI = math.pi

led1 = Pin(4,Pin.OUT) #led bianco
led3 = Pin(2,Pin.OUT) #led giallo
led2 = Pin(0,Pin.OUT) #led verde
# Configurazione del pin del buzzer
#pinB = Pin(14, Pin.OUT)
#passiveBuzzer = PWM(pinB, freq=2000)
#passiveBuzzer.duty(0)

class BUZZER:
    def __init__(self, sig_pin):
        self.pwm = PWM(Pin(sig_pin, Pin.OUT))
        self.pwm.duty(0)  # Inizialmente spento
        
    def play(self, melodies, wait, duty):
        for note in melodies:
            if note == 0:
                self.pwm.duty(0) # Pausa
            else:
                self.pwm.freq(note)
                self.pwm.duty(duty) # Imposta il volume del suono
                if note>0:
                    led1.on()
                    led2.off()
                    led3.off()
                if note>1660:
                    led2.on()
                    led3.off()
                if note>3320:
                    led3.on()
            sleep_ms(wait) # Durata della nota
        self.stop() # Ferma il suono alla fine
        
    def stop(self):
        self.pwm.duty(0)  # Spegne il suono
        led1.off()
        led2.off()
        led3.off()

B0=31
C1=33
CS1=35
D1=37
DS1=39
E1=41
F1=44
FS1=46
G1=49
GS1=52
A1=55
AS1=58
B1=62
C2=65
CS2=78
E2=82
F2=87
FS2=93
G2=98
GS2=104
A2=110
AS2=117
B2=123
C3=131
CS3=139
D3=147
DS3=156
E3=165
F3=175
FS3=185
G3=196
GS3=208
A3=220
AS3=233
B3=247
C4=262
CS4=277
D4=294
DS4=311
E4=330
F4=349
FS4=370
G4=392
GS4=415
A4=440
AS4=466
B4=494
C5=523
CS5=554
D5=587
DS5=622
E5=659
F5=698
FS5=740
G5=784
GS5=831
A5=880
AS5=932
B5=988
C6=1047
CS6=1109
D6=1175
DS6=1245
E6=1319
F6=1397
FS6=1480
G6=1568
GS6=1661
A6=1760
AS6=1865
B6=1976
C7=2093
CS7=2217
D7=2349
DS7=2489
E7=2637
F7=2794
FS7=2960
G7=3136
GS7=3322
A7=3520
AS7=3729
B7=3951
C8=4186
CS8=4435
D8=4699
DS8=4978

mario = [
    E7, E7, 0, E7,  0, C7, E7,  0,
    G7,  0, 0,  0, G6,  0,  0,  0,
    C7,  0, 0, G6,  0,  0, E6,  0,
     0, A6, 0, B6,  0,AS6, A6,  0,
    G6, E7, 0, G7, A7,  0, F7, G7,
     0, E7, 0, C7, D7, B6,  0,  0,
    C7,  0, 0, G6,  0,  0, E6,  0,
     0, A6, 0, B6,  0,AS6, A6,  0,
    G6, E7, 0, G7, A7,  0, F7, G7,
     0, E7, 0, C7, D7, B6,  0,  0,
   ]

buzzer=BUZZER(14)
buzzer.play(mario,150,512)


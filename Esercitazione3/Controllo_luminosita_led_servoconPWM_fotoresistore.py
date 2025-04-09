from machine import ADC, PWM, Pin
from time import sleep, sleep_ms

class LDR:
    """Questa classe legge un valore da un resistore dipendente dalla luce (LDR)"""

    def __init__(self, pin, min_value=0, max_value=100):
        """
        Inizializza una nuova istanza.
        :param pin Un pin a cui è collegato un LDR.
        :param min_value Un valore minimo che può essere restituito dal metodo value().
        :param max_value Un valore massimo che può essere restituito dal metodo value().
        """
        if min_value >= max_value:
            raise Exception('Il valore minimo è maggiore o uguale al valore massimo')

        # inizializza ADC (conversione da analogico a digitale)
        # crea un oggetto ADC
        self.adc = ADC(Pin(pin))
        self.min_value = min_value
        self.max_value = max_value

    def read(self):
        """
        Legge un valore grezzo dall'LDR.
        :return un valore da 0 a 4095.
        """
        return self.adc.read()
    
    def value(self):
        """
        Legge un valore dall'LDR nell'intervallo specificato.
        :return un valore dall'intervallo specificato [min, max].
        """
        return (self.max_value - self.min_value) * self.read() / 4095
    
class Servomotor:
    """
    Una classe per controllare un servomotore SG90 tramite PWM.
    La classe permette di impostare l'angolo del servomotore tra 0 e 180 gradi.
    
    La frequenza di lavoro è di 50 Hz, con un duty cycle che varia tra 2.5% e 12%,
    corrispondente a un duty cycle di 26 a 128 in una risoluzione a 10 bit.

    La classe gestisce anche la conversione dell'angolo in duty cycle.
    """
    def __init__(self, pin_num, freq=50, duty_min=36, duty_max=137):
        self.pwm = PWM(Pin(pin_num), freq=freq)
        self.duty_min = duty_min
        self.duty_max = duty_max
        self.angle = 0
    
    def set_angle(self, angle):
        if 0 <= angle <= 180:
            self.angle = angle
            self.pwm.duty(int(self.duty_min + (angle / 180) * (self.duty_max - self.duty_min)))
        else:
            raise ValueError("Angle must be between 0 and 180 degrees")
        
    def get_angle(self):
        return self.angle


class BUZZER:
    def __init__(self, pin_num):
        """
        Inizializza il buzzer sul pin specificato.
        pin_num: int, numero del pin GPIO a cui è collegato il buzzer
        """
        if not (0 <= pin_num <= 39):
            raise ValueError("Il numero del pin deve essere compreso tra 0 e 39.")
        
        self.pwm = PWM(Pin(pin_num, Pin.OUT))
        self.pwm.duty(0)  # Inizialmente spento
        
    def play(self, melody, dur, vol = 50):
        """
        Riproduce una melodia specifica per una durata e volume dati.
        melody: list, lista di frequenze delle note (in Hz)
        dur: int, durata in millisecondi
        vol: int, volume in percentuale (0-100)
        """
        duty = self.vol_to_duty(vol)
        for note in melody:
            if note == 0:
                self.pwm.duty(0) # Pausa
            else:
                self.pwm.freq(note)
                self.pwm.duty(duty) # Imposta il volume del suono
            sleep_ms(dur) # Durata della nota
        self.stop() # Ferma il suono alla fine

    def play_note(self, note, dur=0, duty=512):
        """
        Riproduce un suono specifico per una durata e volume dati.
        note: int, frequenza della nota (in Hz)
        dur: int, durata in millisecondi
        duty: int, valore del ciclo di lavoro (0-1023), consigliabile 512
        """
        self.pwm.freq(note)
        self.pwm.duty(duty)
        if(dur != 0):
            sleep_ms(dur)
            self.stop() 
        
    def stop(self):
        self.pwm.duty(0)  # Spegne il suono

#notes and its equivalent frequency
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

servo = Servomotor(12)
photo = LDR(34, 0, 180)
led = Pin(13, Pin.OUT)
buzzer = BUZZER(33)

while True:
    servo.set_angle(int(photo.value()))
    print(int(photo.value()))
    sleep(0.1)
    if(photo.value()<20):
        led.value(1)
        buzzer.play_note(C8)
    else:
        led.value(0)
        buzzer.stop()
    


from machine import Pin, PWM
from time import sleep

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
    
servo = Servomotor(12)
button = Pin(14, Pin.IN, Pin.PULL_UP)
while True:
    if(button.value() == 0):
        servo.set_angle(180)
        sleep(1)
    servo.set_angle(0)



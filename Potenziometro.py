from machine import Pin, ADC, PWM
import time

adc = ADC(Pin(27, mode=Pin.IN))
adc.atten(ADC.ATTN_11DB)  # Misura 0-3.3V
pwm_led = PWM(Pin(14, mode=Pin.OUT)) # Attach PWM object on the LED pin

#1kHz to 5kHz → Great for stable brightness control without flickering.
#In python, you can insert underscores _ to make the numbers easier to read.
#For example, to write 1 MHz instead of having 1000000, we can put 1_000_000 .
pwm_led.freq(5_000)


#We use the function .duty_()
#to select the duty cycle with a value between 0 and (0-1024).
#The voltage is set directly on the output of the previously selected pin.

while True:
    # Read ADC and convert to voltage
    #This method returns the raw ADC value ranged according to the resolution of the block,
    #e.g., 0-4095 for 12-bit resolution.
    val = adc.read()
    val = val * (1023 / 4095)
    print(round(val, 2), "V") # Keep only 2 digits
    pwm_led.duty(int(val))
from machine import Pin, I2C
import ssd1306
import framebuf
import time

#risoluzione del display OLED: 128x64 pixel
WIDTH = 128
HEIGHT = 64
SCL_PIN = 22
SDA_PIN = 21

#inizializzo l'interfaccia ic2
#0 indica che vuoi usare il bus I2C numero 0.
#1 indica che vuoi usare il bus I2C numero 1.
i2c = I2C(0, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN))
display = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

display.fill(1)                         # fill entire screen with white colour 
display.rect(8, 10, 112, 43, 0)        # draw a rectangle outline 10,10 to width=107, height=53, colour=1 (black)

# draw battery percentage
# x_pos coordinate orizzontali dei blocchi che riempiono la batteria
# percentages: valori percentuali da mostrare (25%, 50%, 75%, 100%).
x_pos = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109]
percentages = [.10, .20, .30, .40, .50, .60,.70, .80, .90, 1.0]
while True:
    #Cicla 4 volte per simulare la carica crescente.
    for ctr in range(10):
        #fill_rect: disegna un blocco pieno all’interno del rettangolo batteria.
        display.fill_rect(x_pos[ctr],12,9,39,0)
        display.fill_rect(0,2,128,8,1)
        #text(...): mostra la percentuale (es. "25%").
        display.text("{:.0%}".format(percentages[ctr]), 11, 2, 0)
        #show(): aggiorna il display.
        display.show()
        time.sleep_ms(1000)
    
    # This will clear the battery charge percentage 
    for ctr in range(10):
        display.fill_rect(x_pos[ctr],11,24,40,1)
        
    display.show()
        

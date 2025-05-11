#in python i componenti non standard si aggiungono a livello di interprete, ampliandolo con i conseguenti rischi di conflitto tra i vari componenti
#--> soluzione: o nuovo interprete o virtual environment (parto dalla versione 3, ne faccio una copia e su questa aggiungo i componenti necessari)

import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")  #connessione avventua e collegata al topic

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect   #quando perfezioniamo la connessione viene chiamata la callback
mqttc.on_message = on_message

mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)   #porta 1883 con 60 s di keep-alive

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()  #le funzioni loop servono per poter ricevere i messaggi (loop forever è una funzione bloccante e fino a che non si arresta la gestione della connessione continua all'infinito -> ideale se dobbiamo solo metterci in ascolto)
#loop_start: avvia un thread ausiliario che gestisce la connessione. Richiede un loop_stop nel programma per arrestarlo
#loop: funzione che gestisce in maniera immediata la connessione, va eseguita più volte nel programma per far svolgere le operazioni periodicamente
#su micro abbiamo check_msg e wait_msg. Verifica i messaggi in ingresso e li gestisce con una callback
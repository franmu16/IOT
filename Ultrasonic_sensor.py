from machine import Pin, time_pulse_us
import time

class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin):
        """
        Inizializza il sensore ad ultrasuoni impostando i pin per il trigger e l'echo.
        
        :param trig_pin: Numero del pin di output per il trigger.
        :param echo_pin: Numero del pin di input per l'eco.
        """
        self.trig = Pin(trig_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
        # Assicura che il trigger sia spento all'inizio
        self.trig.value(0)
        # Attende che il sensore si stabilizzi
        time.sleep_ms(50)

    def read_distance(self):
        """
        Esegue una singola lettura della distanza.
        Invia un impulso di 10 µs sul pin trigger e misura il tempo che impiega il segnale ad arrivare al pin echo.
        Il tempo misurato viene convertito in centimetri.
        
        return: La distanza misurata in centimetri oppure None in caso di timeout o errore.
        """
        # Imposta il trigger su LOW per assicurarsi di avere un segnale pulito
        self.trig.value(0)
        time.sleep_us(2)
        # Invia un impulso HIGH per 10 microsecondi
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)
        
        # Misura la durata dell'impulso HIGH sul pin echo (timeout di 20ms -> ostacolo a più di 3.5 metri circa)
        duration = time_pulse_us(self.echo, 1, 20000)
        if duration < 0:
            # Se duration è negativo significa che si è verificato un timeout
            return None
        
        # Calcola la distanza: la velocità del suono è circa 0.0343 cm/us.
        # Poiché il segnale percorre andata e ritorno, dividiamo per 2.
        distance = (duration / 2) * 0.0343
        return distance

    def average_distance(self, num_samples=3, delay_between_samples=10):
        """
        Esegue più letture della distanza e ne calcola la media per ottenere un valore più stabile.
        
        :param num_samples: Numero di campioni da prendere (default 3).
        :param delay_between_samples: Ritardo in millisecondi fra una lettura e l'altra (default 10 ms).
        :return: La distanza media in centimetri oppure None se nessuna lettura valida è stata ottenuta.
        """
        distances = []
        for _ in range(num_samples):
            d = self.read_distance()
            if d is not None:
                distances.append(d)
            time.sleep_ms(delay_between_samples)
        
        if not distances:
            return None
        return sum(distances) / num_samples

class Veicolo:
    _marca = ""
    _modello = ""
    _anno = ""
    _velocita_massima = ""
    
    def __init__(self,marca,modello,anno,velocita_massima):
        self._marca = marca
        self._anno = anno
        self._modello = modello
        self._velocita_massima = velocita_massima
    
    def __str__(self):
        return f"{self._marca} {self._modello} ({self._anno}) - Velocità massima: {self._velocita_massima} km/h"
    
    def descrizione(self):
        return(self.__str__())
    
    def mostra_descrizione(self):
        print(self.descrizione())
        
    def tipo_veicolo(self):
        return "Generico veicolo"


class Auto(Veicolo):
    _numero_posti = ""
    
    def __init__(self, marca, modello, anno, velocita_massima, numero_posti):
        super().__init__(marca,modello,anno,velocita_massima)
        self._numero_posti = numero_posti
    
    def descrizione(self):
        return(f"Auto: {super().descrizione()} - {self._numero_posti} posti")
    
    def tipo_veicolo(self):
        return "Automobile"


class Moto(Veicolo):
    _ha_sidecar = False
    
    def __init__ (self,marca,modello,anno,velocita_massima,ha_sidecar):
        super().__init__(marca,modello,anno,velocita_massima)
        self._ha_sidecar = ha_sidecar
        
    def descrizione(self):
        if(self._ha_sidecar):
            return(f"Moto: {super().descrizione()} - Con sidecar")
        else:
            return(f"Moto: {super().descrizione()} - Senza sidecar")
    
    def tipo_veicolo(self):
        return "Motocicletta"


class Camion(Veicolo):
    _capacita_carico = 0
    
    def __init__(self,marca,modello,anno,velocita_massima, capacita_carico):
        super().__init__(marca,modello,anno,velocita_massima)
        self._capacita_carico = capacita_carico
        
    def descrizione(self):
        return(f"Camion: {super().descrizione()} - Capacità: {self._capacita_carico} tonnellate")



a = Auto("Toyota", "Corolla", "2020", "180", "5")
m = Moto("Harley Davidson", "Fat Boy", "2019", "220", True)

a.mostra_descrizione()
m.mostra_descrizione()

print(a.tipo_veicolo())
print(m.tipo_veicolo())

c = Camion("Volvo", "FH16", "2021", "140", 25)
print(c.descrizione())



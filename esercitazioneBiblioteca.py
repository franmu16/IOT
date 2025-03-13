class Libro:
    def __init__(self, titolo, autore, anno, genere, disponibile=True):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.genere = genere
        self.disponibile = disponibile
    
    def __str__(self):
        if self.disponibile:
            return f"{self.titolo} di {self.autore} ({self.anno}) [{self.genere}] - Disponibile\n"
        else:
            return f"{self.titolo} di {self.autore} ({self.anno}) [{self.genere}] - Non Disponibile\n"
        
class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def __str__(self):
        s = "Biblioteca\n"
        for libro in self.catalogo:
            s += libro.__str__()
        return s
    
    def addBook(self, libro):
        self.catalogo.append(libro)
        return True 
    
    def cercaAuthor(self, autore):
        for libro in self.catalogo:
            if libro.autore.lower() == autore.lower():
                return libro
        return None
            
    def cercaTitolo(self, titolo):
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                return libro
        return None 
            
    def prestitoLibro(self, titolo):
        libro = self.cercaTitolo(titolo)
        if libro is not None:
            if libro.disponibile:
                libro.disponibile = False
                return True
            else:
                return False 
                
    def restituisciLibro(self, titolo):
        libro = self.cercaTitolo(titolo)
        if libro is not None:
            if not libro.disponibile:
                libro.disponibile = True
                return True
            else:
                return False

def stampa():
    print("---Biblioteca---\n")
    print("1. Mostra catalogo\n")
    print("2. Cerca per autore\n")
    print("3. Cerca per titolo\n")
    print("4. Prendi in prestito un libro\n")
    print("5. Restituisci un libro\n")
    print("6. Aggiungi un nuovo libro\n")
    print("7. Esci\n")
    
catalogo = Biblioteca()
while True:
    ins = ""
    while not ins in ['1', '2', '3', '4', '5', '6', '7']:
        stampa()
        ins = input("Scegli un'opzione: ")
    if ins == '1':
        print(catalogo.__str__())
    elif ins == '2':
        res = input("Inserire autore: ")
        libro = catalogo.cercaAuthor(res)
        if libro is not None:
            print(libro.__str__())
        else:
            print("Autore non trovato.")
    elif ins == '3':
        res = input("Inserire titolo: ")
        libro = catalogo.cercaTitolo(res)
        if libro is not None:
            print(libro.__str__())
        else:
            print("Titolo non trovato.")
    elif ins == '4':
        titolo = input("Titolo libro da prestare: ")
        if catalogo.prestitoLibro(titolo):
            print("Libro prestato con successo")
        else:
            print("Libro già prestato o non trovato")
    elif ins == '5':
        titolo = input("Titolo libro da restituire: ")
        if catalogo.restituisciLibro(titolo):
            print("Libro restituito con successo")
        else:
            print("Libro già restituito o non trovato")
    elif ins == '6':
        titolo = input("Titolo: ")
        autore = input("Autore: ")
        anno = input("Anno: ")
        genere = input("Genere: ")
        libro = Libro(titolo, autore, anno, genere)
        if catalogo.addBook(libro):
            print("Libro aggiunto con successo!")    
    elif ins == '7':
        break
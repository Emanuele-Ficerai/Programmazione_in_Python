#Sistema Avanzato di Gestione Biblioteca

#Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
#Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
#Gli utenti del sistema devono essere in grado di:
#aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.

#Classi:
#- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

#- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

#    Metodi:
#    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.
#    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. 
#      Restituisce un messaggio di stato.
#    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. 
#      Restituisce un messaggio di stato.
#    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. 
#      Se non ci sono libri disponibili, restituisce un messaggio di errore.

#Test Cases:
#- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
#- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
#- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
#- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.

class Libro:
    def __init__(self, titolo: str, autore: str) -> None:
        self.titolo: str= titolo
        self.autore: str= autore
        self.disponibile: bool = True


class Biblioteca:
    def __init__(self) -> str:
        self.libri: list[Libro]= []
    def aggiungi_libro(self, libro: Libro) -> str: #praticamente dentro le parentesi dopo il self, aggiungo l'attributo "libro" che posso utilizzare solo all'interno di questa funzione
        self.libri.append(libro)
        return "aggiunto"
    def presta_libro(self, titolo_libro: Libro) -> str:
        titolo_libro.disponibile = False
        return "prestato"
    def restituisci_libro(self, titolo_libro: Libro) -> str:
        titolo_libro.disponibile = True
        return "c'è"
    def mostra_libri_disponibili(self) -> list[str]:    
        libri_presenti: list[Libro]=[libro.titolo for libro in self.libri if libro.disponibile==True]
        return libri_presenti if libri_presenti==True else "error" 

book1: list=["topolino", "spiderman"]
book2: list=["batman", "capitan A"]
biblioteca= Biblioteca()
print(biblioteca.aggiungi_libro(book1),\
      biblioteca.aggiungi_libro(book2),\
    biblioteca.presta_libro(book1),\
    biblioteca.mostra_libri_disponibili(),\
        biblioteca.restituisci_libro(book1),\
            biblioteca.mostra_libri_disponibili(),\
                biblioteca.presta_libro(book1),\
                    biblioteca.presta_libro(book2),\
                        biblioteca.mostra_libri_disponibili(),
                        )
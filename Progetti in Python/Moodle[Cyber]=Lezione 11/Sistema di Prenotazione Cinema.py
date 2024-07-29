#Sistema di Prenotazione Cinema
#Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. 
#Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
#Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
#Classi:
#- Film: Rappresenta un film con titolo e durata.
 
#- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
#Metodi:
#- prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. 
#Restituisce un messaggio di conferma o di errore.
#- posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
#- Cinema: Gestisce le operazioni legate alla gestione delle sale.
#Metodi:
#- aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
#- prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

#Test case:
#- Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
#- Un cliente sceglie un film e prenota un certo numero di posti.
#- Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

class Film:
    def __init__(self, titolo: str, durata: str) -> None:
        self.titolo: str = titolo
        self.durata: str = durata


class Sala:
    def __init__(self, NID: int , film_attuale: str, posti_totali: int, posti_prenotati: int) -> None:
        self.NID: int = NID
        self.film_attuale: str = film_attuale
        self.posti_totali: int = posti_totali
        self.posti_prenotati: int = posti_prenotati
    def prenota_posti(self, num_posti: int):
        if self.posti_prenotati + num_posti < self.posti_totali:
            self.posti_prenotati+=num_posti
            return("PRENOTA")
        else:
            return("PIENO")
    def posti_disponibili(self):
        return self.posti_totali - self.posti_prenotati
    

class Cinema:
    def __init__(self, sale: list[Sala]=[]) -> None:
        self.sale: Sala= sale
    def aggiungi_sala(self, sala: Sala):
        self.sale.append(sala)
    def prenota_film(self, titolo: str, num_posti: int ):
        for sala in self.sale:
            if sala.film_attuale.titolo == titolo:
                sala.num_posti(num_posti)

cinema = Cinema()
film1 = Film("Intersteller", 169)
sala1 = Sala(1, film1, 100)
cinema.aggiungi_sala(sala1)
print(cinema.prenota_film("Intersteller"))
# ### CLASSE: Persona

# Creare un file chiamato "persona.py".
# In tale file, definire una classe chiamata Persona.
# Tale classe deve avere due attributi privati di tipo String, uno per il nome ed uno per il cognome, 
# ed un attributo privato di tipo int per l'età.
# - La classe Persona deve avere i seguenti metodi:

#     - init(first_name, last_name). Tale metodo, deve verificare che first_name, last_name siano stringhe; in caso negativo, 
# impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio di errore, ad esempio, 
# "Il nome inserito non è una stringa!".
#     Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona; 
# se first_name e last_name non sono due stringhe, allora assegnare None all'età.

#     - setName(first_name): consente di impostare il nome di una persona, modificando il valore del relativo attributo.
#     Il valore viene modificato se e solo se viene passata al metodo una stringa.
#     In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".

#     - setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo.
#     Il valore viene modificato se e solo se viene passata al metodo una stringa.
#     In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".

#     - setAge(age): consente di impostare l'età di una persona, modificando il valore del relativo attributo.
#     Il valore viene modificato se e solo se viene passato al metodo un numero intero.
#     In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".

#     - getName(): consente di ritornare il nome di una persona.

#     - getLastname(): consente di ritornare il cognome di una persona.

#     - getAge(): consente di ritornare l'età di una persona.

#     - greet(): stampa il seguente saluto "Ciao, sono nome cognome! Ho età anni!"

class Persona:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.__age: int #per assegnare il "privato" agli attributi si utilizza il doppio "__"(underscore) prima dell'attributo

        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            self.__first_name = None
            print("Il nome inserito non è una stringa!")
        
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            self.__last_name = None
            print("Il nome inserito non è una stringa!")
        
        if self.__first_name and self.__last_name:
            self.__age = 0
        else:
            self.__age = None

    def setName(self, first_name) -> None:
        if isinstance(first_name, str):
                self.__first_name = first_name
        else:
                print("Il nome inserito non è una stringa!")

    def setLastName(self, last_name) -> None:
        if isinstance(last_name, str):
                self.__last_name = last_name
        else:
                print("Il nome inserito non è una stringa!")

    def setAge(self, age) -> None:
        if isinstance(age, int):
            self.__age = age
        else:
             print("L'età deve essere un numero intero!")

    def getName(self) -> str:
         return self.__first_name
    
    def getLastname(self) -> str:
         return self.__last_name
    
    def getAge(self) -> int:
         return self.__age
    
    def greet(self) -> None:
         print(f"Ciao sono{self.getName()}{self.getLastname()}! Ho{self.getAge()}anni!")

# ### CLASSE Dottore
# Creare un file chiamato "dottore.py".
# In tale file, definire una classe chiamata Dottore. Si derivi Dottore dalla classe Persona.

# Un dottore ha un nome, un cognome, un età, definiti dalla classe Persona, una specializzazione descritta tramite una stringa 
# (ad esempio, Pediatra, Ostetrico, Medico Generale), ed una parcella per le visite in studio (si usi il tipo float).
# Gli attributi della classe dottore devono essere anch'essi privati.

# - Definire i seguenti metodi:
#     - costruttore della classe Dottore, il quale richiede in input la specializzazione (specialization) 
# di un dottore e la sua parcella (parcel).
#     Tale metodo deve controllare che specialization sia una stringa e che parcel sia un float, 
# altrimenti assegna None all'attributo che non verifica la condizione richiesta, mostrando un messaggio di errore, ad esempio, 
# "La parcella inserita non è un float!".

#     - setSpecialization(specialization): consente di impostare la specializzazione di un dottore, 
# modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa.
#     In caso contrario, stamapre un messaggio di errore, ad esempio "La specializzazione inserita non è una stringa!".

#     - setParcel(parcel): consente di impostare la parcella di un dottore, modificando il valore del relativo attributo.
#     Il valore viene modificato se e solo se viene passato al metodo un float.
#     In caso contrario, stamapre un messaggio di errore, ad esempio "La parcella inserita non è un float!".

#     - getSpecialization(): consente di ritornare la specializzazione del dottore.

#     - getParcel(): consente di ritornare la parcella del dottore.

#     - isAValidDoctor(): stabilisce se un dottore è un dottore valido; un dottore è valido se e solo se ha più di 30 anni, 
# in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina. Stampare "Doctor nome e cognome is valid!" ,
# se il dottore risulta valido.
#     In caso contrario, stampare "Doctor nome e cognome is not valid!".

#     - doctorGreet():tale metodo richiama la funzione greet() della classe Persona.
#     Poi, stampa il seguente saluto "Sono un medico specializzazione"

from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)
        self.__specialization: str = specialization
        self.__parcel: float = parcel

        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione inserita non è una stringa!")

        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcella inserita non è un float!")

    def setSpecialization(self, specialization) -> None:
        if isinstance(specialization, str):
                self.__specialization = specialization
        else:
                print("La specializzazione inserita non è una stringa!")

    def setParcel(self, parcel) -> None:
        if isinstance(parcel, str):
                self.__parcel = parcel
        else:
                print("La parcella inserita non è un float!")
    
    def getSpecialization(self) -> str:
         return self.__specialization
    
    def getParcel(self) -> float:
         return self.__parcel
    
    def isAValidDoctor(self) -> None:
        if self.__age > 30:
              print(f"Doctor {self.__first_name} e {self.__last_name} is valid!"); return True
        else:
             print(f"Doctor {self.__first_name} e {self.__last_name} is not valid!"); return False

    def doctorGreet(self) -> None:
         print(f"Sono un medico {self.__specialization}")

# ### CLASSE: Paziente
# Creare un file chiamato "paziente.py".
# In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

# Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
# - Definire i seguenti metodi:

#     costruttore della classe paziente, il quale richiede in input il codice identificativo,
# il quale deve essere un attributo privato.
#     setIdCode(idCode): consente di impostare il codice identificativo del paziente.
#     getidCode(): consente di ritornare il codice identificativo del paziente.
#     patientInfo(): stampa in output le informazioni del paziente in questo modo:

#         "Paziente: {nome} {cognome}
#          ID: {codice identificativo}"

from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str, id: str) -> None:
        super().__init__(first_name, last_name)
        self.__id: str = id

    def setIdcode(self, id: str) -> None:
        self.__id = id
     
    def getidcode(self) -> str:
        return self.__id
    
    def patientInfo(self) -> None:
        print(f"Paziente:{self.__first_name} {self.__last_name}\n ID:{self.__id}")

# ### CLASSE: Fattura
# Creare un file chiamato "fatture.py".
# In tale file, creare una classe chiamata Fattura.

# - Definire i seguenti metodi:

#     init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. 
# Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor(). 
# In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, 
# mentre assegnare 0 all'attributo salary (di tipo int).  In caso contrario, assegnare il valore None a tutti i 4 
# gli attributi della classe e stampare un messaggio di errore, 
# come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
#     getSalary(): deve ritornare il salario guadagnato dal dottore. 
# Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.
#     getFatture(): deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) 
# che ha il dottore e ritornare il suo valore.
#     addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, 
# aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().  
# Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
#     removePatient(idCode): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input 
# il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, 
# richiamando il metodo get Fatture() e getSalary(). 
# Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".

from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self, dottore: Dottore) -> None:
         if self.dottore.isAValidDoctor(self) == True:
             self.dottore: Dottore = dottore
             self.pazienti: list[Paziente] = []
             self.fatture: int = len(self.pazienti)
             self.salario: int = 0
         else:
             self.dottore, self.pazienti, self.fatture, self.salary = None
             print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
    
    def getSalary(self) -> int:
        self.salario = self.dottore.getParcel() * len(self.pazienti)
        return self.salario
    
    def getFatture(self) -> int:
        self.fatture = len(self.pazienti)
        return self.fatture
    
    def addPatient(self, newpatient: Paziente) -> None:
        self.newpatient: Paziente = newpatient
        self.pazienti.append(newpatient)
        self.getFatture(), self.getSalary()
        print(f"Alla lista del {self.dottore} è stato aggiunto il {newpatient.getidcode()}")

    def removePatient(self, idCode: str) -> None:
        self.idCode: str = idCode
        self.pazienti.remove(idCode)
        self.getFatture(), self.getSalary()
        print(f"Alla lista del {self.dottore} è stato rimosso il {idCode}")
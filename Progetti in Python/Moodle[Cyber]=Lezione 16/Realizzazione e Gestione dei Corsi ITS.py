#FILE COMPLETO
# ### Classe Room:
# La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), un numero di posti (seats) e un'area (area). 
#L'area è calcolata come il doppio dei posti.
# - Metodi:
#     - get_id(): Restituisce l'ID dell'aula.
#     - get_floor(): Restituisce il piano dell'aula.
#     - get_seats(): Restituisce il numero di posti dell'aula.
#     - get_area(): Restituisce l'area dell'aula.

# ### Classe Building:
# La classe Building rappresenta un edificio. 
#Ogni edificio ha un nome (name), un indirizzo (address), un intervallo di piani (floors), e una lista di aule (rooms).
# - Metodi:
#     - get_floors(): Restituisce l'intervallo di piani dell'edificio.
#     - get_rooms(): Restituisce la lista delle aule nell'edificio.
#     - add_room(room): Aggiunge un'aula all'edificio, 
#solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio.
#     - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.

class Room:
    def __init__(self, id: str, floor: int, seats: int) -> None:
        self.id: str = id
        self.floor: int = floor
        self.seats: int = seats
        self.area: int = seats*2
    
    def get_id(self) -> str:
        return self.id
    def get_floor(self) -> int:
        return self.floor
    def get_seats(self) -> int:
        return self.seats
    def get_area(self) -> int:
        return self.seats*2
    

class Building:
    def __init__(self, name: str, address: str, floors: tuple[int]) -> None:
        self.name: str = name
        self.address: str = address
        self.floors: tuple = floors
        self.rooms: list [Room] = []
    
    def get_floors(self) -> tuple [int] :
        return self.floors
    
    def get_rooms(self) -> list [Room]:
        return self.rooms
    

    def add_room(self, room: Room) -> None:
        self.rooms.append(room) if room.floor in range(self.floors[0], self.floors [1]+1) and room not in self.rooms else None
    
    def area(self) -> float:
        return sum([room.get_area() for room in self.rooms])
    
    # ### Classi Person, Student e Lecturer:
# La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
# Le classi Student e Lecturer ereditano da Person.
# Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
#     - set_group(group): Associa un gruppo di studio allo studente

# ### Classe Group:
# La classe Group rappresenta un gruppo di studio. 
# Ogni gruppo ha un nome (name), un limite di studenti (limit), una lista di studenti (students) e una lista di docenti (lecturers).
# - Metodi:
#     - get_name(): Restituisce il nome del gruppo
#     - get_limit(): Restituisce il limite di studenti nel gruppo
#     - get_students(): Resituisce la lista di studenti nel gruppo
#     - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. 
#       E' consentito 1 docente ogni 10 studenti. Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
#     - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
#     - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto.

class Person: 
    def __init__(self, cf: str, name: str, surname: str, age: int) -> None:
        self.cf: str = cf
        self.name: str = name
        self.surname: str = surname
        self.age: int = age


class Student(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int) -> None:
        super().__init__(cf, name, surname, age)
        self.group = None
    def set_group(self, group: 'Group') -> None:
        group.add_student(self)
        self.group = group


class Lecturer(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int) -> None:
        super().__init__(cf, name, surname, age)


class Group:
    def __init__(self, name: str, limit: int) -> None:
        self.name: str = name
        self.limit: int = limit
        self.students: list[Student] = []
        self.lecturers: list[Lecturer] = []
    def get_name(self) -> str:
        return self.name
    def get_limit(self) -> int:
        return self.limit
    def get_students(self) -> list[Student]:
        return self.students
    def get_limit_lecturers(self) -> int:
        return len(self.students)// 10+1
    def add_student(self, student: Student) -> None:
        if student not in self.students and self.limit > len(self.students):
            self.students.append(student) 
    def add_lecturer(self, lecturer: Lecturer) -> None:
        if lecturer not in self.lecturers and self.limit > len(self.lecturers):
            self.lecturers.append(lecturer)

# ### Classe Course:
# La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
# - Metodi:
#     - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
#     - get_groups(): Restituisce la lista dei gruppi nel corso.
#     - add_group(group): Aggiunge un gruppo al corso.

class Course:
    def __init__(self, name: str) -> None:
        self.groups: list[Group] = []
    def register(self, student: Student):
        for group in self.groups:
            if len(group.students) < group.limit:
                group.add_student(student)
                break
    def get_groups(self) -> list[Group]:
        return self.groups
    def add_group(self, group: Group) -> None:
        if group not in self.groups:
            self.groups.append(group)
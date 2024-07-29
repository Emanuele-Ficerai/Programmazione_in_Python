# Crea un context manager usando una classe

# Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

# Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__
class FileManager:
    def __init__(self, filename: str, mode: str) -> None:
        self.filename: str = filename
        self.mode: str = mode
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_value, tarcebacke):   
        if exc_type is not None:
            print("Caught an exception")
            print(f"Exception type{exc_type}")
            print(f"Exception type{exc_value}")
            print(f"Exception type{tarcebacke}")
        else:
            self.file.close()
        return False
    
with FileManager("example.txt", "w")as f:
    f.write("Hello, word")
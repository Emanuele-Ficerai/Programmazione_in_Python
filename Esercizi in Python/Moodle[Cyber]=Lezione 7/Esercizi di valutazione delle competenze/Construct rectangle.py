#Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. 
#Pertanto, data l'area specifica di una pagina Web rettangolare, il tuo compito ora è progettare una pagina Web rettangolare, 
#la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:
#1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
#2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
#3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.
#Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.
#Esempio:
#construct_rectangle(4)
#L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
#Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. 
#Quindi la lunghezza L è 2 e la larghezza W è 2.
#For example:
#Test 	Result
#print(construct_rectangle(4))
#[2, 2]
def construct_rectangle(area: float) -> list[float]:
      W = int(area**0.5)
      while W > 0:
            if area % W==0:
              L = area // W
              return[L, W]
      W=W-1
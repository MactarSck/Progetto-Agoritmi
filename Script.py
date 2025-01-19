import csv
from collections import deque

def leggi_matrice_adiacenza(percorso_file):
    # Legge la matrice di adiacenza da un file CSV.
    with open(percorso_file, 'r') as file:
        reader = csv.reader(file)
        matrice = [list(map(int, riga)) for riga in reader]
    return matrice

def grafo_orientato(matrice):
    # Determina se il grafo rappresentato dalla matrice di adiacenza è orientato.
    n = len(matrice)
    for i in range(n):
        for j in range(i + 1, n):
            if matrice[i][j] != matrice[j][i]:
                return True  # Il grafo è orientato
    return False  # Il grafo non è orientato

def bfs(matrice, start):
    # Applica l'algoritmo BFS
    n = len(matrice)
    visitato = [False] * n
    distanza = [-1] * n  # Distanza dal nodo di partenza
    predecessore = [-1] * n  # Per tracciare i percorsi

    coda = deque([start])
    visitato[start] = True
    distanza[start] = 0

    while coda:
        nodo_corrente = coda.popleft()
        for vicino, connesso in enumerate(matrice[nodo_corrente]):
            if connesso and not visitato[vicino]:
                visitato[vicino] = True
                distanza[vicino] = distanza[nodo_corrente] + 1
                predecessore[vicino] = nodo_corrente
                coda.append(vicino)

    return distanza, predecessore

def cammino_minimo(predecessore, destinazione):

    cammino = []
    nodo_corrente = destinazione
    
    # Risale attraverso i predecessori fino al nodo iniziale
    while nodo_corrente != -1:
        cammino.append(nodo_corrente)
        nodo_corrente = predecessore[nodo_corrente]
    
    #invertiamo l'ordine
    return cammino[::-1]  # Risultato cammino

def output(percorso_file, dati):
    # Stampa risultato in un file di testo
    with open(percorso_file, 'w') as file:
        for chiave, valore in dati.items():
            file.write(f"{chiave}: {valore}\n")
            
def stampa_risultati(risultati):
    # Stampa i risultati a video
    for chiave, valore in risultati.items():
        print(f"{chiave}: {valore}")

if __name__ == "__main__":
    # File di input e output
    file_input = "grafo.csv"
    file_output = "risultati_grafo.txt"
    
    matrice_adiacenza = leggi_matrice_adiacenza(file_input)

    orientato = grafo_orientato(matrice_adiacenza)

    nodo_iniziale = int(input("Inserisci il nodo iniziale (0-3): "))
    
    distanza, predecessore = bfs(matrice_adiacenza, nodo_iniziale)

    # Calcola cammini minimi per ogni nodo
    cammini_minimi = {}
    for i in range(len(matrice_adiacenza)):
        cammino = cammino_minimo(predecessore, i)
        cammini_minimi[i] = cammino

    # Rappresentazione Output
    risultati = {
        "Il grafo e orientato?": "Sì" if orientato else "No",
        "Distanze dal nodo iniziale": distanza,
        "Predecessori": predecessore,
        "Cammini Minimi": cammini_minimi
    }
    
    stampa_risultati(risultati)
    
    output(file_output, risultati)
    


    print(f"Risultati in: {file_output}")
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:46:21 2023

@author: ruvee
"""

#  Implementazione del grafo

grafo = {
    'A': {
        'B': {
            '08:00': 13,
            '12:00': 16,
            '18:00': 18,
            },
        'C': {
            '08:00': 17,
            '12:00': 10,
            '18:00': 9,
            },
        'D': {
            '08:00': 22,
            '12:00': 22,
            '18:00': 22,
            },
        'E': {
            '08:00': 10,
            '12:00': 18,
            '18:00': 15,
            },
        'F': {
            '08:00': 13,
            '12:00': 18,
            '18:00': 20,
            }
        },
    'B': {
        'A': {
            '08:00': 13,
            '12:00': 16,
            '18:00': 18,
            },
        'F': {
            '08:00': 12,
            '12:00': 15,
            '18:00': 20,
            }
        },
    
    'C': {
        'A': {
            '08:00': 17,
            '12:00': 10,
            '18:00': 9,
            },
        'D': {
            '08:00': 11,
            '12:00': 8,
            '18:00': 5,
            }
        },
    
    'D': {
        'A': {
            '08:00': 22,
            '12:00': 22,
            '18:00': 22,
            },
        'C': {
            '08:00': 11,
            '12:00': 8,
            '18:00': 5,
            },
        'E': {
            '08:00': 2,
            '12:00': 10,
            '18:00': 5,
            },
        'F': {
            '08:00': 12,
            '12:00': 12,
            '18:00': 18,
            }
        },
    
    'E': {
        'A': {
            '08:00': 10,
            '12:00': 18,
            '18:00': 15,
            },
        'D': {
            '08:00': 2,
            '12:00': 10,
            '18:00': 5,
            },
        'F': {
            '08:00': 10,
            '12:00': 13,
            '18:00': 18,
            }
        },
    
    'F': {
        'A': {
            '08:00': 13,
            '12:00': 18,
            '18:00': 20,
            },
        'B': {
            '08:00': 12,
            '12:00': 15,
            '18:00': 20,
            },
        'E': {
            '08:00': 10,
            '12:00': 13,
            '18:00': 18,
            },
        'D': {
            '08:00': 12,
            '12:00': 12,
            '18:00': 18,
            }
        }
     }


#  Implementazione di Dijkstra

import heapq  # Per utilizzare il modulo heapq per l'heap binario

def dijkstra_temporale(grafo, nodo_iniziale, nodo_finale, orario_desiderato):
    # Inizializza le distanze con infinito per tutti i nodi tranne il nodo iniziale
    distanze = {nodo: float('inf') for nodo in grafo}
    distanze[nodo_iniziale] = 0

    # Crea un dizionario per tenere traccia dei predecessori per ciascun nodo
    predecessori = {}

    # Crea un heap binario iniziale con il nodo iniziale
    heap = [(0, nodo_iniziale)]

    while heap:
        # Estrai il nodo con la distanza minima dalla coda
        (distanza_attuale, nodo_attuale) = heapq.heappop(heap)

        # Se abbiamo raggiunto il nodo finale, costruisci il percorso e restituiscilo
        if nodo_attuale == nodo_finale:
            percorso = []
            while nodo_attuale is not None:
                percorso.insert(0, nodo_attuale)
                nodo_attuale = predecessori.get(nodo_attuale)
            return distanza_attuale, percorso

        # Se la distanza attuale è maggiore di quella già calcolata, passa al prossimo nodo
        if distanza_attuale > distanze[nodo_attuale]:
            continue

        # Itera sugli archi uscenti dal nodo attuale
        for vicino, pesi_temporali in grafo[nodo_attuale].items():
            tempo_percorrenza = pesi_temporali.get(orario_desiderato)
            if tempo_percorrenza is not None:
                distanza_alternativa = distanza_attuale + tempo_percorrenza
                # Se la distanza alternativa è più breve, aggiornala
                if distanza_alternativa < distanze[vicino]:
                    distanze[vicino] = distanza_alternativa
                    predecessori[vicino] = nodo_attuale
                    heapq.heappush(heap, (distanza_alternativa, vicino))

    # Se non è stato possibile raggiungere il nodo finale, restituisci None
    return None, []

# Interazione con l'utente

nodo_iniziale = input("Inserisci il nodo di partenza: ").strip().upper()
nodo_finale = input("Inserisci il nodo di destinazione: ").strip().upper()
orario_desiderato = input("Seleziona l'orario (8:00, 12:00 o 18:00): ").strip()
tempo_percorrenza, percorso = dijkstra_temporale(grafo, nodo_iniziale, nodo_finale, orario_desiderato)

if tempo_percorrenza is not None:
    print(f"Il tempo di percorrenza da {nodo_iniziale} a {nodo_finale} alle {orario_desiderato} è di {tempo_percorrenza} minuti.")
    print(f"Percorso: {' -> '.join(percorso)}")
else:
    print(f"Non è stato trovato un percorso da {nodo_iniziale} a {nodo_finale} alle {orario_desiderato}.")


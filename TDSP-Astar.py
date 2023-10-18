# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:00:34 2023

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


#  Implementazione di A*

coordinate_nodi = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (3, 1),
    'D': (2, 3),
    'E': (4, 2),
    'F': (5, 0)
}

import heapq
import math

def distanza_euclidea(node1, node2):
    x1, y1 = coordinate_nodi[node1]
    x2, y2 = coordinate_nodi[node2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def astar_temporale(grafo, nodo_iniziale, nodo_finale, orario_desiderato):
    distanze = {nodo: float('inf') for nodo in grafo}
    distanze[nodo_iniziale] = 0
    heap = [(0, nodo_iniziale)]
    predecessori = {}

    while heap:
        _, nodo_attuale = heapq.heappop(heap)
        if nodo_attuale == nodo_finale:
            percorso = []
            while nodo_attuale is not None:
                percorso.insert(0, nodo_attuale)
                nodo_attuale = predecessori.get(nodo_attuale)
            return sum(grafo[percorso[i]][percorso[i + 1]][orario_desiderato] for i in range(len(percorso) - 1)), percorso

        for vicino, pesi_temporali in grafo[nodo_attuale].items():
            tempo_percorrenza = pesi_temporali.get(orario_desiderato)
            if tempo_percorrenza is not None:
                distanza_alternativa = distanze[nodo_attuale] + tempo_percorrenza

                if distanza_alternativa < distanze[vicino]:
                    distanze[vicino] = distanza_alternativa
                    predecessori[vicino] = nodo_attuale
                    euristica = distanza_euclidea(vicino, nodo_finale)
                    punteggio_f = distanza_alternativa + euristica
                    heapq.heappush(heap, (punteggio_f, vicino))

    return None, []

# Interazione con l'utente
# PS quando avviene l'interazione con l'utente l'errata sintassi dell'ora produce errore,
# si consiglia di scrivere 08:00, 12:00, 18:00
nodo_iniziale = input("Inserisci il nodo di partenza: ").strip().upper()
nodo_finale = input("Inserisci il nodo di destinazione: ").strip().upper()
orario_desiderato = input("Seleziona l'orario (8:00, 12:00 o 18:00): ").strip()
tempo_percorrenza, percorso = astar_temporale(grafo, nodo_iniziale, nodo_finale, orario_desiderato)

if tempo_percorrenza is not None:
    print(f"Il tempo di percorrenza da {nodo_iniziale} a {nodo_finale} alle {orario_desiderato} è di {tempo_percorrenza} minuti.")
    print(f"Percorso: {' -> '.join(map(str, percorso))}")
else:
    print(f"Non è stato trovato un percorso da {nodo_iniziale} a {nodo_finale} alle {orario_desiderato}.")



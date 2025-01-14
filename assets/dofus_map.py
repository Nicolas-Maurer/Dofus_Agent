import numpy as np
import matplotlib.pyplot as plt
import pickle

# Save the MapManager object to a file
def save_map_manager(map_manager, filename):
    with open(filename, 'wb') as file:
        pickle.dump(map_manager, file)

# Load the MapManager object from a file
def load_map_manager(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
    
class MapManager():
    def __init__(self):
        self.maps = {}

    def add_map(self, x, y, map):
        """Add a map to the manager"""
        key = (x, y)
        if key not in self.maps:
            self.maps[key] = map

    def visualize(self):
        fig, ax = plt.subplots()
        for key, map_node in self.maps.items():
            x, y = key
            ax.plot(x, y, 'bo')  # Place un point pour chaque carte
            for neighbor in map_node.neighbors:
                nx, ny = neighbor
                ax.plot([x, nx], [y, ny], 'k-', alpha=0.5)  # Trace des lignes vers les voisins
        ax.set_aspect('equal')
        plt.grid(True)
        plt.gca().invert_yaxis()
        plt.show()

class MapNode():
    "Represent element in a map"
    
    def __init__(self, x: int, y: int, zone: str, neighbors: list):
        self.x = x
        self.y = y
        self.zone = zone
        self.neighbors = neighbors
        self.ressources = {}
    
    def add_ressource(self, ressource, quantity):
        """Add the ressource available on this map"""

        if ressource not in self.ressources:
            self.ressources[ressource] = quantity
    


dofus_map = MapManager()
dofus_map.add_map(1, -15, MapNode(1, -15, "Cité d'Astrub", [(0, -15), (1, -16), (2, -15), (1, -14)]))
dofus_map.add_map(2, -15, MapNode(2, -15, "Cité d'Astrub", [(1, -15), (2, -16), (3, -15), (2, -14)]))
dofus_map.add_map(3, -15, MapNode(3, -15, "Cité d'Astrub", [(2, -15), (3, -16), (4, -15), (3, -14)]))
dofus_map.add_map(4, -15, MapNode(4, -15, "Cité d'Astrub", [(3, -15), (4, -16), (5, -15), (4, -14)]))
dofus_map.add_map(5, -15, MapNode(5, -15, "Cité d'Astrub", [(4, -15), (5, -16), (6, -15), (5, -14)]))
dofus_map.add_map(6, -15, MapNode(6, -15, "Cité d'Astrub", [(5, -15), (6, -16), (7, -15), (6, -14)]))
dofus_map.add_map(7, -15, MapNode(7, -15, "Cité d'Astrub", [(6, -15), (7, -16), (8, -15), (7, -14)]))

dofus_map.add_map(1, -16, MapNode(1, -16, "Cité d'Astrub", [(0, -16), (1, -17), (2, -16), (1, -15)]))
dofus_map.add_map(2, -16, MapNode(2, -16, "Cité d'Astrub", [(1, -16), (2, -17), (3, -16), (2, -15)]))
dofus_map.add_map(3, -16, MapNode(3, -16, "Cité d'Astrub", [(2, -16),           (4, -16), (3, -15)])) 
dofus_map.add_map(4, -16, MapNode(4, -16, "Cité d'Astrub", [(3, -16),           (5, -16), (4, -15)]))
dofus_map.add_map(5, -16, MapNode(5, -16, "Cité d'Astrub", [(4, -16), (5, -17), (6, -16), (5, -15)]))
dofus_map.add_map(6, -16, MapNode(6, -16, "Cité d'Astrub", [(5, -16), (6, -17), (7, -16), (6, -15)]))
dofus_map.add_map(7, -16, MapNode(7, -16, "Cité d'Astrub", [(6, -16), (7, -17), (8, -16), (7, -15)]))

dofus_map.add_map(1, -17, MapNode(1, -17, "Cité d'Astrub", [(0, -17), (1, -18), (2, -17), (1, -16)]))
dofus_map.add_map(2, -17, MapNode(2, -17, "Cité d'Astrub", [(1, -17), (2, -18),           (2, -16)]))
dofus_map.add_map(3, -17, MapNode(3, -17, "Cité d'Astrub", [          (3, -18), (4, -17)          ])) 
dofus_map.add_map(4, -17, MapNode(4, -17, "Cité d'Astrub", [(3, -17), (4, -18),  (5, -17)          ]))
dofus_map.add_map(5, -17, MapNode(5, -17, "Cité d'Astrub", [(4, -17), (5, -18), (6, -17), (5, -16)]))
dofus_map.add_map(6, -17, MapNode(6, -17, "Cité d'Astrub", [(5, -17), (6, -18)                    ]))
dofus_map.add_map(7, -17, MapNode(7, -17, "Cité d'Astrub", [          (7, -18), (8, -17), (7, -16)]))

dofus_map.add_map(1, -18, MapNode(1, -18, "Cité d'Astrub", [(0, -18), (1, -19), (2, -18), (1, -17)]))
dofus_map.add_map(2, -18, MapNode(2, -18, "Cité d'Astrub", [(1, -18), (2, -19), (3, -18), (2, -17)]))
dofus_map.add_map(3, -18, MapNode(3, -18, "Cité d'Astrub", [(2, -18), (3, -19), (4, -18), (3, -17)]))
dofus_map.add_map(4, -18, MapNode(4, -18, "Cité d'Astrub", [(3, -18), (4, -19), (5, -18), (4, -17)]))
dofus_map.add_map(5, -18, MapNode(5, -18, "Cité d'Astrub", [(4, -18), (5, -19), (6, -18), (5, -17)]))
dofus_map.add_map(6, -18, MapNode(6, -18, "Cité d'Astrub", [(5, -18), (6, -19), (7, -18), (6, -17)]))
dofus_map.add_map(7, -18, MapNode(7, -18, "Cité d'Astrub", [(6, -18), (7, -19), (8, -18), (7, -17)]))

dofus_map.add_map(1, -19, MapNode(1, -19, "Cité d'Astrub", [(0, -19), (1, -20), (2, -19), (1, -18)]))
dofus_map.add_map(2, -19, MapNode(2, -19, "Cité d'Astrub", [(1, -19), (2, -20),           (2, -18)]))
dofus_map.add_map(3, -19, MapNode(3, -19, "Cité d'Astrub", [                    (4, -19), (3, -18)]))
dofus_map.add_map(4, -19, MapNode(4, -19, "Cité d'Astrub", [(3, -19), (4, -20), (5, -19), (4, -18)]))
dofus_map.add_map(5, -19, MapNode(5, -19, "Cité d'Astrub", [(4, -19),           (6, -19), (5, -18)]))
dofus_map.add_map(6, -19, MapNode(6, -19, "Cité d'Astrub", [(5, -19),                     (6, -18)]))
dofus_map.add_map(7, -19, MapNode(7, -19, "Cité d'Astrub", [          (7, -20), (8, -19), (7, -18)]))

dofus_map.add_map(1, -20, MapNode(1, -20, "Cité d'Astrub", [(0, -20), (1, -21), (2, -20), (1, -19)]))
dofus_map.add_map(2, -20, MapNode(2, -20, "Cité d'Astrub", [(1, -20), (2, -21), (3, -20), (2, -19)]))
dofus_map.add_map(3, -20, MapNode(3, -20, "Cité d'Astrub", [(2, -20), (3, -21), (4, -20),         ]))
dofus_map.add_map(4, -20, MapNode(4, -20, "Cité d'Astrub", [(3, -20), (4, -21), (5, -20), (4, -19)]))
dofus_map.add_map(5, -20, MapNode(5, -20, "Cité d'Astrub", [(4, -20), (5, -21), (6, -20),         ]))
dofus_map.add_map(6, -20, MapNode(6, -20, "Cité d'Astrub", [(5, -20), (6, -21), (7, -20),         ]))
dofus_map.add_map(7, -20, MapNode(7, -20, "Cité d'Astrub", [(6, -20), (7, -21), (8, -20), (7, -19)]))

dofus_map.add_map(1, -21, MapNode(1, -21, "Cité d'Astrub", [(0, -21), (1, -22), (2, -21), (1, -20)]))
dofus_map.add_map(2, -21, MapNode(2, -21, "Cité d'Astrub", [(1, -21), (2, -22), (3, -21), (2, -20)]))
dofus_map.add_map(3, -21, MapNode(3, -21, "Cité d'Astrub", [(2, -21), (3, -22), (4, -21), (3, -20)]))
dofus_map.add_map(4, -21, MapNode(4, -21, "Cité d'Astrub", [(3, -21), (4, -22), (5, -21), (4, -20)]))
dofus_map.add_map(5, -21, MapNode(5, -21, "Cité d'Astrub", [(4, -21), (5, -22), (6, -21), (5, -20)]))
dofus_map.add_map(6, -21, MapNode(6, -21, "Cité d'Astrub", [(5, -21), (6, -22), (7, -21), (6, -20)]))
dofus_map.add_map(7, -21, MapNode(7, -21, "Cité d'Astrub", [(6, -21), (7, -22), (8, -21), (7, -20)]))

dofus_map.add_map(8, -21,  MapNode(8, -21, "Carrière d'Astrub",  [(7, -21),  (8,  -22), (9,  -21), (8,  -20)]))
dofus_map.add_map(9, -21,  MapNode(9, -21, "Carrière d'Astrub",  [(8, -21),  (9,  -22), (10, -21), (9,  -20)]))
dofus_map.add_map(10, -21, MapNode(10, -21, "Carrière d'Astrub", [(9, -21),             (11, -21), (10, -20)]))
dofus_map.add_map(11, -21, MapNode(11, -21, "Carrière d'Astrub", [(10, -21), (11, -22), (12, -21), (11, -20)]))
dofus_map.add_map(12, -21, MapNode(12, -21, "Carrière d'Astrub", [(11, -21),            (13, -21), (12, -20)]))

dofus_map.add_map(8,  -20, MapNode(8, -20, "Carrière d'Astrub",  [(7, -20),  (8,  -21), (9,  -20), (8,  -19)]))
dofus_map.add_map(9,  -20, MapNode(9, -20, "Carrière d'Astrub",  [(8, -20),  (9,  -21), (10, -20), (9,  -19)]))
dofus_map.add_map(10, -20, MapNode(10, -20, "Carrière d'Astrub", [(9, -20),  (10, -21), (11, -20), (10, -19)]))
dofus_map.add_map(11, -20, MapNode(11, -20, "Carrière d'Astrub", [(10, -20), (11, -21), (12, -20), (11, -19)]))
dofus_map.add_map(12, -20, MapNode(12, -20, "Carrière d'Astrub", [(11, -20), (12, -21),            (12, -19)]))

dofus_map.add_map(8,  -19, MapNode(8, -19, "Carrière d'Astrub",  [(7, -19),  (8,  -20), (9,  -19), (8,  -18)]))
dofus_map.add_map(9,  -19, MapNode(9, -19, "Carrière d'Astrub",  [(8, -19),  (9,  -20), (10, -19), (9,  -18)]))
dofus_map.add_map(10, -19, MapNode(10, -19, "Carrière d'Astrub", [(9, -19),  (10, -20),            (10, -18)])) ## special case
dofus_map.add_map(11, -19, MapNode(11, -19, "Carrière d'Astrub", [           (11, -20), (12, -19), (11, -18)]))
dofus_map.add_map(12, -19, MapNode(12, -19, "Carrière d'Astrub", [(11, -19), (12, -20),            (12, -18)]))

dofus_map.add_map(8,  -18, MapNode(8, -18, "Carrière d'Astrub",  [(7, -18),  (8,  -19), (9,  -18), (8,  -17)]))
dofus_map.add_map(9,  -18, MapNode(9, -18, "Carrière d'Astrub",  [(8, -18),  (9,  -19), (10, -18), (9,  -17)]))
dofus_map.add_map(10, -18, MapNode(10, -18, "Carrière d'Astrub", [(9, -18),  (10, -19), (11, -18), (10, -17)])) 
dofus_map.add_map(11, -18, MapNode(11, -18, "Carrière d'Astrub", [(10, -18), (11, -19), (12, -18), (11, -17)]))
dofus_map.add_map(12, -18, MapNode(12, -18, "Carrière d'Astrub", [(11, -18), (12, -19),            (12, -17)]))

dofus_map.add_map(8,  -17, MapNode(8,  -17, "Carrière d'Astrub", [(7, -17),  (8,  -18), (9,  -17), (8,  -16)]))
dofus_map.add_map(9,  -17, MapNode(9,  -17, "Carrière d'Astrub", [(8, -17),  (9,  -18), (10, -17), (9,  -16)])) ## special case
dofus_map.add_map(10, -17, MapNode(10, -17, "Carrière d'Astrub", [(9, -17),  (10, -18), (11, -17), (10, -16)])) 
dofus_map.add_map(11, -17, MapNode(11, -17, "Carrière d'Astrub", [(10, -17), (11, -18), (12, -17), (11, -16)]))
dofus_map.add_map(12, -17, MapNode(12, -17, "Carrière d'Astrub", [(11, -17), (12, -18),            (12, -16)]))

dofus_map.add_map(8,  -16, MapNode(8,  -16, "Carrière d'Astrub", [(7, -16),  (8,  -17), (9,  -16), (8,  -15)]))
dofus_map.add_map(9,  -16, MapNode(9,  -16, "Carrière d'Astrub", [(8, -16),  (9,  -17), (10, -16), (9,  -15)]))
dofus_map.add_map(10, -16, MapNode(10, -16, "Carrière d'Astrub", [(9, -16),  (10, -17), (11, -16), (10, -15)])) 
dofus_map.add_map(11, -16, MapNode(11, -16, "Carrière d'Astrub", [(10, -16), (11, -17), (12, -16), (11, -15)]))
dofus_map.add_map(12, -16, MapNode(12, -16, "Carrière d'Astrub", [(11, -16), (12, -17),            (12, -15)]))

dofus_map.add_map(8,  -15, MapNode(8,  -15, "Carrière d'Astrub", [(7, -15),  (8,  -16), (9,  -15), (8,  -14)]))
dofus_map.add_map(9,  -15, MapNode(9,  -15, "Carrière d'Astrub", [(8, -15),  (9,  -16), (10, -15), (9,  -14)]))
dofus_map.add_map(10, -15, MapNode(10, -15, "Carrière d'Astrub", [(9, -15),  (10, -16), (11, -15), (10, -14)])) 
dofus_map.add_map(11, -15, MapNode(11, -15, "Carrière d'Astrub", [(10, -15), (11, -16), (12, -15), (11, -14)]))
dofus_map.add_map(12, -15, MapNode(12, -15, "Carrière d'Astrub", [(11, -15), (12, -16)                      ]))

dofus_map.add_map(3,  -14, MapNode(3,  -14, "Prairies d'Astrub", [(2, -14),  (3,  -15), (4,  -14), (3,  -13)]))
dofus_map.add_map(4,  -14, MapNode(4,  -14, "Prairies d'Astrub", [(3, -14),  (4,  -15), (5,  -14), (4,  -13)]))
dofus_map.add_map(5,  -14, MapNode(5,  -14, "Prairies d'Astrub", [(4, -14),  (5,  -15), (6,  -14), (5,  -13)]))
dofus_map.add_map(6,  -14, MapNode(6,  -14, "Prairies d'Astrub", [(5, -14),  (6,  -15), (7,  -14), (6,  -13)]))
dofus_map.add_map(7,  -14, MapNode(7,  -14, "Prairies d'Astrub", [(6, -14),  (7,  -15), (8,  -14), (7,  -13)]))
dofus_map.add_map(8,  -14, MapNode(8,  -14, "Prairies d'Astrub", [(7, -14),  (8,  -15), (9,  -14), (8,  -13)]))
dofus_map.add_map(9,  -14, MapNode(9,  -14, "Prairies d'Astrub", [(8, -14),  (9,  -15), (10, -14), (9,  -13)]))
dofus_map.add_map(10, -14, MapNode(10, -14, "Prairies d'Astrub", [(9, -14),  (10, -15), (11, -14), (10, -13)]))
dofus_map.add_map(11, -14, MapNode(11, -14, "Prairies d'Astrub", [(10, -14), (11, -15),            (11, -13)]))

dofus_map.add_map(3,  -13, MapNode(3,  -13, "Prairies d'Astrub", [(2, -13),  (3,  -14), (4,  -13), (3,  -12)]))
dofus_map.add_map(4,  -13, MapNode(4,  -13, "Prairies d'Astrub", [(3, -13),  (4,  -14), (5,  -13), (4,  -12)]))
dofus_map.add_map(5,  -13, MapNode(5,  -13, "Prairies d'Astrub", [(4, -13),  (5,  -14), (6,  -13), (5,  -12)]))
dofus_map.add_map(6,  -13, MapNode(6,  -13, "Prairies d'Astrub", [(5, -13),  (6,  -14), (7,  -13), (6,  -12)]))
dofus_map.add_map(7,  -13, MapNode(7,  -13, "Prairies d'Astrub", [(6, -13),  (7,  -14), (8,  -13), (7,  -12)]))
dofus_map.add_map(8,  -13, MapNode(8,  -13, "Prairies d'Astrub", [(7, -13),  (8,  -14), (9,  -13), (8,  -12)]))
dofus_map.add_map(9,  -13, MapNode(9,  -13, "Prairies d'Astrub", [(8, -13),  (9,  -14), (10, -13), (9,  -12)]))
dofus_map.add_map(10, -13, MapNode(10, -13, "Prairies d'Astrub", [(9, -13),  (10, -14), (11, -13), (10, -12)]))
dofus_map.add_map(11, -13, MapNode(11, -13, "Prairies d'Astrub", [(10, -13), (11, -14),            (11, -12)]))

dofus_map.add_map(3,  -12, MapNode(3,  -12, "Prairies d'Astrub", [(2, -12),  (3,  -13), (4,  -12), (3,  -11)]))
dofus_map.add_map(4,  -12, MapNode(4,  -12, "Prairies d'Astrub", [(3, -12),  (4,  -13), (5,  -12), (4,  -11)]))
dofus_map.add_map(5,  -12, MapNode(5,  -12, "Prairies d'Astrub", [(4, -12),  (5,  -13), (6,  -12), (5,  -11)]))
dofus_map.add_map(6,  -12, MapNode(6,  -12, "Prairies d'Astrub", [(5, -12),  (6,  -13), (7,  -12), (6,  -11)]))
dofus_map.add_map(7,  -12, MapNode(7,  -12, "Prairies d'Astrub", [(6, -12),  (7,  -13), (8,  -12), (7,  -11)]))
dofus_map.add_map(8,  -12, MapNode(8,  -12, "Prairies d'Astrub", [(7, -12),  (8,  -13), (9,  -12), (8,  -11)]))
dofus_map.add_map(9,  -12, MapNode(9,  -12, "Prairies d'Astrub", [(8, -12),  (9,  -13), (10, -12), (9,  -11)]))
dofus_map.add_map(10, -12, MapNode(10, -12, "Prairies d'Astrub", [(9, -12),  (10, -13), (11, -12), (10, -11)]))
dofus_map.add_map(11, -12, MapNode(11, -12, "Prairies d'Astrub", [(10, -12), (11, -13),            (11, -11)]))

dofus_map.add_map(3,  -11, MapNode(3,  -11, "Prairies d'Astrub", [(2, -11),  (3,  -12), (4,  -11), (3,  -10)]))
dofus_map.add_map(4,  -11, MapNode(4,  -11, "Prairies d'Astrub", [(3, -11),  (4,  -12), (5,  -11), (4,  -10)]))
dofus_map.add_map(5,  -11, MapNode(5,  -11, "Prairies d'Astrub", [(4, -11),  (5,  -12), (6,  -11), (5,  -10)]))
dofus_map.add_map(6,  -11, MapNode(6,  -11, "Prairies d'Astrub", [(5, -11),  (6,  -12), (7,  -11), (6,  -10)]))
dofus_map.add_map(7,  -11, MapNode(7,  -11, "Prairies d'Astrub", [(6, -11),  (7,  -12), (8,  -11), (7,  -10)]))
dofus_map.add_map(8,  -11, MapNode(8,  -11, "Prairies d'Astrub", [(7, -11),  (8,  -12), (9,  -11), (8,  -10)]))
dofus_map.add_map(9,  -11, MapNode(9,  -11, "Prairies d'Astrub", [(8, -11),  (9,  -12), (10, -11), (9,  -10)]))
dofus_map.add_map(10, -11, MapNode(10, -11, "Prairies d'Astrub", [(9, -11),  (10, -12), (11, -11), (10, -10)]))
dofus_map.add_map(11, -11, MapNode(11, -11, "Prairies d'Astrub", [(10, -11), (11, -12)                      ]))

dofus_map.add_map(3,  -10, MapNode(3,  -10, "Prairies d'Astrub", [(2, -10),  (3,  -11), (4,  -10), (3,  -9)]))
dofus_map.add_map(4,  -10, MapNode(4,  -10, "Prairies d'Astrub", [(3, -10),  (4,  -11), (5,  -10), (4,  -9)]))
dofus_map.add_map(5,  -10, MapNode(5,  -10, "Prairies d'Astrub", [(4, -10),  (5,  -11), (6,  -10), (5,  -9)]))
dofus_map.add_map(6,  -10, MapNode(6,  -10, "Prairies d'Astrub", [(5, -10),  (6,  -11), (7,  -10), (6,  -9)]))
dofus_map.add_map(7,  -10, MapNode(7,  -10, "Prairies d'Astrub", [(6, -10),  (7,  -11), (8,  -10), (7,  -9)]))
dofus_map.add_map(8,  -10, MapNode(8,  -10, "Prairies d'Astrub", [(7, -10),  (8,  -11), (9,  -10), (8,  -9)]))
dofus_map.add_map(9,  -10, MapNode(9,  -10, "Prairies d'Astrub", [(8, -10),  (9,  -11), (10, -10), (9,  -9)]))
dofus_map.add_map(10, -10, MapNode(10, -10, "Prairies d'Astrub", [(9, -10),  (10, -11)                     ]))

dofus_map.add_map(3,  -9, MapNode(3,  -9, "Prairies d'Astrub", [(2, -9),  (3,  -10), (4,  -9), (3,  -8)]))
dofus_map.add_map(4,  -9, MapNode(4,  -9, "Prairies d'Astrub", [(3, -9),  (4,  -10), (5,  -9), (4,  -8)]))
dofus_map.add_map(5,  -9, MapNode(5,  -9, "Prairies d'Astrub", [(4, -9),  (5,  -10), (6,  -9)          ]))
dofus_map.add_map(6,  -9, MapNode(6,  -9, "Prairies d'Astrub", [(5, -9),  (6,  -10), (7,  -9)          ]))
dofus_map.add_map(7,  -9, MapNode(7,  -9, "Prairies d'Astrub", [(6, -9),  (7,  -10), (8,  -9)          ]))
dofus_map.add_map(8,  -9, MapNode(8,  -9, "Prairies d'Astrub", [(7, -9),  (8,  -10), (9,  -9), (8,  -8)]))
dofus_map.add_map(9,  -9, MapNode(9,  -9, "Prairies d'Astrub", [(8, -9),  (9,  -10),           (9,  -8)]))

dofus_map.add_map(2,  -8, MapNode(2,  -8, "Prairies d'Astrub", [(1, -8),  (2,  -9), (3,  -8)          ]))
dofus_map.add_map(3,  -8, MapNode(3,  -8, "Prairies d'Astrub", [(3, -9),  (3,  -9)                    ]))
dofus_map.add_map(8,  -8, MapNode(8,  -8, "Prairies d'Astrub", [          (8,  -9), (9,  -8)          ]))
dofus_map.add_map(9,  -8, MapNode(9,  -8, "Prairies d'Astrub", [(8, -8),  (9,  -9),                   ]))

dofus_map.add_map(-4, -8, MapNode(-4, -8, "Cimetière d'Astrub", [(-5, -8),  (-4, -9), (-3,  -8)          ]))
dofus_map.add_map(-3, -8, MapNode(-3, -8, "Cimetière d'Astrub", [(-4, -8),  (-3, -9), (-2,  -8), (-3, -7)])) 

dofus_map.add_map(-4, -9, MapNode(-4, -9, "Cimetière d'Astrub", [(-5, -9),  (-4, -10), (-3,  -9), (-4, -8)]))
dofus_map.add_map(-3, -9, MapNode(-3, -9, "Cimetière d'Astrub", [(-4, -9),  (-3, -10),                    ]))
dofus_map.add_map(-2, -9, MapNode(-2, -9, "Cimetière d'Astrub", [(-3, -9),  (-2, -10),                    ]))
dofus_map.add_map(-1, -9, MapNode(-1, -9, "Cimetière d'Astrub", [           (-1, -10), (0,  -9),         ])) # staircase go to down
dofus_map.add_map(0,  -9, MapNode(0,  -9, "Cimetière d'Astrub", [(-1, -9),  (0,  -10), (1,  -9),         ]))
dofus_map.add_map(1,  -9, MapNode(1,  -9, "Cimetière d'Astrub", [(0, -9),  (1,  -10), (2,  -9),         ]))
dofus_map.add_map(2,  -9, MapNode(2,  -9, "Cimetière d'Astrub", [(1, -9),  (2,  -10), (3,  -9), (2,  -8)]))

dofus_map.add_map(-3, -10, MapNode(-3, -10, "Cimetière d'Astrub", [(-4, -10),  (-3, -11), (-2, -10), (-3, -9)]))
dofus_map.add_map(-2, -10, MapNode(-2, -10, "Cimetière d'Astrub", [(-3, -10),  (-2, -11), (-1, -10), (-2, -9)]))
dofus_map.add_map(-1, -10, MapNode(-1, -10, "Cimetière d'Astrub", [(-2, -10),  (-1, -11), (0,  -10), (-1, -9)]))
dofus_map.add_map(-0, -10, MapNode(-0, -10, "Cimetière d'Astrub", [(-1, -10),  (-0, -11), (1,  -10), (-0, -9)]))
dofus_map.add_map(1, -10, MapNode(1, -10, "Cimetière d'Astrub",   [(0, -10),   (1, -11),  (2,  -10), (1, -9)]))
dofus_map.add_map(2, -10, MapNode(2, -10, "Cimetière d'Astrub",   [(1, -10),              (3,  -10), (2, -9)]))

dofus_map.add_map(-3, -11, MapNode(-3, -11, "Cimetière d'Astrub", [(-4, -11),  (-3, -12), (-2,  -11), (-3, -10)]))
dofus_map.add_map(-2, -11, MapNode(-2, -11, "Cimetière d'Astrub", [(-3, -11),  (-2, -12), (-1,  -11), (-2, -10)]))
dofus_map.add_map(-1, -11, MapNode(-1, -11, "Cimetière d'Astrub", [(-2, -11),  (-1, -12), (0,  -11), (-1, -10)]))
dofus_map.add_map(-0, -11, MapNode(-0, -11, "Cimetière d'Astrub", [(-1, -11),  (-0, -12), (1,  -11), (-0, -10)]))
dofus_map.add_map(1, -11, MapNode(1, -11, "Cimetière d'Astrub", [(0, -11),  (1, -12), (2,  -11), (1, -10)]))
dofus_map.add_map(2, -11, MapNode(2, -11, "Cimetière d'Astrub", [(1, -11),  (2, -12), (3,  -11)          ]))

dofus_map.add_map(-3, -12, MapNode(-3, -12, "Cimetière d'Astrub", [(-4, -12),  (-3, -13), (-2,  -12), (-3, -11)]))
dofus_map.add_map(-2, -12, MapNode(-2, -12, "Cimetière d'Astrub", [(-3, -12),  (-2, -13), (-1,  -12), (-2, -11)]))
dofus_map.add_map(-1, -12, MapNode(-1, -12, "Cimetière d'Astrub", [(-2, -12),  (-1, -13), (0,  -12), (-1, -11)]))
dofus_map.add_map(-0, -12, MapNode(-0, -12, "Cimetière d'Astrub", [(-1, -12),  (-0, -13), (1,  -12), (-0, -11)]))
dofus_map.add_map(1, -12, MapNode(1, -12, "Cimetière d'Astrub", [(0, -12),  (1, -13), (2,  -12), (1, -11)]))
dofus_map.add_map(2, -12, MapNode(2, -12, "Cimetière d'Astrub", [(1, -12),  (2, -13), (3,  -12), (2, -11)]))

dofus_map.add_map(-3, -13, MapNode(-3, -13, "Cimetière d'Astrub", [(-4, -13),  (-3, -14), (-2,  -13), (-3, -12)]))
dofus_map.add_map(-2, -13, MapNode(-2, -13, "Cimetière d'Astrub", [(-3, -13),  (-2, -14), (-1,  -13), (-2, -12)]))
dofus_map.add_map(-1, -13, MapNode(-1, -13, "Cimetière d'Astrub", [(-2, -13),  (-1, -14), (0,  -13), (-1, -12)]))
dofus_map.add_map(-0, -13, MapNode(-0, -13, "Cimetière d'Astrub", [(-1, -13),  (-0, -14), (1,  -13), (-0, -12)]))
dofus_map.add_map(1, -13, MapNode(1, -13, "Cimetière d'Astrub", [(0, -13),  (1, -14), (2,  -13), (1, -12)]))
dofus_map.add_map(2, -13, MapNode(2, -13, "Cimetière d'Astrub", [(1, -13),  (2, -14), (3,  -13), (2, -12)]))

dofus_map.add_map(-3, -14, MapNode(-3, -14, "Cimetière d'Astrub", [(-4, -14),  (-3, -15), (-2,  -14), (-3, -13)]))
dofus_map.add_map(-2, -14, MapNode(-2, -14, "Cimetière d'Astrub", [(-3, -14),  (-2, -15), (-1,  -14), (-2, -13)]))
dofus_map.add_map(-1, -14, MapNode(-1, -14, "Cimetière d'Astrub", [(-2, -14),  (-1, -15), (0,  -14), (-1, -13)]))
dofus_map.add_map(-0, -14, MapNode(-0, -14, "Cimetière d'Astrub", [(-1, -14),  (-0, -15), (1,  -14), (-0, -13)]))
dofus_map.add_map(1, -14, MapNode(1, -14, "Cimetière d'Astrub", [(0, -14),  (1, -15), (2,  -14), (1, -13)]))
dofus_map.add_map(2, -14, MapNode(2, -14, "Cimetière d'Astrub", [(1, -14),  (2, -15), (3,  -14), (2, -13)]))

dofus_map.add_map(-3, -15, MapNode(-3, -15, "Foret d'Astrub", [(-4, -15),  (-3, -16), (-2, -15), (-3, -14)]))
dofus_map.add_map(-2, -15, MapNode(-2, -15, "Foret d'Astrub", [(-3, -15),  (-2, -16), (-1, -15), (-2, -14)]))
dofus_map.add_map(-1, -15, MapNode(-1, -15, "Foret d'Astrub", [(-2, -15),  (-1, -16), (0,  -15), (-1, -14)]))
dofus_map.add_map(0,  -15, MapNode(0,  -15, "Foret d'Astrub", [(-1, -15),  (0, -16),  (1,  -15), (0,  -14)]))

dofus_map.add_map(-3, -16, MapNode(-3, -16, "Foret d'Astrub", [(-4, -16),  (-3, -17), (-2, -16), (-3, -15)]))
dofus_map.add_map(-2, -16, MapNode(-2, -16, "Foret d'Astrub", [(-3, -16),  (-2, -17), (-1, -16), (-2, -15)]))
dofus_map.add_map(-1, -16, MapNode(-1, -16, "Foret d'Astrub", [(-2, -16),  (-1, -17), (0,  -16), (-1, -15)]))
dofus_map.add_map(0,  -16, MapNode(0,  -16, "Foret d'Astrub", [(-1, -16),  (0, -17),  (1,  -16), (0,  -15)]))
##
dofus_map.add_map(-3, -17, MapNode(-3, -17, "Foret d'Astrub", [(-4, -17),  (-3, -18), (-2, -17), (-3, -16)]))
dofus_map.add_map(-2, -17, MapNode(-2, -17, "Foret d'Astrub", [(-3, -17),  (-2, -18), (-1, -17), (-2, -16)]))
dofus_map.add_map(-1, -17, MapNode(-1, -17, "Foret d'Astrub", [(-2, -17),  (-1, -18), (0,  -17), (-1, -16)]))
dofus_map.add_map(0,  -17, MapNode(0,  -17, "Foret d'Astrub", [(-1, -17),  (0, -18),  (1,  -17), (0,  -16)]))

dofus_map.add_map(-3, -18, MapNode(-3, -18, "Foret d'Astrub", [(-4, -18),  (-3, -19), (-2, -18), (-3, -17)]))
dofus_map.add_map(-2, -18, MapNode(-2, -18, "Foret d'Astrub", [(-3, -18),  (-2, -19), (-1, -18), (-2, -17)]))
dofus_map.add_map(-1, -18, MapNode(-1, -18, "Foret d'Astrub", [(-2, -18),  (-1, -19), (0,  -18), (-1, -17)]))
dofus_map.add_map(0,  -18, MapNode(0,  -18, "Foret d'Astrub", [(-1, -18),  (0, -19),  (1,  -18), (0,  -17)]))

dofus_map.add_map(-3, -19, MapNode(-3, -19, "Foret d'Astrub", [(-4, -19),  (-3, -20), (-2, -19), (-3, -18)]))
dofus_map.add_map(-2, -19, MapNode(-2, -19, "Foret d'Astrub", [(-3, -19),  (-2, -20), (-1, -19), (-2, -18)]))
dofus_map.add_map(-1, -19, MapNode(-1, -19, "Foret d'Astrub", [(-2, -19),  (-1, -20), (0,  -19), (-1, -18)]))
dofus_map.add_map(0,  -19, MapNode(0,  -19, "Foret d'Astrub", [(-1, -19),  (0, -20),  (1,  -19), (0,  -18)]))

dofus_map.add_map(-3, -20, MapNode(-3, -20, "Foret d'Astrub", [(-4, -20),  (-3, -21), (-2, -20), (-3, -19)]))
dofus_map.add_map(-2, -20, MapNode(-2, -20, "Foret d'Astrub", [(-3, -20),  (-2, -21), (-1, -20), (-2, -19)]))
dofus_map.add_map(-1, -20, MapNode(-1, -20, "Foret d'Astrub", [(-2, -20),  (-1, -21), (0,  -20), (-1, -19)]))
dofus_map.add_map(0,  -20, MapNode(0,  -20, "Foret d'Astrub", [(-1, -20),  (0, -21),  (1,  -20), (0,  -19)]))

dofus_map.add_map(-3, -21, MapNode(-3, -21, "Foret d'Astrub", [(-4, -21),  (-3, -22), (-2, -21), (-3, -20)]))
dofus_map.add_map(-2, -21, MapNode(-2, -21, "Foret d'Astrub", [(-3, -21),  (-2, -22), (-1, -21), (-2, -20)]))
dofus_map.add_map(-1, -21, MapNode(-1, -21, "Foret d'Astrub", [(-2, -21),  (-1, -22), (0,  -21), (-1, -20)]))
dofus_map.add_map(0,  -21, MapNode(0,  -21, "Foret d'Astrub", [(-1, -21),  (0, -22),  (1,  -21), (0,  -20)]))

dofus_map.add_map(-3, -22, MapNode(-3, -22, "Foret d'Astrub", [(-4, -22), (-3, -23), (-2, -22), (-3, -21)]))
dofus_map.add_map(-2, -22, MapNode(-2, -22, "Foret d'Astrub", [(-3, -22), (-2, -23), (-1, -22), (-2, -21)]))
dofus_map.add_map(-1, -22, MapNode(-1, -22, "Foret d'Astrub", [(-2, -22), (-1, -23), (0,  -22), (-1, -21)]))
dofus_map.add_map(0,  -22, MapNode(0,  -22, "Foret d'Astrub", [(-1, -22), (0, -23),  (1,  -22), (0,  -21)]))
dofus_map.add_map(1,  -22, MapNode(1,  -22, "Foret d'Astrub", [(0, -22),  (1, -23),  (2,  -22), (1,  -21)]))
dofus_map.add_map(2,  -22, MapNode(2,  -22, "Foret d'Astrub", [(1, -22),  (2, -23),  (3,  -22), (2,  -21)]))

dofus_map.add_map(-2, -23, MapNode(-2, -23, "Foret d'Astrub", [(-3, -23), (-2, -24), (-1, -23), (-2, -22)]))
dofus_map.add_map(-1, -23, MapNode(-1, -23, "Foret d'Astrub", [(-2, -23), (-1, -24), (0,  -23), (-1, -22)]))
dofus_map.add_map(0,  -23, MapNode(0,  -23, "Foret d'Astrub", [(-1, -23), (0, -24),  (1,  -23), (0,  -22)]))
dofus_map.add_map(1,  -23, MapNode(1,  -23, "Foret d'Astrub", [(0, -23),  (1, -24),  (2,  -23), (1,  -22)]))
dofus_map.add_map(2,  -23, MapNode(2,  -23, "Foret d'Astrub", [(1, -23),  (2, -24),  (3,  -23), (2,  -22)]))

dofus_map.add_map(-2, -24, MapNode(-2, -24, "Foret d'Astrub", [(-3, -24), (-2, -25), (-1, -24), (-2, -23)]))
dofus_map.add_map(-1, -24, MapNode(-1, -24, "Foret d'Astrub", [(-2, -24), (-1, -25), (0,  -24), (-1, -23)]))
dofus_map.add_map(0,  -24, MapNode(0,  -24, "Foret d'Astrub", [(-1, -24), (0, -25),  (1,  -24), (0,  -23)]))
dofus_map.add_map(1,  -24, MapNode(1,  -24, "Foret d'Astrub", [(0, -24),  (1, -25),  (2,  -24), (1,  -23)]))
dofus_map.add_map(2,  -24, MapNode(2,  -24, "Foret d'Astrub", [(1, -24),  (2, -25),  (3,  -24), (2,  -23)]))

dofus_map.add_map(-2, -25, MapNode(-2, -25, "Foret d'Astrub", [(-3, -25), (-2, -26), (-1, -25), (-2, -24)]))
dofus_map.add_map(-1, -25, MapNode(-1, -25, "Foret d'Astrub", [(-2, -25), (-1, -26), (0,  -25), (-1, -24)]))
dofus_map.add_map(0,  -25, MapNode(0,  -25, "Foret d'Astrub", [(-1, -25), (0, -26),  (1,  -25), (0,  -24)]))
dofus_map.add_map(1,  -25, MapNode(1,  -25, "Foret d'Astrub", [(0, -25),  (1, -26),  (2,  -25), (1,  -24)]))
dofus_map.add_map(2,  -25, MapNode(2,  -25, "Foret d'Astrub", [(1, -25),  (2, -26),  (3,  -25), (2,  -24)]))

dofus_map.add_map(-2, -26, MapNode(-2, -26, "Foret d'Astrub", [(-3, -26), (-2, -27), (-1, -26), (-2, -25)]))
dofus_map.add_map(-1, -26, MapNode(-1, -26, "Foret d'Astrub", [(-2, -26), (-1, -27), (0,  -26), (-1, -25)]))
dofus_map.add_map(0,  -26, MapNode(0,  -26, "Foret d'Astrub", [(-1, -26), (0, -27),  (1,  -26), (0,  -25)]))
dofus_map.add_map(1,  -26, MapNode(1,  -26, "Foret d'Astrub", [(0, -26),  (1, -27),  (2,  -26), (1,  -25)]))
dofus_map.add_map(2,  -26, MapNode(2,  -26, "Foret d'Astrub", [(1, -26),  (2, -27),  (3,  -26), (2,  -25)]))

dofus_map.add_map(-2, -27, MapNode(-2, -27, "Foret d'Astrub", [(-3, -27), (-2, -28), (-1, -27), (-2, -26)]))
dofus_map.add_map(-1, -27, MapNode(-1, -27, "Foret d'Astrub", [(-2, -27), (-1, -28), (0,  -27), (-1, -26)]))
dofus_map.add_map(0,  -27, MapNode(0,  -27, "Foret d'Astrub", [(-1, -27), (0, -28),  (1,  -27), (0,  -26)]))
dofus_map.add_map(1,  -27, MapNode(1,  -27, "Foret d'Astrub", [(0, -27),  (1, -28),  (2,  -27), (1,  -26)]))
dofus_map.add_map(2,  -27, MapNode(2,  -27, "Foret d'Astrub", [(1, -27),  (2, -28),  (3,  -27), (2,  -26)]))

dofus_map.add_map(-2, -28, MapNode(-2, -28, "Foret d'Astrub", [(-3, -28), (-2, -29), (-1, -28), (-2, -27)]))
dofus_map.add_map(-1, -28, MapNode(-1, -28, "Foret d'Astrub", [(-2, -28),            (0,  -28), (-1, -27)]))
dofus_map.add_map(0,  -28, MapNode(0,  -28, "Foret d'Astrub", [(-1, -28),            (1,  -28), (0,  -27)]))
dofus_map.add_map(1,  -28, MapNode(1,  -28, "Foret d'Astrub", [(0, -28),             (2,  -28), (1,  -27)]))
dofus_map.add_map(2,  -28, MapNode(2,  -28, "Foret d'Astrub", [(1, -28),  (2, -29),  (3,  -28), (2,  -27)]))

dofus_map.add_map(-2, -29, MapNode(-2, -29, "Foret d'Astrub", [(-3, -29), (-2, -30), (-1, -29), (-2, -28)]))
dofus_map.add_map(2,  -29, MapNode(2,  -29, "Foret d'Astrub", [           (2, -30),  (3,  -29), (2,  -28)]))
dofus_map.add_map(2,  -30, MapNode(2,  -30, "Foret d'Astrub", [                      (3,  -30), (2,  -29)]))

dofus_map.add_map(-1, -29, MapNode(-1, -29, "Tainéla", [(-2, -29), (-1, -30), (0,  -29)           ]))
dofus_map.add_map(0,  -29, MapNode(0,  -29, "Tainéla", [(-1, -29), (0, -30),  (1,  -29)           ]))
dofus_map.add_map(1,  -29, MapNode(1,  -29, "Tainéla", [(0, -29),  (1, -30),                      ]))

dofus_map.add_map(-2, -30, MapNode(-2, -30, "Tainéla", [           (-2, -31), (-1,  -30), (-2, -29)]))
dofus_map.add_map(-1, -30, MapNode(-1, -30, "Tainéla", [(-2, -30), (-1, -31), (0,  -30), (-1, -29)]))
dofus_map.add_map(0,  -30, MapNode(0,  -30, "Tainéla", [(-1, -30), (0, -31),  (1,  -30), (0,  -29)]))
dofus_map.add_map(1,  -30, MapNode(1,  -30, "Tainéla", [(0, -30),  (1, -31),             (1,  -29)]))

dofus_map.add_map(-2, -31, MapNode(-2, -31, "Tainéla", [           (-2, -32), (-1,  -31), (-2, -30)]))
dofus_map.add_map(-1, -31, MapNode(-1, -31, "Tainéla", [(-2, -31), (-1, -32), (0,  -31), (-1, -30)]))
dofus_map.add_map(0,  -31, MapNode(0,  -31, "Tainéla", [(-1, -31), (0, -32),  (1,  -31), (0,  -30)]))
dofus_map.add_map(1,  -31, MapNode(1,  -31, "Tainéla", [(0, -31),  (1, -32),  (2,  -31), (1,  -30)]))
dofus_map.add_map(2,  -31, MapNode(2,  -31, "Tainéla", [(1, -31),  (2, -32),                      ]))

dofus_map.add_map(-2, -32, MapNode(-2, -32, "Tainéla", [                      (-1,  -32), (-2, -31)]))
dofus_map.add_map(-1, -32, MapNode(-1, -32, "Tainéla", [(-2, -32), (-1, -33), (0,  -32), (-1, -31)]))
dofus_map.add_map(0,  -32, MapNode(0,  -32, "Tainéla", [(-1, -32), (0, -33),  (1,  -32), (0,  -31)]))
dofus_map.add_map(1,  -32, MapNode(1,  -32, "Tainéla", [(0, -32),  (1, -33),  (2,  -32), (1,  -31)]))
dofus_map.add_map(2,  -32, MapNode(2,  -32, "Tainéla", [(1, -32),  (2, -33),  (3,  -32), (2,  -31)]))
dofus_map.add_map(3,  -32, MapNode(3,  -32, "Tainéla", [(2, -32),  (3, -33),  (4,  -32), (3,  -31)]))
dofus_map.add_map(4,  -32, MapNode(4,  -32, "Tainéla", [(3, -32),                        (4,  -31)]))

dofus_map.add_map(-1, -33, MapNode(-1, -33, "Tainéla", [                      (0,  -33), (-1, -32)]))
dofus_map.add_map(0,  -33, MapNode(0,  -33, "Tainéla", [(-1, -33), (0, -34),  (1,  -33), (0,  -32)]))
dofus_map.add_map(1,  -33, MapNode(1,  -33, "Tainéla", [(0, -33),  (1, -34),  (2,  -33), (1,  -32)]))
dofus_map.add_map(2,  -33, MapNode(2,  -33, "Tainéla", [(1, -33),  (2, -34),  (3,  -33), (2,  -32)]))
dofus_map.add_map(3,  -33, MapNode(3,  -33, "Tainéla", [(2, -33),                        (3,  -32)]))

dofus_map.add_map(0,  -34, MapNode(0,  -34, "Tainéla", [                      (1,  -34), (0,  -33)]))
dofus_map.add_map(1,  -34, MapNode(1,  -34, "Tainéla", [(0, -34),             (2,  -34), (1,  -33)]))
dofus_map.add_map(2,  -34, MapNode(2,  -34, "Tainéla", [(1, -34),                        (2,  -33)]))

dofus_map.add_map(3,  -31, MapNode(3,  -31, "Champs d'Astrub", [           (3, -32),  (4,  -31), (3,  -30)]))
dofus_map.add_map(4,  -31, MapNode(4,  -31, "Champs d'Astrub", [(3, -31),  (4, -32),  (5,  -31), (4,  -30)]))
dofus_map.add_map(5,  -31, MapNode(5,  -31, "Champs d'Astrub", [(4, -31),                        (5,  -30)]))

dofus_map.add_map(3,  -30, MapNode(3,  -30, "Champs d'Astrub", [(2, -30), (3, -31), (4,  -30), (3,  -29)]))
dofus_map.add_map(4,  -30, MapNode(4,  -30, "Champs d'Astrub", [(3, -30), (4, -31), (5,  -30), (4,  -29)]))
dofus_map.add_map(5,  -30, MapNode(5,  -30, "Champs d'Astrub", [(4, -30), (5, -31), (6,  -30), (5,  -29)]))
dofus_map.add_map(6,  -30, MapNode(6,  -30, "Champs d'Astrub", [(5, -30),                      (6,  -29)]))

dofus_map.add_map(3,  -29, MapNode(3,  -29, "Champs d'Astrub", [(2, -29), (3, -30), (4,  -29), (3,  -28)]))
dofus_map.add_map(4,  -29, MapNode(4,  -29, "Champs d'Astrub", [(3, -29), (4, -30), (5,  -29), (4,  -28)]))
dofus_map.add_map(5,  -29, MapNode(5,  -29, "Champs d'Astrub", [(4, -29), (5, -30), (6,  -29), (5,  -28)]))
dofus_map.add_map(6,  -29, MapNode(6,  -29, "Champs d'Astrub", [(5, -29), (6, -30),            (6,  -28)]))

dofus_map.add_map(3,  -28, MapNode(3,  -28, "Champs d'Astrub", [(2, -28), (3, -29), (4,  -28), (3,  -27)]))
dofus_map.add_map(4,  -28, MapNode(4,  -28, "Champs d'Astrub", [(3, -28), (4, -29), (5,  -28), (4,  -27)]))
dofus_map.add_map(5,  -28, MapNode(5,  -28, "Champs d'Astrub", [(4, -28), (5, -29), (6,  -28), (5,  -27)]))
dofus_map.add_map(6,  -28, MapNode(6,  -28, "Champs d'Astrub", [(5, -28), (6, -29), (7,  -28), (6,  -27)]))
dofus_map.add_map(7,  -28, MapNode(7,  -28, "Champs d'Astrub", [(6, -28),           (8,  -28), (7,  -27)]))

dofus_map.add_map(3,  -27, MapNode(3,  -27, "Champs d'Astrub", [(2, -27), (3, -28), (4,  -27), (3,  -26)]))
dofus_map.add_map(4,  -27, MapNode(4,  -27, "Champs d'Astrub", [(3, -27), (4, -28), (5,  -27), (4,  -26)]))
dofus_map.add_map(5,  -27, MapNode(5,  -27, "Champs d'Astrub", [(4, -27), (5, -28), (6,  -27), (5,  -26)]))
dofus_map.add_map(6,  -27, MapNode(6,  -27, "Champs d'Astrub", [(5, -27), (6, -28), (7,  -27), (6,  -26)]))
dofus_map.add_map(7,  -27, MapNode(7,  -27, "Champs d'Astrub", [(6, -27), (7, -28),            (7,  -26)])) # staircase to go right

dofus_map.add_map(3,  -26, MapNode(3,  -26, "Champs d'Astrub", [(2, -26), (3, -27), (4,  -26), (3,  -25)]))
dofus_map.add_map(4,  -26, MapNode(4,  -26, "Champs d'Astrub", [(3, -26), (4, -27), (5,  -26), (4,  -25)]))
dofus_map.add_map(5,  -26, MapNode(5,  -26, "Champs d'Astrub", [(4, -26), (5, -27), (6,  -26), (5,  -25)]))
dofus_map.add_map(6,  -26, MapNode(6,  -26, "Champs d'Astrub", [(5, -26), (6, -27), (7,  -26), (6,  -25)]))
dofus_map.add_map(7,  -26, MapNode(7,  -26, "Champs d'Astrub", [(6, -26), (7, -27), (8,  -26), (7,  -25)])) 

dofus_map.add_map(3,  -25, MapNode(3,  -25, "Champs d'Astrub", [(2, -25), (3, -26), (4,  -25), (3,  -24)]))
dofus_map.add_map(4,  -25, MapNode(4,  -25, "Champs d'Astrub", [(3, -25), (4, -26), (5,  -25), (4,  -24)]))
dofus_map.add_map(5,  -25, MapNode(5,  -25, "Champs d'Astrub", [(4, -25), (5, -26), (6,  -25), (5,  -24)]))
dofus_map.add_map(6,  -25, MapNode(6,  -25, "Champs d'Astrub", [(5, -25), (6, -26), (7,  -25), (6,  -24)]))
dofus_map.add_map(7,  -25, MapNode(7,  -25, "Champs d'Astrub", [(6, -25), (7, -26),            (7,  -24)])) 

dofus_map.add_map(3,  -24, MapNode(3,  -24, "Champs d'Astrub", [(2, -24), (3, -25), (4,  -24), (3,  -23)]))
dofus_map.add_map(4,  -24, MapNode(4,  -24, "Champs d'Astrub", [(3, -24), (4, -25), (5,  -24), (4,  -23)]))
dofus_map.add_map(5,  -24, MapNode(5,  -24, "Champs d'Astrub", [(4, -24), (5, -25), (6,  -24), (5,  -23)]))
dofus_map.add_map(6,  -24, MapNode(6,  -24, "Champs d'Astrub", [(5, -24), (6, -25), (7,  -24), (6,  -23)]))
dofus_map.add_map(7,  -24, MapNode(7,  -24, "Champs d'Astrub", [(6, -24), (7, -25), (8,  -24), (7,  -23)])) 
dofus_map.add_map(8,  -24, MapNode(8,  -24, "Champs d'Astrub", [(7, -24),           (9,  -24), (8,  -23)])) 
dofus_map.add_map(9,  -24, MapNode(9,  -24, "Champs d'Astrub", [(8, -24), (9, -25),            (9,  -23)])) 

dofus_map.add_map(3,  -23, MapNode(3,  -23, "Champs d'Astrub", [(2, -23), (3, -24), (4,  -23), (3,  -22)]))
dofus_map.add_map(4,  -23, MapNode(4,  -23, "Champs d'Astrub", [(3, -23), (4, -24), (5,  -23), (4,  -22)]))
dofus_map.add_map(5,  -23, MapNode(5,  -23, "Champs d'Astrub", [(4, -23), (5, -24), (6,  -23), (5,  -22)]))
dofus_map.add_map(6,  -23, MapNode(6,  -23, "Champs d'Astrub", [(5, -23), (6, -24), (7,  -23), (6,  -22)]))
dofus_map.add_map(7,  -23, MapNode(7,  -23, "Champs d'Astrub", [(6, -23), (7, -24), (8,  -23), (7,  -22)])) 
dofus_map.add_map(8,  -23, MapNode(8,  -23, "Champs d'Astrub", [(7, -23), (8, -24), (9,  -23), (8,  -22)])) 
dofus_map.add_map(9,  -23, MapNode(9,  -23, "Champs d'Astrub", [(8, -23), (9, -24),            (9,  -22)]))  # staircase to go right

dofus_map.add_map(3,  -22, MapNode(3,  -22, "Champs d'Astrub", [(2, -22), (3, -23), (4,  -22), (3,  -21)]))
dofus_map.add_map(4,  -22, MapNode(4,  -22, "Champs d'Astrub", [(3, -22), (4, -23), (5,  -22), (4,  -21)]))
dofus_map.add_map(5,  -22, MapNode(5,  -22, "Champs d'Astrub", [(4, -22), (5, -23), (6,  -22), (5,  -21)]))
dofus_map.add_map(6,  -22, MapNode(6,  -22, "Champs d'Astrub", [(5, -22), (6, -23), (7,  -22), (6,  -21)]))
dofus_map.add_map(7,  -22, MapNode(7,  -22, "Champs d'Astrub", [(6, -22), (7, -23), (8,  -22), (7,  -21)])) 
dofus_map.add_map(8,  -22, MapNode(8,  -22, "Champs d'Astrub", [(7, -22), (8, -23), (9,  -22), (8,  -21)])) 
dofus_map.add_map(9,  -22, MapNode(9,  -22, "Champs d'Astrub", [(8, -22), (9, -23),            (9,  -21)])) 


dofus_map.add_map(10,  -22, MapNode(10,  -22, "Calanques d'Astrub", [           (10, -23), (11,  -22)            ])) 
dofus_map.add_map(11,  -22, MapNode(11,  -22, "Calanques d'Astrub", [(10, -22), (11, -23), (12,  -22), (11,  -21)])) 
dofus_map.add_map(12,  -22, MapNode(12,  -22, "Calanques d'Astrub", [(11, -22), (12, -23),                       ])) 

dofus_map.add_map(10,  -23, MapNode(10,  -23, "Calanques d'Astrub", [           (10, -24), (11,  -23), (10,  -22)])) # staircase to go left
dofus_map.add_map(11,  -23, MapNode(11,  -23, "Calanques d'Astrub", [(10, -23), (11, -24), (12,  -23), (11,  -22)])) 
dofus_map.add_map(12,  -23, MapNode(12,  -23, "Calanques d'Astrub", [(11, -23), (12, -24),             (12,  -22)])) 

dofus_map.add_map(10,  -24, MapNode(10,  -24, "Calanques d'Astrub", [           (10, -25), (11,  -24), (10,  -23)])) 
dofus_map.add_map(11,  -24, MapNode(11,  -24, "Calanques d'Astrub", [(10, -24), (11, -25), (12,  -24), (11,  -23)])) 
dofus_map.add_map(12,  -24, MapNode(12,  -24, "Calanques d'Astrub", [(11, -24), (12, -25),             (12,  -23)])) 

dofus_map.add_map(8,  -25, MapNode(8,  -25, "Calanques d'Astrub", [           (8,  -26), (9,  -25),          ]))
dofus_map.add_map(9,  -25, MapNode(9,  -25, "Calanques d'Astrub", [(8,  -25), (9,  -26), (10, -25), (9,  -24)]))
dofus_map.add_map(10, -25, MapNode(10, -25, "Calanques d'Astrub", [(9,  -25), (10, -26), (11, -25), (10, -24)]))
dofus_map.add_map(11, -25, MapNode(11, -25, "Calanques d'Astrub", [(10, -25), (11, -26), (12, -25), (11, -24)])) 
dofus_map.add_map(12, -25, MapNode(12, -25, "Calanques d'Astrub", [(11, -25), (12, -26),            (12, -24)])) 

dofus_map.add_map(8,  -26, MapNode(8,  -26, "Calanques d'Astrub", [(7,  -26), (8,  -27), (9,  -26), (8,  -25)]))
dofus_map.add_map(9,  -26, MapNode(9,  -26, "Calanques d'Astrub", [(8,  -26), (9,  -27), (10, -26), (9,  -25)]))
dofus_map.add_map(10, -26, MapNode(10, -26, "Calanques d'Astrub", [(9,  -26), (10, -27), (11, -26), (10, -25)]))
dofus_map.add_map(11, -26, MapNode(11, -26, "Calanques d'Astrub", [(10, -26), (11, -27), (12, -26), (11, -25)])) 
dofus_map.add_map(12, -26, MapNode(12, -26, "Calanques d'Astrub", [(11, -26), (12, -27),            (12, -25)])) 

dofus_map.add_map(8,  -27, MapNode(8,  -27, "Calanques d'Astrub", [           (8,  -28), (9,  -27), (8,  -26)])) # staircase to go left
dofus_map.add_map(9,  -27, MapNode(9,  -27, "Calanques d'Astrub", [(8,  -27), (9,  -28), (10, -27), (9,  -26)]))
dofus_map.add_map(10, -27, MapNode(10, -27, "Calanques d'Astrub", [(9,  -27), (10, -28), (11, -27), (10, -26)]))
dofus_map.add_map(11, -27, MapNode(11, -27, "Calanques d'Astrub", [(10, -27), (11, -28), (12, -27), (11, -26)])) 
dofus_map.add_map(12, -27, MapNode(12, -27, "Calanques d'Astrub", [(11, -27), (12, -28), (13, -27), (12, -26)])) 
dofus_map.add_map(13, -27, MapNode(13, -27, "Calanques d'Astrub", [(12, -27), (13, -28),                     ])) 

dofus_map.add_map(8,  -28, MapNode(8,  -28, "Calanques d'Astrub", [(7,  -28), (8,  -29), (9,  -28), (8,  -27)]))
dofus_map.add_map(9,  -28, MapNode(9,  -28, "Calanques d'Astrub", [(8,  -28), (9,  -29), (10, -28), (9,  -27)]))
dofus_map.add_map(10, -28, MapNode(10, -28, "Calanques d'Astrub", [(9,  -28), (10, -29), (11, -28), (10, -27)]))
dofus_map.add_map(11, -28, MapNode(11, -28, "Calanques d'Astrub", [(10, -28),            (12, -28), (11, -27)])) 
dofus_map.add_map(12, -28, MapNode(12, -28, "Calanques d'Astrub", [(11, -28),            (13, -28), (12, -27)])) 
dofus_map.add_map(13, -28, MapNode(13, -28, "Calanques d'Astrub", [(12, -28),                       (13, -27)])) 

dofus_map.add_map(8,  -29, MapNode(8,  -29, "Calanques d'Astrub", [                      (9,  -29), (8,  -28)]))
dofus_map.add_map(9,  -29, MapNode(9,  -29, "Calanques d'Astrub", [(8,  -29),            (10, -29), (9,  -28)]))
dofus_map.add_map(10, -29, MapNode(10, -29, "Calanques d'Astrub", [(9,  -29),                       (10, -28)]))

# dofus_map.visualize()

## All the free map is done.

# from short_path import a_star_map, show_map_with_path

# start = (10, -29)
# goal = (12, -21)

# path, visited = a_star_map(dofus_map, start, goal)
# print("Path:", path)
# print("Visited:", visited)

# show_map_with_path(dofus_map, path)



def get_item_coordinates(item_name: str) -> dict:
    """
    Retrieve the coordinates of a specified item on the map.
    Args:
        item_name (str): The name of the item to find coordinates for.
    Returns:
        dict: A dictionary containing the coordinates of the specified item and the associated quantity.
    """

    if item_name == "ble":
        return bles


bles = {
    (-28, -45): 1,
    (-28, -44): 5,
    (-22, -44): 1,
    (-27, -43): 8,
    (-26, -43): 1,
    (-24, -43): 1,
    (-26, -42): 1,
    (-24, -42): 1,
    (-26, -41): 1,
    (-24, -41): 11,
    (-29, -40): 4,
    (-25, -40): 7,
    (-24, -40): 8,
    (-23, -41): 18,
    (-21, -40): 4,
    (-26, -39): 9,
    (-24, -39): 17,
    (-26, -38): 5,
    (3, -30): 3,
    (4, -30): 23,
    (5, -30): 2,
    (6, -30): 6,
    (4, -29): 14,
    (6, -29): 12,
    (6, -28): 8,
    (4, -27): 11,
    (5, -25): 10,
    (7, -25): 9,
    (3, -23): 7,
    (4, -23): 1,
    (7, -23): 11,
    (9, -23): 6,
    (3, -22): 10,
    (5, -22): 9,
    (6, -21): 5,
    (7, -21): 5,
    (5, -14): 1,
    (3, -9): 3,
    (5, -9): 2,
    (5, 4): 1,
    (8, 5): 11,
    (9, 5): 17,
    (4, 6): 2,
    (5, 6): 14,
    (6, 6): 15,
    (8, 6): 11,
    (9, 6): 26,
    (5, 7): 1,
    (6, 8): 1,
    (9, 8): 10,
    (10, 8): 16,
    (7, 9): 3,
    (8, 9): 6,
    (9, 9): 6,
    (8, 11): 2,
    (13, 14): 8,
    (9, 21): 3,
    (3, 2): 1,
    (1, 23): 8,
    (2, 23): 10,
    (3, 23): 7,
    (0, 24): 4,
    (2, 24): 10,
    (3, 24): 7,
    (3, 26): 2,
    (3, 27): 1,
    (1, 28): 12,
    (4, 28): 2,
    (5, 31): 1,
    (-16, -13): 5,
 }

# bles = {    (6, -28): 8,
#     (4, -27): 11,
#     (5, -25): 10,
#     (7, -25): 9,
#     (3, -23): 7,
#     (4, -23): 1,
#     (7, -23): 11,
#     (9, -23): 6,
#     (3, -22): 10,
#     (5, -22): 9,
#     (6, -21): 5,}
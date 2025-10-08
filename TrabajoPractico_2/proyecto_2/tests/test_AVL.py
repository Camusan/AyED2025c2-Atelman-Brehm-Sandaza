# Archivo de test para realizar pruebas unitarias del modulo1


import unittest
from modules.AVL import ArbolAVL
import numpy as np


class Testabb(unittest.TestCase):
    
    def setUp(self):
        self.avl = ArbolAVL()
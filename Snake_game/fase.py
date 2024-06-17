import pygame
import random

class Fase:
    def __init__(self, numero, largura, altura, tamanho_do_quadrado):
        self.numero = numero
        self.largura = largura
        self.altura = altura
        self.tamanho_do_quadrado = tamanho_do_quadrado
        self.obstaculos = self.criar_obstaculos()

    def criar_obstaculos(self):
        obstaculos = []

        if self.numero > 1:
          
            num_obstaculos = 30
            
            if self.numero >= 3:
                num_obstaculos += 10

            for _ in range(num_obstaculos):
                x = random.randrange(0, self.largura, self.tamanho_do_quadrado)
                y = random.randrange(0, self.altura, self.tamanho_do_quadrado)
                obstaculos.append([x, y])

        return obstaculos

    def desenhar(self, tela):
        for pos in self.obstaculos:
            pygame.draw.rect(tela, (192, 192, 192), [pos[0], pos[1], self.tamanho_do_quadrado, self.tamanho_do_quadrado])

import pygame
import random

class Comida:
    def __init__(self, largura, altura, tamanho_quadrado, obstaculos):
        self.obstaculos = obstaculos
        self.imagem = pygame.image.load('img/Apple_JE3_BE3.png').convert_alpha()  # Carrega a imagem da comida
        self.imagem = pygame.transform.scale(self.imagem, (tamanho_quadrado, tamanho_quadrado))  # Redimensiona a imagem
        self.posicao = self.criar_comida(largura, altura, tamanho_quadrado)
    
    def criar_comida(self, largura, altura, tamanho_quadrado):
        while True:
            x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * tamanho_quadrado
            y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * tamanho_quadrado
            if [x, y] not in self.obstaculos:
                return [x, y]
    
    def desenhar(self, tela):
        tela.blit(self.imagem, (self.posicao[0], self.posicao[1]))


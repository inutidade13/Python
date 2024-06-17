import pygame

class Snake:
    def __init__(self, altura, largura, tamanho_quadrado):
        self.corpo = [[altura // 2, largura // 2]]  # Posição inicial da cobra
        self.direcao = [0, 0]  # Direção inicial da cobra
        self.crescer = False  # Indicador se a cobra deve crescer
        self.altura = altura
        self.largura = largura
        self.tamanho_quadrado = tamanho_quadrado

    def mover(self):
        nova_cabeca = [self.corpo[0][0] + self.direcao[0], self.corpo[0][1] + self.direcao[1]]

        # Verificar se a cobra ultrapassou os limites da tela
        if nova_cabeca[0] >= self.largura:
            nova_cabeca[0] = 0
        elif nova_cabeca[0] < 0:
            nova_cabeca[0] = self.largura - self.tamanho_quadrado
        elif nova_cabeca[1] >= self.altura:
            nova_cabeca[1] = 0
        elif nova_cabeca[1] < 0:
            nova_cabeca[1] = self.altura - self.tamanho_quadrado

        self.corpo.insert(0, nova_cabeca)

        if not self.crescer:
            self.corpo.pop()
        else:
            self.crescer = False

    def mudar_direcao(self, direcao):
        if direcao == pygame.K_DOWN and self.direcao != [0, -self.tamanho_quadrado]:
            self.direcao = [0, self.tamanho_quadrado]
        elif direcao == pygame.K_UP and self.direcao != [0, self.tamanho_quadrado]:
            self.direcao = [0, -self.tamanho_quadrado]
        elif direcao == pygame.K_RIGHT and self.direcao != [-self.tamanho_quadrado, 0]:
            self.direcao = [self.tamanho_quadrado, 0]
        elif direcao == pygame.K_LEFT and self.direcao != [self.tamanho_quadrado, 0]:
            self.direcao = [-self.tamanho_quadrado, 0]

    def desenhar(self, tela):
        for parte in self.corpo:
            pygame.draw.rect(tela, (0, 255, 0), [parte[0], parte[1], self.tamanho_quadrado, self.tamanho_quadrado])

    def colidiu(self):
        if self.corpo[0] in self.corpo[1:]:
            return True
        return False

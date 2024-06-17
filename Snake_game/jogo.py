import pygame
from snake import Snake
from comida import Comida
from fase import Fase
from menu import Menu  # Certifique-se de que o arquivo menu.py está no mesmo diretório

class Jogo:
    def __init__(self, largura, altura, tamanho_do_quadrado, imagem_de_fundo):
        pygame.init()
        pygame.display.set_caption("Jogo da Cobrinha")

        self.largura = largura
        self.altura = altura
        self.tamanho_do_quadrado = tamanho_do_quadrado

        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.relogio = pygame.time.Clock()

        self.fase_atual = 1
        self.pontuacao = 0

        self.menu = Menu(self.tela, self.largura, self.altura, imagem_de_fundo)
        self.exibir_menu()

    def exibir_menu(self):
        menu_ativo = self.menu.exibir()
        if not menu_ativo:
            self.proxima_fase()
            self.rodar()

    def proxima_fase(self):
        self.fase = Fase(self.fase_atual, self.largura, self.altura, self.tamanho_do_quadrado)
        self.cobrinha = Snake(self.altura, self.largura, self.tamanho_do_quadrado)
        self.comida = Comida(self.largura, self.altura, self.tamanho_do_quadrado, self.fase.obstaculos)

    def desenhar_pontuacao(self):
        fonte = pygame.font.SysFont("Helvetica", 30)
        texto = fonte.render(f"Pontos: {self.pontuacao} - Fase: {self.fase_atual}", True, (255, 0, 0))
        self.tela.blit(texto, [10, 10])

    def rodar(self):
        fim_do_jogo = False
        while not fim_do_jogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fim_do_jogo = True
                elif event.type == pygame.KEYDOWN:
                    self.cobrinha.mudar_direcao(event.key)

            self.cobrinha.mover()

            if self.cobrinha.corpo[0][0] == self.comida.posicao[0] and self.cobrinha.corpo[0][1] == self.comida.posicao[1]:
                self.cobrinha.crescer = True
                self.comida = Comida(self.largura, self.altura, self.tamanho_do_quadrado, self.fase.obstaculos)
                self.pontuacao += 1

            if self.cobrinha.colidiu() or self.cobrinha.corpo[0] in self.fase.obstaculos:
                fim_do_jogo = True

            if self.pontuacao >= 5:
                self.fase_atual += 1
                self.proxima_fase()
                self.pontuacao = 0
                

            self.tela.fill((0, 0, 0))
            self.fase.desenhar(self.tela)
            self.cobrinha.desenhar(self.tela)
            self.comida.desenhar(self.tela)
            self.desenhar_pontuacao()

            pygame.display.update()
            self.relogio.tick(10)

        pygame.quit()

if __name__ == "__main__":
    largura, altura = 1200, 600
    tamanho_do_quadrado = 20
    imagem_de_fundo = ""  
    jogo = Jogo(largura, altura, tamanho_do_quadrado, imagem_de_fundo)

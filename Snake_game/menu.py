import pygame

class Menu:
    def __init__(self, tela, largura, altura, imagem_de_fundo):
        self.tela = tela
        self.largura = largura
        self.altura = altura
        self.imagem_de_fundo = pygame.image.load('img\cobraimagem.png')
        self.imagem_de_fundo = pygame.transform.scale(self.imagem_de_fundo, (self.largura, self.altura))

    def exibir(self):
        menu_ativo = True
        while menu_ativo:
            self.tela.blit(self.imagem_de_fundo, (0, 0))
            fonte = pygame.font.SysFont("Helvetica", 50)
            titulo = fonte.render("Jogo da Cobrinha", True, (255, 255, 255))
            self.tela.blit(titulo, (self.largura // 2 - titulo.get_width() // 2, self.altura // 4))

            fonte_opcao = pygame.font.SysFont("Helvetica", 40)
            opcao_jogar = fonte_opcao.render("Jogar", True, (0, 255, 0))
            opcao_sair = fonte_opcao.render("Sair", True, (255, 0, 0))

            jogar_rect = opcao_jogar.get_rect(center=(self.largura // 2, self.altura // 2))
            sair_rect = opcao_sair.get_rect(center=(self.largura // 2, self.altura // 2 + 50))

            self.tela.blit(opcao_jogar, jogar_rect)
            self.tela.blit(opcao_sair, sair_rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if jogar_rect.collidepoint(event.pos):
                        menu_ativo = False
                    elif sair_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()

        return menu_ativo

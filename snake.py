import pygame
import random

pygame.init()
pygame.font.init()

janela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Jogo da cobra -- FEITO POR VINICIUS BATISTELLA")

cor_cobra = (0, 128, 0)
velocidade = 20
x = 290
y = 290
largura_comida = 10
altura_comida = 10
fps = pygame.time.Clock()
cobra = [(290, 290)]
comer = False
rodando = True
morte  = False
direcao = "direita"


ultimo_movimento = pygame.time.get_ticks()

def limites(x, y):
    if x < 0 or x > 580 or y < 0 or y > 580:
        return x, y, True
    return x, y, False

def tela_morte():
    fonte = pygame.font.SysFont("Arial", 20)
    texto_morte= fonte.render("Você morreu, pressione qualquer tecla para reiniciar", True, (255, 0, 0))
    janela.blit(texto_morte, (50, 300))

def comida():
    x_aleatorio = random.randint(0, 580)
    y_aleatorio = random.randint(0, 580)
    return x_aleatorio, y_aleatorio

x_comida, y_comida = comida()
react_comida = pygame.Rect(x_comida, y_comida, largura_comida, altura_comida)

while rodando:

    for jogo in pygame.event.get():
        if jogo.type == pygame.QUIT:
            rodando = False
        if jogo.type == pygame.KEYDOWN:
            if morte:
                morte = False
                x = 290
                y = 290
                x_comida, y_comida = comida()
                react_comida = pygame.Rect(x_comida, y_comida, largura_comida, altura_comida)
                cobra = [(290, 290)]

    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - ultimo_movimento >= 100:
        ultimo_movimento = tempo_atual
        janela.fill((0, 0, 0))
        movimento =  False
        if not morte:
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_UP] or tecla[pygame.K_w]:
                if direcao != "baixo":
                    direcao = "cima"

            if tecla[pygame.K_DOWN] or tecla[pygame.K_s]:
                if direcao != "cima":
                    direcao = "baixo"

            if tecla[pygame.K_LEFT] or tecla[pygame.K_a]:
                if direcao != "direita":
                    direcao = "esquerda"

            if tecla[pygame.K_RIGHT] or tecla[pygame.K_d]:
                if direcao != "esquerda":
                    direcao = "direita"
            if direcao == "cima":
                y -= velocidade
                movimento = True
            if direcao == "baixo":
                y += velocidade
                movimento = True
            if direcao == "esquerda":
                x -= velocidade
                movimento = True
            if direcao == "direita":
                x += velocidade
                movimento = True

            react_cobra = pygame.Rect(x, y, 20, 20)
            x, y, morte = limites(x, y)
            if movimento:
                cobra.append((x, y))
                for i in range(len(cobra) - 1):
                    if  cobra[i] == (x, y, morte):
                        morte = True
            if movimento:
                if react_cobra.colliderect(react_comida):
                    x_comida, y_comida = comida()
                    react_comida = pygame.Rect(x_comida, y_comida, largura_comida, altura_comida)
                    comer = True


            if movimento:
                if not comer:
                    cobra.pop(0)
                else:
                    comer = False
    
            
            if morte == True:
                cobra.clear()

            for adicionar in cobra:
                pygame.draw.rect(janela, cor_cobra, (adicionar[0], adicionar[1], 20, 20))
        pygame.draw.rect(janela, (255, 0, 0), (x_comida, y_comida, largura_comida, altura_comida))
    
    if morte:
        tela_morte()

    fps.tick(60)
    pygame.display.flip()
import pygame
import random

pygame.init()
pygame.font.init()

#CONFIGURANDO A JANELA
janela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Jogo da cobra -- FEITO POR VINICIUS BATISTELLA")

#VARIAVEIS UTILIZADAS NO JOGO
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
pontuacao = 0

ultimo_movimento = pygame.time.get_ticks()

# FUNÇÕES DO JOGO

# SE BATEU OU NÃO NA BORDA
def limites(x, y):
    if x < 0 or x > 580 or y < 0 or y > 580:
        return True
    return False

# MORTE E REINICIO DO JOGO
def tela_morte():
    fonte = pygame.font.SysFont("Arial", 20)
    texto_morte= fonte.render("Você morreu, pressione qualquer tecla para reiniciar", True, (255, 0, 0))
    #CENTRALIZAR NA TELA
    retangulo_texto = texto_morte.get_rect(center=(300, 300))
    janela.blit(texto_morte, retangulo_texto)

# POSSIÇÃO ALEATORIA 
def comida():
    x_aleatorio = random.randrange(0, 600, 20) + 5
    y_aleatorio = random.randrange(0, 600, 20) + 5
    return x_aleatorio, y_aleatorio

x_comida, y_comida = comida()
react_comida = pygame.Rect(x_comida, y_comida, largura_comida, altura_comida)

# COMEÇO DO JOGO
while rodando:

    for jogo in pygame.event.get():
        if jogo.type == pygame.QUIT: # FECHA O JOGO QUANDO CLICA NO X
            rodando = False # FECHA O JOGO QUANDO CLICA NO X
        if jogo.type == pygame.KEYDOWN:
            if morte: # PRA REINICIAR O JOGO QUANDO MORREU
                morte = False
                x = 290
                y = 290
                x_comida, y_comida = comida() # GERA NOVA COMIDA
                react_comida = pygame.Rect(x_comida, y_comida, largura_comida, altura_comida) # GERA NOVA COMIDA
                cobra = [(290, 290)] # REINICIA A COBRA
                pontuacao  = 0 

    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - ultimo_movimento >= 100: # MOVIMENTO DA COBRA A CADA 100ms
        ultimo_movimento = tempo_atual
        janela.fill((0, 0, 0)) # LIMPAR A TELA
        movimento =  False
        if not morte:
            tecla = pygame.key.get_pressed() # QUAL TECLA TA PRESSIONADA
            if tecla[pygame.K_UP] or tecla[pygame.K_w]: # DIREÇÃO DA COBRA  E  NÃO PODER DEIXAR A COBRA IR PARA O LADO OPOSTO
                if direcao != "baixo":
                    direcao = "cima"

            if tecla[pygame.K_DOWN] or tecla[pygame.K_s]: # DIREÇÃO DA COBRA  E  NÃO PODER DEIXAR A COBRA IR PARA O LADO OPOSTO
                if direcao != "cima":
                    direcao = "baixo"

            if tecla[pygame.K_LEFT] or tecla[pygame.K_a]: # DIREÇÃO DA COBRA  E  NÃO PODER DEIXAR A COBRA IR PARA O LADO OPOSTO
                if direcao != "direita":
                    direcao = "esquerda"

            if tecla[pygame.K_RIGHT] or tecla[pygame.K_d]: # DIREÇÃO DA COBRA  E  NÃO PODER DEIXAR A COBRA IR PARA O LADO OPOSTO
                if direcao != "esquerda":
                    direcao = "direita"
            if direcao == "cima": # MOVIMENTO DA COBRA
                y -= velocidade
                movimento = True
            if direcao == "baixo": # MOVIMENTO DA COBRA
                y += velocidade
                movimento = True
            if direcao == "esquerda": # MOVIMENTO DA COBRA
                x -= velocidade
                movimento = True
            if direcao == "direita": # MOVIMENTO DA COBRA
                x += velocidade
                movimento = True

            morte = limites(x, y)

            react_cobra = pygame.Rect(x, y, 20, 20)
            
            if movimento:
                cobra.append((x, y))
                for i in range(len(cobra) - 1): # VERIFICA SE A COBRA BATEU NELA MESMA
                    if  cobra[i] == (x, y):
                        morte = True
            if movimento:
                if react_cobra.colliderect(react_comida):
                    x_comida, y_comida = comida()
                    react_comida = pygame.Rect(x_comida, y_comida, largura_comida, altura_comida)
                    comer = True
                    pontuacao += 27

            if movimento:
                if not comer:
                    cobra.pop(0) # SE Não TIVER COMIDO  REMOVE O MAIS ANTIGO
                else:
                    comer = False # FAZ O CONTRARIO  E A COBRA CRESCE
    
            
            if morte == True:
                cobra.clear()

            for adicionar in cobra:
                pygame.draw.rect(janela, cor_cobra, (adicionar[0], adicionar[1], 20, 20))
        pygame.draw.rect(janela, (255, 0, 0), (x_comida, y_comida, largura_comida, altura_comida))

    # PONTUAÇÃO
    fonte = pygame.font.SysFont("Calibri", 20)
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
    janela.blit(texto_pontuacao, (10, 10))

    if morte:
        tela_morte()

    fps.tick(60) # FAZ O JOGO RODAR A 60 FPS
    pygame.display.flip()
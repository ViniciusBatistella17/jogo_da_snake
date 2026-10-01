import pygame

pygame.init()
pygame.font.init()

janela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Jogo da cobra -- FEITO POR VINICIUS BATISTELLA")

cor_cobra = (0, 128, 0)
velocidade = 1
x = 290
y = 290

rodando = True
morte  = False

def limites(x, y):
    if x < 0 or x > 580 or y < 0 or y > 580:
        morte = True
    else:
        morte = False

    return x, y, morte

def tela_morte():
    fonte = pygame.font.SysFont("Arial", 20)
    texto_morte= fonte.render("Você morreu, pressione qualquer tecla para reiniciar", True, (255, 0, 0))
    janela.blit(texto_morte, (50, 300))


while rodando:

    for jogo in pygame.event.get():
        if jogo.type == pygame.QUIT:
            rodando = False
        if jogo.type == pygame.KEYDOWN:
            if morte:
                morte = False
                x = 290
                y = 290
    
    janela.fill((0, 0, 0))
    if not morte:
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_UP] or tecla[pygame.K_w]:
            y -= velocidade
        if tecla[pygame.K_DOWN] or tecla[pygame.K_s]:
            y += velocidade
        if tecla[pygame.K_LEFT] or tecla[pygame.K_a]:
            x -= velocidade
        if tecla[pygame.K_RIGHT] or tecla[pygame.K_d]:
            x += velocidade
        

    
        x, y, morte = limites(x, y)
        pygame.draw.rect(janela, cor_cobra, (x, y, 20, 20))
    
    if morte:
        tela_morte()

    pygame.display.flip()
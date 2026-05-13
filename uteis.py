import pygame

def gradienteRotavel(
        tela,                       # Window to draw
        cores,                      # Tuple of two colors (xxx,xxx,xxx) )
        rotacao,                    # angle of rotation in degrees
        altura,                     # height of gratient considering 0 degrees
        largura,                    # width of gratient considering 0 degrees
        centro,                     # Position of the center of the gradient
        eixo= pygame.Vector2(0,0),  # Difference between the gradient rectangle center and the rotation axis.
        line=3                      # Thickness of each line in gradient
    ):
    # Correction for visual bugs.(Only in certain angles)
    altura = altura-line
    largura = largura-line

    #create a parameter for color transition
    rate = (
        float(cores[0][0]-cores[1][0])/altura,
        float(cores[0][1]-cores[1][1])/altura,
        float(cores[0][2]-cores[1][2])/altura
    )

    for l in range(altura):
        color = (                                       # 
                min(max(cores[1][0]+(rate[0]*(l)),0),255),    # 
                min(max(cores[1][1]+(rate[1]*(l)),0),255),    # 
                min(max(cores[1][2]+(rate[2]*(l)),0),255)     # 
            )
        p1 = pygame.Vector2(-largura/2+eixo.x,l-altura/2+eixo.y)
        p2 = pygame.Vector2(+largura/2+eixo.x,l-altura/2+eixo.y)
        linha = [p.rotate(rotacao)+centro+eixo for p in [p1,p2]]
        pygame.draw.polygon(tela, color, linha, width=3)

# A test for gradienteRotavel. It creates a gradient square in the middle of screen that rotates around its on center.
'''
tela = pygame.display.set_mode((500,500))
screen = pygame.display.set_mode((500,500),pygame.SCALED | pygame.RESIZABLE)

WIDTH, HEIGHT = 500, 500
clock = pygame.time.Clock()
running = True
atual = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    screen.fill("white")
    gradienteRotavel(
        tela=screen,
        cores=(
            (0,0,255),
            (255,0,0)
        ),
        eixo=pygame.Vector2(0,0),
        centro=pygame.Vector2(250,250),
        rotacao=atual, # <------------------ make it rotate
        altura=400,
        largura=400
    )
    pygame.display.flip()
    dt = clock.tick(30) / 1000
    atual += 1
pygame.quit()
'''
from curses import BUTTON1_RELEASED
import pygame as pg
import random 
pg.init()

class Bola:
    def __init__(self, x, y, padre,  color = (255, 255, 255), radio = 10):
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.vx = 1
        self.vy = 1
        self.padre = padre


    def mover(self):
        self.x += self.vx 
        self.y += self.vy

        if self.x <= self.radio or self.x >= self.padre.get_width() - self.radio:
            self.vx *= -1

        #if self.radio >= self.x >= limDer - self.radio:

        if self.y <= self.radio or self.y >= self.padre.get_height() - self.radio:
            self.vy *= -1

    def dibujar(self):
        pg.draw.circle(self.padre, self.color, (self.x, self.y), self.radio)

class Game:
    def __init__(self, ancho=600, alto=800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.bolas = []
        for i in range(random.randint(2,10)): 
            radio = random.randint(5, 50)
            x = random.randint(radio, ancho - radio)
            y = random.randint(radio, alto - radio)
            color = (random.randint(0, 255),
                     random.randint(0, 255),
                     random.randint(0, 255)
                    )

            bola = Bola(x, y, self.pantalla, color, radio)
            bola.vx = random.randint(5,15) * random.choice([-1, 1])
            bola.vy = random.randint(5,15) * random.choice([-1, 1])
            self.bolas.append(bola)
        """
        for i in range(random.randint(2, 10)):
            radio = random.randint(5, 50)
            self.bolas.append(Bola(random.randint(radio, ancho - radio),
                                   random.randint(radio, alto - radio),
                                   self.pantalla,
                                   (random.randint(0, 255),
                                    random.randint(0, 255),
                                    random.randint(0, 255)),
                                   radio))
            self.bolas[i].vx = random.randint(5,15) * random.choice[(-1, 1)]
            self.bolas[i].vy = random.randint(5,15) * random.choice[(-1, 1)]
        """

        """
        for i... random de numero de bolas:
            self.bolas.append(nueva_bola)
            diferentes colores
            diferentes tamaños
            diferentes velocidades
        """


    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

            self.pantalla.fill((255, 0, 0))    

            for bola in self.bolas:
                bola.mover()
                bola.dibujar()

            pg.display.flip()

    
if __name__ == '__main__':
    pg.init()

    game = Game()
    game.bucle_ppal()

    pg.quit()
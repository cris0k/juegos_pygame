from curses import BUTTON1_RELEASED
import pygame as pg

pg.init()

class Vigneta: #Super class con todo definido para luego ser elegido y utilizado por las otras class
    def __init__(self, padre, x, y, ancho, alto, color = (255, 255, 255)):
        self.padre = padre
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.alto = alto
        self.vx = 0
        self.vy = 0

    def dibujar(self):
        pass

    def mover(self):
        pass

class Ladrillo(Vigneta):
    def dibujar(self):
        pg.draw.rect(self.padre, self.color, (self.x, self.y, self.ancho, self.alto))

    def comprobarToque(self, bola):
        #hago cosas al tocarme la bola
        pass


class Raqueta(Vigneta):
    def __init__(self, padre, x, y, ancho, alto, color = (255, 255, 0)):
        super().__init__(padre, x, y, ancho, alto, color)
        self.vx = 5 # como en Vigneta decimos que la velocidad es 0, hay que sobreescribirla

    def dibujar(self):
        pg.draw.rect(self.padre, self.color, (self.x, self.y, self.ancho, self.alto))

    def mover(self):
        teclas = pg.key.get_pressed() 
        if teclas[pg.K_LEFT]:
            self.x -= self.vx
        if teclas[pg.K_RIGHT]:
            self.x += self.vx

 # Que el rectangulo no pase del borde de la pantalla del juego
        if self.x <= 0:
            self.x = 0
        if self.x + self.ancho >= self.padre.get_width():
            self.x = self.padre.get_width() - self.ancho

class Bola:
    def __init__(self, padre, x, y, color = (255, 255, 255), radio = 10) :
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.vx = 5
        self.vy = 5
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

    def compruebaChoque(self, otro):
        if (self.x - self.radio in range(otro.x, otro.x + otro.ancho) or \
            self.x + self.radio in range(otro.x, otro.x + otro.ancho)) and \
           (self.y - self.radio in range(otro.y, otro.y + otro.alto) or \
            self.y + self.radio in range(otro.y, otro.y + otro.alto)):
           
           self.vy *= -1



class Game:
    def __init__(self, ancho=600, alto=800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.bola = Bola(self.pantalla, ancho // 2, alto //2 )
        self.raqueta = Raqueta(self.pantalla, ancho//2, alto // 2, 100, 20)
        self.ladrillo = Ladrillo(self.pantalla, 10, 10, 100, 50)
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


    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

        # Una de las posibles soluciones a que el recrangulo se mueva al dejar pulsada la tecla
                """
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_LEFT:
                        self.raqueta.vx = -5
                    if evento.key == pg.K_RIGHT:
                        self.raqueta.vx = 5
                if evento.type == pg.KEYUP:
                    if evento.key in (pg.K_LEFT, pg.K_RIGHT):
                        self.raqueta.vx = 0
                """
            

            self.pantalla.fill((255, 0, 0))    

            self.ladrillo.mover()
            self.bola.mover()
            self.raqueta.mover()
            self.bola.compruebaChoque(self.raqueta)
            self.bola.dibujar()
            self.raqueta.dibujar()
            self.ladrillo.dibujar()

            pg.display.flip()

    
if __name__ == '__main__':
    pg.init()

    game = Game()
    game.bucle_ppal()

    pg.quit()
    

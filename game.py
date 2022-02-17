import pygame as pg
pg.init()

class Ball:
    def __init__(self, x, y, color = (255,255,255), radio= 10): #Atributos por defecto. Si mas tarde no lo definimos,estos seran los atributos
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.vx = 1 #velocidad x hacia donde va a ir
        self.vy = 1 #velocidad y hacia donde va a ir
    
    def move(self, right_limit, inferior_limit):
        self.x += self.vx
        self.y += self.vy


        if self.x <= self.radio or self.x >=right_limit - self.radio:
            self.vx *= -1
            #if self.radio >= self.x >= right_limit - self.radio:  esto es lo mismo que lo de arriba

        if self.y <= self.radio or self.y >= inferior_limit - self.radio:
            self.vy *= -1

    def draw (self, surface): # Paint the circle
        pg.draw.circle(surface, self.color,(self.x, self.y), self.radio) 


class Game:
    def __init__(self, width=600, height=800):
        self.screen = pg.display.set_mode((width, height))
        self.ball = Ball(width // 2, height // 2, (255, 255,0)) # Division entera de la posicion(sin decimales) + cambio de color de bola

    def main_loop(self):
        game_over = False

        while not game_over:
            events = pg.event.get()

            for event in events:
                if event.type == pg.QUIT:
                    game_over = True
            
            self.ball.move(self.screen.get_width(), self.screen.get_height()) #get width y get height esta predefinido por pygame
            self.screen.fill((255, 0, 0))
            self.ball.draw(self.screen)
            

            pg.display.flip()

if __name__== '__main__':
    pg.init()

    game = Game() # crea el juego
    game.main_loop() # hace funcionar el juego

    pg.quit()

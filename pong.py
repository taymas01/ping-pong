from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Pingpong')

background = transform.scale(image.load('background.jpg'), (700, 500))
clock = time.Clock()
FPS = 60

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, x, y, widht, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widht, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update_l(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 435:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

left = Player('racket.png', 0, 200,30,100, 5)
right = Player('racket.png', 670, 200,30,100, 5)
ball = Gamesprite('tenis_ball.png', 100, 100,50,50, 5)

game = True
while game:
    print(clock.get_fps())
    for e in event.get():
        if e.type==QUIT:
            game = False
    
    
    
    window.blit(background, (0, 0))
  
    ball.reset()

    left.reset()
    left.update_l()        
    
    right.reset()
    right.update_r()

    clock.tick(FPS)
    display.update()

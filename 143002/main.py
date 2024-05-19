from pygame 
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
   def update_r(self):
       keys = key.get_pressed()
       
 #метод "выстрел" (используем место игрока, чтобы создать там пулю)
       
    bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, -15)
    bullets.add(bullet)


#класс спрайта-врага  
class Enemy(GameSprite):
   #движение врага
   def update(self):
       self.rect.y += self.speed
       global lost
       #исчезает, если дойдет до края экрана
       if self.rect.y > win_height:
           self.rect.x = randint(80, win_width - 80)
           self.rect.y = 0
           lost = lost + 1
           self.speed = randint(1, 5)

class Bullet(GameSprite):
    def update(self):                   
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

bullets = sprite.Group()
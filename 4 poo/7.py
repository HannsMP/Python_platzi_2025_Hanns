from typing import List
from os import system
from time import sleep
from random import randint

system('cls')

## recursos screen
emoji_sea = '🟦'
emoji_border = '⬜'

## recursos jugador
emoji_player_A = '🟧' 
emoji_player_B = '🟩'

# indica que el enemigo destruyo tu buque
emoji_destroy_A = '🟠' 
emoji_destroy_B = '🟢'

# a lo kamikase, te auto destruiste un buque
emoji_boom = '🟫'

# la bomba cae en el mar
emoji_swirl = '🌀'

class Screen:
    def __init__(self, width=1, heigh=1, border=False):
        self.width = max(1, width)
        self.heigh = max(1, heigh)
        if(border):
            self.border = [emoji_border for w in range(self.width+2)]
        else:
            self.border = None
        self.reset()
        
    def reset(self):
        self.pixels = [
            [emoji_sea for w in range(self.width)]
                for h in range(self.heigh)
        ]
  
    def draw(self):
        system('cls')
        sep = ''
        
        if self.border:
            print(*self.border, sep=sep)
            
            for row in self.pixels:
                print(emoji_border, *row, emoji_border, sep=sep)
                
            print(*self.border, sep=sep)
                
        else:
            for row in self.pixels:
                print(*row, sep=sep)
        
        print('')
                    
    def set_pixel(self, x, y, value = ''):
        self.pixels[y][x] = value
        
    def is_empty(self, x, y):
        return self.pixels[y][x] == emoji_sea
            
    def valid_x(self, x):
        return 0 <= x and x < self.width
    
    def valid_y(self, y):
        return 0 <= y and y < self.heigh
            
class Vessel:
    def __init__(self, size, is_vertical, x, y):
        self.size = min(max(1, size), 3)
        self.is_vertical = is_vertical
        self.x = x
        self.y = y
        self.life = True
        self.my_pixels: List[List[int]] = []
        
        self.my_pixels.append([x, y])
        for i in range(1, self.size):
            if is_vertical:
                self.my_pixels.append([x + i, y])
                self.my_pixels.append([x - 1, y])
                
            else:
                self.my_pixels.append([x, y + i])
                self.my_pixels.append([x, y - i])
                                
class PLayer:
    def __init__(self, emoji='', destroy='', is_bot=False):
        self.emoji = emoji
        self.emoji_destroy = destroy
        self.is_bot = is_bot
        self.vessels:List[Vessel] = []
        self.lifes = 0
        
    def show_life(self):
        print(f"{self.emoji} tienes {self.lifes} buques")
    
    def show_dead(self):
        if self.is_bot:
            print(f"{self.emoji} 💀 Perdiste, {self.lifes} de {len(self.vessels)} buques sobrevivientes [Bot]")
        else:
            print(f"{self.emoji} 💀 Perdiste, {self.lifes} de {len(self.vessels)} buques sobrevivientes")
        
    def  show_win(self):    
        if self.is_bot:
            print(f"{self.emoji} 🏆 Ganaste, {self.lifes} de {len(self.vessels)} buques sobrevivientes [Bot]")
        else:
            print(f"{self.emoji} 🏆 Ganaste, {self.lifes} de {len(self.vessels)} buques sobrevivientes")
    
    def create_vessel(self, vessel:Vessel, screen:Screen):
        self.vessels.append(vessel)
        
        for [x, y] in vessel.my_pixels:
            screen.set_pixel(x, y, self.emoji)
            
        if vessel.life:
            self.lifes+=1
        
    def detroy_vessel(self, vessel:Vessel, screen:Screen, emoji=''):
        if not vessel.life:
            return
                
        for [x, y] in vessel.my_pixels:
            screen.set_pixel(x, y, emoji)
        
        vessel.life = False
        self.lifes-=1
        
    def is_my_vessel(self, x, y):
        for vessel in self.vessels:
            if not vessel.life:
                continue
            
            if [x, y] in vessel.my_pixels:
                return vessel

        return None
          
class Game:
    def __init__(self, width=10, heigh=10, show_border=False, playerA_is_bot=False, playerB_is_bot=True, waiting_time_remmember=False, count_vessel = 1):
        self.screen = Screen(width, heigh, show_border)
        self.playerA = PLayer(emoji_player_A, emoji_destroy_A, playerA_is_bot)
        self.playerB = PLayer(emoji_player_B, emoji_destroy_B, playerB_is_bot)
        self.count_vessel = count_vessel
        
        if waiting_time_remmember == True:
            self.waiting_time_remmember = 5
        elif 0 < waiting_time_remmember:
            self.waiting_time_remmember = max(1, waiting_time_remmember)
        else:
            self.waiting_time_remmember = False
                
    def run(self):
        for i in range(max(1, self.count_vessel)):
            for player in [self.playerA, self.playerB]:
                self.form_vessel(player)
                sleep(1)
        self.start()
                   
    def form_vessel(self, player:PLayer):
                   
        if player.is_bot:
            size = randint(1, 3)
            is_vertical = randint(1,2) == 1
   
        else:
            size = int(input(f"🤖 {player.emoji} Tamaño de buque (1-3): "))
            is_vertical = input(f"🤖 {player.emoji} Inclinacion del buque (H): ") == 'H'
         
        while True:
            
            if player.is_bot:
                x = randint(0, self.screen.width - 1)
                y = randint(0, self.screen.heigh - 1)
                
            else:
                x = int(input(f"🤖 {player.emoji} Coordenada X del buque (1-{self.screen.width}): ")) - 1
                y = int(input(f"🤖 {player.emoji} Coordenada Y del buque (1-{self.screen.heigh}): ")) - 1
                
            vessel = Vessel(size, is_vertical, x, y)
            
            is_valid = self.valid_vessel(vessel)
            
            if is_valid:
                self.set_vessel(player, vessel)
                self.screen.draw()
                break
            
            if not player.is_bot:
                print(f"⚠ La ubicacion ({x}, {y+1}) del buque no es valida")

    def valid_vessel (self, vessel:Vessel):
        
        for [x, y] in vessel.my_pixels:            
            if not (self.screen.valid_x(x) and self.screen.valid_y(y) and self.screen.is_empty(x, y)):
                return False

        return True
    
    def set_vessel (self, player:PLayer, vessel:Vessel):           
        player.create_vessel(vessel, self.screen)
        
    def start(self):
        while True:
            for [player_me, player_enemy] in [[self.playerA, self.playerB], [self.playerB, self.playerA]]:
                if player_me.is_bot:
                    x = randint(0, self.screen.width - 1)
                    y = randint(0, self.screen.heigh - 1)
                    
                else:
                    
                    self.screen.draw()
                    
                    if self.waiting_time_remmember:
                        for awaiting in range(self.waiting_time_remmember):
                            self.screen.draw()
                            print("Recuerda las coordenadas exactas")
                            print(f"  desaparecere en {self.waiting_time_remmember - awaiting}")
                            sleep(1)
                            
                            
                        system('cls')
                    
                    while True:
                        x = int(input(f"🤖 {player_me.emoji} Coordenada X de la bomba (1-{self.screen.width}): ")) - 1
                        y = int(input(f"🤖 {player_me.emoji} Coordenada Y de la bomba (1-{self.screen.heigh}): ")) - 1
                        
                        if self.screen.valid_x(x) and self.screen.valid_y(y):
                            break
                        
                is_vessel_enemy = player_enemy.is_my_vessel(x, y)
                is_vessel_me = player_me.is_my_vessel(x, y)
                                
                if is_vessel_enemy:
                    player_enemy.detroy_vessel(is_vessel_enemy, self.screen, player_enemy.emoji_destroy)
                elif is_vessel_me:
                    player_me.detroy_vessel(is_vessel_me, self.screen, emoji_boom)
                else:
                    self.screen.set_pixel(x, y, emoji_swirl)
                
                self.screen.draw()
                
                is_playerA_dead = self.playerA.lifes == 0
                is_playerB_dead = self.playerB.lifes == 0
                
                if is_playerA_dead:
                    self.playerB.show_win()
                    self.playerA.show_dead()
                    return
                
                if is_playerB_dead:
                    self.playerA.show_win()
                    self.playerB.show_dead()
                    return
                
                self.playerA.show_life()
                self.playerB.show_life()
                
                sleep(1)
                          
game = Game(
    width=20,
    heigh=20,
    show_border=True,
    playerA_is_bot=True,
    playerB_is_bot=True,
    waiting_time_remmember = 3,
    count_vessel = 5
)

game.run()
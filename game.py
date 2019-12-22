import sys
import pygame

Anim = []
tmp = [0, 0]
num = 1
level = 0
tmp_color = ''
ag = 0
tut = 0
re = 1
f_cnt = 0

aqua = (0, 255, 255)  # морская волна
black = (0, 0, 0)  # черный
blue = (0, 0, 255)  # синий
fuchsia = (255, 0, 255)  # фуксия
gray = (128, 128, 128)  # серый
green = (0, 128, 0)  # зеленый
lime = (0, 255, 0)  # цвет лайма
maroon = (128, 0, 0)  # темно-бордовый
navy_blue = (0, 0, 128)  # темно-синий
olive = (128, 128, 0)  # оливковый
purple = (128, 0, 128)  # фиолетовый
red = (255, 0, 0)  # красный
silver = (192, 192, 192)  # серебряный
teal = (0, 128, 128)  # зелено-голубой
white = (255, 255, 255)  # белый
yellow = (255, 255, 0)  # желтый
brown = (85, 55, 43) #коричневый

preDoor = [[7, 1],
[4, 1],
[10, 3],
[6, 4],
[1, 1],
[1, 6],
[3, 6]]

H = [[1, 1],
[4, 6],
[6, 4],
[4, 4],
[4, 8],
[6, 6],
[3, 2]]

Block = [[[[1], [1], [1], [1], [1], [1], [1], [1], [1]],
[[1], [0], [0], [2, red], [0], [1], [2, blue], [0], [1]],
[[1], [0], [0], [2, red], [0], [1], [2, blue], [0], [1]],
[[1], [0], [0], [2, red], [1], [0], [2, blue], [0], [1]],
[[1], [0], [0], [2, red], [0], [0], [2, blue], [0], [1]],
[[1], [0], [0], [2, red], [0], [0], [2, blue], [0], [1]],
[[1], [1], [1], [1], [1], [1], [1], [1], [1]]],

[[[1], [1], [1], [1], [1], [1], [1], [1]],
[[1], [1], [0], [0], [0], [0], [1], [1]],
[[1], [1], [1], [1], [0], [1], [1], [1]],
[[1], [1], [1], [1], [0], [0], [1], [1]],
[[1], [1], [0], [0], [0], [0], [1], [1]],
[[1], [1], [0], [0], [0], [1], [1], [1]],
[[1], [1], [0], [0], [0], [0], [1], [1]],
[[1], [1], [1], [1], [1], [1], [1], [1]]],

[[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
[[1], [0], [0], [0], [2, green], [2, green], [0], [2, green], [2, green], [1], [1], [1]],
[[1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1]],
[[1], [0], [0], [0], [0], [0], [2, green], [0], [2, silver], [2, silver], [0], [1]],
[[1], [0], [1], [1], [1], [1], [0], [0], [0], [0], [1], [1]],
[[1], [0], [1], [0], [0], [0], [0], [0], [0], [0], [1], [1]],
[[1], [0], [1], [0], [2, blue], [0], [0], [0], [0], [0], [0], [1]],
[[1], [0], [1], [2, blue], [2, blue], [0], [0], [0], [0], [0], [0], [1]],
[[1], [0], [0], [0], [1], [1], [1], [1], [1], [0], [0], [1]],
[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]],

[[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
[[1], [1], [0], [2, green], [0], [2, blue], [2, blue], [2, blue], [1], [1]],
[[1], [0], [0], [1], [0], [2, yellow], [0], [0], [1], [1]],
[[1], [0], [0], [1], [1], [1], [1], [2, blue], [1], [1]],
[[1], [0], [0], [0], [0], [1], [0], [2, blue], [0], [1]],
[[1], [0], [1], [0], [1], [1], [1], [2, blue], [0], [1]],
[[1], [0], [1], [0], [2, red], [0], [2, blue], [0], [0], [1]],
[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]],

[[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
[[1], [0], [0], [0], [0], [0], [1], [0], [0], [1]],
[[1], [0], [0], [0], [0], [0], [1], [0], [0], [1]],
[[1], [0], [0], [0], [0], [0], [1], [1], [1], [1]],
[[1], [0], [0], [0], [0], [0], [0], [0], [0], [1]],
[[1], [0], [0], [0], [0], [0], [1], [1], [1], [1]],
[[1], [0], [0], [0], [0], [0], [1], [0], [0], [1]],
[[1], [0], [0], [0], [0], [0], [1], [0], [0], [1]],
[[1], [0], [0], [0], [0], [0], [1], [0], [0], [1]],
[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]],

[[[1], [1], [1], [1], [1], [1], [1], [1]],
[[1], [0], [0], [0], [0], [2, fuchsia], [0], [1]],
[[1], [0], [0], [0], [0], [2, fuchsia], [2, fuchsia], [1]],
[[1], [0], [0], [0], [0], [0], [0], [1]],
[[1], [0], [0], [0], [0], [0], [0], [1]],
[[1], [2, lime], [2, lime], [0], [0], [0], [0], [1]],
[[1], [0], [2, lime], [0], [0], [0], [0], [1]],
[[1], [1], [1], [1], [1], [1], [1], [1]]],

[[[1], [1], [1], [1], [1], [1], [1]],
[[1], [1], [1], [0], [1], [1], [1]],
[[1], [0], [0], [0], [2, lime], [0], [1]],
[[1], [0], [0], [0], [0], [0], [1]],
[[1], [0], [0], [0], [0], [0], [1]],
[[1], [0], [2, lime], [2, lime], [2, lime], [0], [1]],
[[1], [0], [2, lime], [0], [2, lime], [0], [1]],
[[1], [1], [1], [1], [1], [1], [1]]]]

bucket = [[[4, 2, blue], [1, 5, red]],
[[5, 6, blue]],
[[9, 6, silver], [3, 3, green], [7, 4, blue]],
[[1, 6, green], [4, 2, red], [6, 2, blue], [5, 6, yellow]],
[[4, 1, green], [8, 4, red]],
[[1, 1, fuchsia], [6, 1, lime]],
[[3, 1, lime]]]

move = [
[],
[[5, 3, blue], [2, 4, blue], [3, 4, blue], [3, 5, blue], [4, 5, blue], [3, 6, blue], [4, 3, blue]],
[[6, 2, green], [7, 2, green], [7, 3, green], [8, 4, silver], [5, 5, blue], [6, 5, blue], [9, 5, silver], [6, 6, blue], [6, 7, blue], [7, 7, blue], [8, 7, blue]],
[[1, 3, green], [2, 3, green]],
[[3, 3, green], [4, 3, green], [5, 3, green], [3, 4, green], [5, 4, green], [6, 4, green], [3, 5, green], [4, 5, green], [5, 5, green], [3, 6, green], [5, 6, green], [3, 7, green],
[4, 7, green], [5, 7, green], [1, 2, red], [1, 3, red], [1, 4, red], [3, 1, red], [2, 4, red]],
[[2, 2, fuchsia], [2, 3, fuchsia], [3, 3, fuchsia], [3, 4, fuchsia], [4, 4, fuchsia], [4, 5, fuchsia], [5, 5, fuchsia], [5, 6, fuchsia], [6, 5, fuchsia], [3, 1, fuchsia],
[3, 6, fuchsia], [6, 4, fuchsia]],
[[2, 2, lime], [1, 3, lime], [2, 3, lime], [3, 3, lime], [4, 3, lime], [5, 3, lime], [2, 4, lime], [4, 4, lime], [1, 5, lime], [5, 5, lime]]]

Card = []
Bucket = []
Door = []
Move = []

def build(level, screen):
    for i in range(len(Block[level])):
        for j in range(len(Block[level][i])):
            if len(Block[level][i][j]) == 1 and Block[level][i][j][0] == 0:
                Card.append(floor_block(screen, j * 40, i * 40))
            elif len(Block[level][i][j]) == 1 and Block[level][i][j][0] == 1:
                Card.append(unbroken_block(screen, j * 40, i * 40))
            else:
                Card.append(usual_block(screen, Block[level][i][j][1], j * 40, i * 40))
    for i in (bucket[level]):
        Bucket.append(bucket1(screen, i[0] * 40, i[1] * 40, i[2]))
    for i in move[level]:
        Move.append(moving_block(screen, i[0] * 40, i[1] * 40, i[2]))
    Door.append(door(screen, preDoor[level][0] * 40, preDoor[level][1] * 40))

def draw(level):
    for i in Card:
        if (i.type == 0 or i.tmp == 1):
            i.blit_me()
    for i in Bucket:
        i.blit_me()
    for i in Anim:
        if i.wait <= 70:
            i.blit_me()
    for i in Move:
        if i.tmp == 1:
            i.blit_me()
    Door[0].blit_me()


class hero():
    def __init__(self, screen, x, y):
        self.screen = screen
        pic = pygame.image.load("C:/arcade/animation/right/Hero0.png")
        pic = pygame.transform.scale(pic, (40, 40))
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x * 40; self.rect.y = y * 40
        self.way = "right"
        self.tmp_block = False
    def animation1(self, word):
        global num
        pic = pygame.image.load("C:/arcade/animation/" + word + "/Hero" + str(num) + ".png");
        pic = pygame.transform.scale(pic, (40, 40))
        num = (num + 1) % 4
        self.image = pic
    def blit_me(self):
        self.screen.blit(self.image, self.rect)
    def check(self, tmp):
        for i in Card:
            if i.tmp != 0 and self.rect.x + tmp[0] * 40 == i.rect.x and self.rect.y + tmp[1] * 40 == i.rect.y:
                return False
        for i in range(len(Move)):
            if Move[i].tmp != 0 and self.rect.x + tmp[0] * 40 == Move[i].rect.x and self.rect.y + tmp[1] * 40 == Move[i].rect.y and not(Move[i].check(tmp)):
                return False
            if Move[i].tmp != 0 and self.rect.x + tmp[0] * 40 == Move[i].rect.x and self.rect.y + tmp[1] * 40 == Move[i].rect.y and re == 0:
                return False
            elif Move[i].tmp != 0 and self.rect.x + tmp[0] * 40 == Move[i].rect.x and self.rect.y + tmp[1] * 40 == Move[i].rect.y:
                self.tmp_block = i

        return True
    def update(self, level):
        global tmp, Anim
        way = ["bottom", "right", "", "left", "up"]
        word = way[2 - (tmp[0] * 1 + tmp[1] * 2)]
        if word != "":
            self.way = word
        if (tmp != [0, 0]):
            for i in range(4):
                if (self.check(tmp)):
                    for i in Anim:
                        for j in range(10):
                            i.update()
                    if (type(self.tmp_block) != bool):
                        Move[self.tmp_block].rect.x += 10 * tmp[0]
                        Move[self.tmp_block].rect.y += 10 * tmp[1]
                    draw(level)
                    self.animation1(word)
                    self.rect.x += 10 * tmp[0]
                    self.rect.y += 10 * tmp[1]
                    self.blit_me()
                    pygame.display.flip()
                    pygame.time.wait(80)
                else:
                    pic = pygame.image.load("C:/arcade/animation/" + word + "/Hero0.png")
                    pic = pygame.transform.scale(pic, (40, 40))
                    self.image = pic
        tmp = [0, 0]
        self.tmp_block = False

def upd(a):
    a[3] = 0
    return a

def upd1(a):
    a[3] = 50
    return a

def upd2(a):
    if (a[3] == 0):
        return a
    a[3] = 170
    return a


def upd3(a):
    if (a[3] == 0):
        return a
    a[3] = 110
    return a

def update1(a):
    for i in range(a.get_width()):
        for j in range(a.get_height()):
            if a.get_at((i, j))[3] != 0:
                a.set_at((i, j), upd2(a.get_at((i, j))))
    return a

def update(a, b):
    for i in range(b.get_width()):
        for j in range(b.get_height()):
            if b.get_at((i, j))[3] == 0:
                a.set_at((i, j), upd(a.get_at((i, j))))
            else:
                a.set_at((i, j), upd1(a.get_at((i, j))))
    return a


def update3(a, b):
    for i in range(b.get_width()):
        for j in range(b.get_height()):
            if b.get_at((i, j))[3] == 0:
                a.set_at((i, j), upd(a.get_at((i, j))))
            else:
                a.set_at((i, j), upd3(a.get_at((i, j))))
    return a

class usual_block:
    def __init__(self, screen, color, x, y):
        self.screen = screen
        pic = pygame.image.load("C:/arcade/blocks/usual.png")
        pic = pygame.transform.scale(pic, (40, 40))
        self.image = pic.convert_alpha()
        self.color = color
        self.rect = self.image.get_rect()
        self.rect.x = x; self.rect.y = y
        self.surf = pygame.Surface((40, 40)).convert_alpha()
        self.surf.fill(color)
        self.surf = update(self.surf, self.image)
        self.tmp = 1
        self.type = 2
        self.colored = False
    def blit_me(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.surf, (self.rect.x, self.rect.y))


class unbroken_block:
    def __init__(self, screen, x, y):
        self.screen = screen
        pic = pygame.image.load("C:/arcade/blocks/unbroken.png")
        pic = pygame.transform.scale(pic, (40, 40))
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x; self.rect.y = y
        self.tmp = 1
        self.type = 1
        self.colored = False
    def blit_me(self):
        self.screen.blit(self.image, self.rect)


class floor_block:
    def __init__(self, screen, x, y):
        self.screen = screen
        pic = pygame.image.load("C:/arcade/blocks/floor.png")
        pic = pygame.transform.scale(pic, (40, 40))
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x;
        self.rect.y = y
        self.type = 0
        self.colored = True
        self.tmp = 0
    def blit_me(self):
        self.screen.blit(self.image, self.rect)

class moving_block:
    def __init__(self, screen, x, y, color):
        self.screen = screen
        pic = pygame.image.load("C:/arcade/blocks/moving.png")
        pic = pygame.transform.scale(pic, (40, 40))
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x;
        self.rect.y = y
        self.type = 3
        self.colored = False
        self.color = color
        self.tmp = 1
        self.surf = pygame.Surface((40, 40)).convert_alpha()
        self.surf.fill(color)
        self.surf = update3(self.surf, self.image)
    def check(self, tmp):
        for i in Card:
            if i.type != 0 and i.tmp == 1 and self.rect.x + tmp[0] * 40 == i.rect.x and self.rect.y + tmp[1] * 40 == i.rect.y:
                return False
        for i in Move:
            if i.tmp == 1 and self.rect.x + tmp[0] * 40 == i.rect.x and self.rect.y + tmp[1] * 40 == i.rect.y:
                return False
        if self.rect.x + tmp[0] * 40 == Door[0].rect.x and self.rect.y + tmp[1] * 40 == Door[0].rect.y:
            return False
        for i in Bucket:
            if self.rect.x + tmp[0] * 40 == i.rect.x and self.rect.y + tmp[1] * 40 == i.rect.y:
                return False
        return True
    def blit_me(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.surf, (self.rect.x, self.rect.y))


def fill(image, color):
    for i in range(image.get_width()):
        for j in range(image.get_height()):
            if image.get_at((i, j)) == white:
                image.set_at((i, j), color)
    return image

def unfill(a):
    for i in range(a.image.get_width()):
        for j in range(a.image.get_height()):
            if a.image.get_at((i, j)) == a.color:
                a.image.set_at((i, j), brown)

class bucket1:
    def __init__(self, screen, x, y, color):
        self.screen = screen
        pic = pygame.image.load("C:/arcade/bucket/empty.png")
        pic = pygame.transform.scale(pic, (40, 40))
        pic = fill(pic, color)
        self.image = pic
        self.color = color
        self.rect = self.image.get_rect()
        self.rect.x = x; self.rect.y = y
    def blit_me(self):
        self.screen.blit(self.image, self.rect)

class ani:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.wait = 0
        pic = pygame.image.load("C:/arcade/animation/smoke/" + str(self.wait // 10 + 1) + ".png")
        pic = pygame.transform.scale(pic, (40, 40))
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x; self.rect.y = y
    def blit_me(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.wait += 1
        if (self.wait <= 70):
            pic = pygame.image.load("C:/arcade/animation/smoke/" + str(self.wait // 10 + 1) + ".png")
            pic = pygame.transform.scale(pic, (40, 40))
            self.image = pic

class door:
    def __init__(self, screen, x, y):
        self.screen = screen
        pic = pygame.image.load("C:/arcade/door/usual.png")
        pic = pygame.transform.scale(pic, (40, 40))
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x; self.rect.y = y
    def update(self):
        pic = pygame.image.load("C:/arcade/door/usual1.png")
        pic = pygame.transform.scale(pic, (40, 40))
        self.image = pic
    def blit_me(self):
        self.screen.blit(self.image, self.rect)

def conv(a):
    if a == "right":
        return [40, 0]
    if a == "left":
        return [-40, 0]
    if a == "up":
        return [0, -40]
    if a == "bottom":
        return [0, 40]

def win(a):
    if a.rect.x == Door[0].rect.x and a.rect.y == Door[0].rect.y:
        return True
    return False

class flying_window:
    def __init__(self, screen, text):
        self.screen = screen
        self.bg = pygame.transform.scale(pygame.image.load("C:/arcade/window.png"), (200, 100))
        self.rect = self.bg.get_rect()
        self.rect.x = -200
        self.rect.y = 100
        self.time = 0
        self.out = False
        fontObj = pygame.font.Font("C:/arcade/schrifts/1.otf", self.rect.width // len(text) + 7)
        self.textSurfaceObj = fontObj.render(text, True, black)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.x = (self.rect.width - self.textRectObj.width) / 2 + self.rect.x
        self.textRectObj.y = self.rect.y + (self.rect.height - self.textRectObj.height) // 2
    def blit_me(self):
        self.screen.blit(self.bg, self.rect)
        self.screen.blit(self.textSurfaceObj, self.textRectObj)
    def update(self):
        if self.rect.x + 100 < self.screen.get_rect().width // 2:
            self.rect.x += 8
            self.textRectObj.x += 8
        elif self.rect.x + 100 == self.screen.get_rect().width / 2 and self.time < 100:
            pass
        elif self.rect.x - 200 <= self.screen.get_rect().width:
            self.rect.x += 8
            self.textRectObj.x += 8
        else:
            self.out = True


def fly(a):
    while not(a.out):
        draw(level)
        a.update()
        a.blit_me()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                a.time = 100


class toolbar:
    def __init__(self, screen):
        self.screen = screen
        self.m_rect = pygame.Rect((self.screen.get_rect().width - 300) / 2, 0, 300, 100)
        self.but1 = pygame.transform.scale(pygame.image.load("C:/arcade/toolbar/menu.png"), (80, 80))
        self.but2 = pygame.transform.scale(pygame.image.load("C:/arcade/toolbar/again.png"), (80, 80))
        self.but3 = pygame.transform.scale(pygame.image.load("C:/arcade/toolbar/exit.png"), (80, 80))
        self.but11 = pygame.transform.chop(self.but1, (0, 75, 0, 5))
        self.but21 = pygame.transform.chop(self.but2, (0, 75, 0, 5))
        self.but31 = pygame.transform.chop(self.but3, (0, 75, 0, 5))
        self.but1Rect = self.but1.get_rect()
        self.but2Rect = self.but2.get_rect()
        self.but3Rect = self.but3.get_rect()
        self.but1Rect.x = self.m_rect.x + 10
        self.but1Rect.y = 10
        self.but2Rect.x = self.m_rect.x + 100
        self.but2Rect.y = 10
        self.but3Rect.x = self.m_rect.x + 190
        self.but3Rect.y = 10
        self.im1 = self.but1; self.im2 = self.but2; self.im3 = self.but3
    def blit_me(self):
        pygame.draw.rect(self.screen, brown, self.m_rect)
        self.screen.blit(self.im1, self.but1Rect)
        self.screen.blit(self.im2, self.but2Rect)
        self.screen.blit(self.im3, self.but3Rect)
    def update(self):
        if self.but1Rect.collidepoint(pygame.mouse.get_pos()):
            self.im1 = self.but11
            self.but1Rect = self.im1.get_rect()
            self.but1Rect.x = self.m_rect.x + 20
            self.but1Rect.y = 15
        else:
            self.im1 = self.but1
            self.but1Rect = self.im1.get_rect()
            self.but1Rect.x = self.m_rect.x + 20
            self.but1Rect.y = 10

        if self.but2Rect.collidepoint(pygame.mouse.get_pos()):
            self.im2 = self.but21
            self.but2Rect = self.im2.get_rect()
            self.but2Rect.x = self.m_rect.x + 110
            self.but2Rect.y = 15
        else:
            self.im2 = self.but2
            self.but2Rect = self.im2.get_rect()
            self.but2Rect.x = self.m_rect.x + 110
            self.but2Rect.y = 10

        if self.but3Rect.collidepoint(pygame.mouse.get_pos()):
            self.im3 = self.but31
            self.but3Rect = self.im3.get_rect()
            self.but3Rect.x = self.m_rect.x + 200
            self.but3Rect.y = 15
        else:
            self.im3 = self.but3
            self.but3Rect = self.im3.get_rect()
            self.but3Rect.x = self.m_rect.x + 200
            self.but3Rect.y = 10
        if (self.screen.get_rect().width > pygame.mouse.get_pos()[0] + 10 and self.screen.get_rect().height > pygame.mouse.get_pos()[1] + 10 and pygame.mouse.get_pos()[0] > 10 and pygame.mouse.get_pos()[1] > 10):
            #print(pygame.mouse.get_pos(), self.screen.get_rect().width)
            self.blit_me()

def clean():
    global f_cnt, re, level, Move, tut, ag, tmp_color, num, Anim, tmp, Card, Door, Bucket
    pygame.mixer.music.pause()
    tmp_color = ''
    ag = 0
    re = 1
    f_cnt = 0
    Anim = []
    tmp = [0, 0]
    num = 1
    Card = []
    Bucket = []
    Door = []
    Move = []

def run_game():
    global ag, re, tut, fl, tmp_color, f_cnt
    pygame.init()
    if (level == len(preDoor)):
        sys.exit()
    screen = pygame.display.set_mode((len(Block[level][0]) * 40, len(Block[level]) * 40))
    pygame.display.set_caption("Our project")
    build(level, screen)
    boy = hero(screen, H[level][0], H[level][1])
    tool = toolbar(screen)
    draw(level)
    pl = 0
    boy.update(level)
    boy.blit_me()
    #print(level, tut)
    if (level == 0 and tut):
        #print("OK")
        run_tutorial(screen)
    while True:
        screen = pygame.display.set_mode((len(Block[level][0]) * 40, len(Block[level]) * 40))
        n = 0
        for i in Card:
            if i.type == 2 and i.tmp == 1:
                n = 1
        for i in Move:
            if i.tmp == 1:
                n = 1
        if n == 0 and pl != 1:
            pl = 1
            pygame.mixer.music.pause()
            pygame.mixer.music.load('C:/arcade/eggs/break.mp3')
            pygame.mixer.music.play()
        if fl != 1:
            break
        if win(boy):
            Door[0].update()
            Door[0].blit_me()
            boy.blit_me()
            pygame.time.wait(80)
            fl = 2
            clean()
            pygame.mixer.music.pause()
            break
        if level == 1:
            screen.fill(white)
        else:
            screen.fill(black)
        for i in Anim:
            i.update()
        draw(level)
        if ag == 1:
            clean()
            pygame.mixer.music.pause()
            break
        boy.update(level)
        boy.blit_me()
        tool.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    tmp[0] = 1; tmp[1] = 0
                elif event.key == pygame.K_LEFT:
                    tmp[0] = -1 * (boy.rect.x > 10); tmp[1] = 0
                elif event.key == pygame.K_UP:
                    tmp[0] = 0; tmp[1] = -1 * (boy.rect.y > 10)
                elif event.key == pygame.K_DOWN:
                    tmp[0] = 0; tmp[1] = 1 * (boy.rect.y < 600)
                elif event.key == pygame.K_a:
                    for i in Card:
                        if i.type == 0:
                            i.image = pygame.transform.scale(pygame.image.load("C:/arcade/eggs/an.png"), (40, 40))
                    Door[0].image = pygame.transform.scale(pygame.image.load("C:/arcade/door/an.png"), (40, 40))
                    pygame.mixer.music.load("C:/arcade/eggs/ram.mp3")
                    pygame.mixer.music.play()
                elif event.key == pygame.K_f:
                    f_cnt += 1
                    if (f_cnt - 1 == len(Bucket)):
                        run_egg()
                    for i in Bucket:
                        if i.rect.x == boy.rect.x and i.rect.y == boy.rect.y and i.color != brown:
                            tmp_color = i.color
                            unfill(i)
                elif event.key == pygame.K_q:
                    if tmp_color:
                        for i in Card:
                            add = conv(boy.way)
                            if i.type == 2 and boy.rect.x + add[0] == i.rect.x and boy.rect.y + add[1] == i.rect.y and tmp_color == i.color:
                                i.colored = True
                                i.surf = update1(i.surf)
                        for i in Move:
                            add = conv(boy.way)
                            if boy.rect.x + add[0] == i.rect.x and boy.rect.y + add[
                                1] == i.rect.y and tmp_color == i.color:
                                i.colored = True
                                i.surf = update1(i.surf)
                elif event.key == pygame.K_e:
                    re = 1 - re
                elif event.key == pygame.K_s:
                    near = []
                    fl1 = 0
                    add = conv(boy.way)
                    mn = Card[0]
                    for i in Card:
                        if boy.rect.x + add[0] == i.rect.x and boy.rect.y + add[1] == i.rect.y and i.type == 2:
                            mn = i
                        if (level == 1 and boy.rect.x + add[0] == i.rect.x and boy.rect.y + add[1] == i.rect.y and i.rect.x == 240 and i.rect.y == 240):
                            i.image = pygame.transform.scale(pygame.image.load("C:/arcade/eggs/ric.png"), (40, 60))
                            i.rect = i.image.get_rect()
                            i.rect.x = 240
                            i.rect.y = 210
                        if (level == 3 and boy.rect.x + add[0] == i.rect.x and boy.rect.y + add[1] == i.rect.y and i.rect.x == 40 and i.rect.y == 40):
                            i.image = pygame.transform.scale(pygame.image.load("C:/arcade/eggs/pilot.png"), (80, 80))
                            i.rect = i.image.get_rect()
                            i.rect.x = 0
                            i.rect.y = 0
                        if (level == 1 and boy.rect.x + add[0] == i.rect.x and boy.rect.y + add[1] == i.rect.y +  40 and i.rect.x == 240 and i.rect.y == 200):
                            i.tmp = 0
                    for i in Move:
                        if boy.rect.x + add[0] == i.rect.x and boy.rect.y + add[1] == i.rect.y:
                            mn = i
                    if boy.rect.x + add[0] != mn.rect.x and boy.rect.y + add[1] == mn.rect.y:
                        fl1 = 1
                    for i in Card:
                        if abs(mn.rect.x - i.rect.x) == 40 and mn.rect.y == i.rect.y and i.type == 2:
                            near.append(i)
                        if abs(mn.rect.y - i.rect.y) == 40 and mn.rect.x == i.rect.x and i.type == 2:
                            near.append(i)
                    for i in Move:
                        if abs(mn.rect.x - i.rect.x) == 40 and mn.rect.y == i.rect.y:
                            near.append(i)
                        if abs(mn.rect.y - i.rect.y) == 40 and mn.rect.x == i.rect.x:
                            near.append(i)
                    if (mn.type != 0 and mn.type != 1):
                        for i in near:
                            if i.type != 0 and not(i.colored) and i.color == mn.color:
                                fl1 = 1
                    else:
                        fl1 = 1
                    if (mn.tmp == 0):
                        fl1 = 1
                    if not(mn.colored):
                        fl1 = 1
                    if (fl1 == 0):
                        if (mn.type == 2):
                            Card.append(floor_block(screen, mn.rect.x, mn.rect.y))
                        Anim.append(ani(screen, mn.rect.x, mn.rect.y))
                        mn.tmp = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tool.but1Rect.collidepoint(pygame.mouse.get_pos()):
                    fl = 0
                elif tool.but2Rect.collidepoint(pygame.mouse.get_pos()):
                    ag = 1
                elif tool.but3Rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()

        pygame.display.flip()

def run_egg():
    pygame.init()
    pic = pygame.image.load("C:/arcade/eggs/F.png")
    pic = pygame.transform.scale(pic, (500, 400))
    screen = pygame.display.set_mode((pic.get_rect().width, pic.get_rect().height))
    pygame.display.set_caption("Our project")
    fl = 0
    while True:
        if fl == 1:
            break
        screen.blit(pic, pic.get_rect())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    fl = 1
        pygame.display.flip()


class button:
    def __init__(self, screen, x, y, text):
        self.screen = screen
        pic = pygame.image.load("C:/arcade/button.png")
        pic = pygame.transform.scale(pic, (300, 100))
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x; self.rect.y = y
        fontObj = pygame.font.Font('freesansbold.ttf', 30)
        self.textSurfaceObj = fontObj.render(text, True, black)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.x = x + (300 - self.textRectObj.width) / 2
        self.textRectObj.top = y + 30
    def update(self):
        pic = pygame.image.load("C:/arcade/button.png")
        pic = pygame.transform.scale(pic, (300, 100))
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pic = pygame.transform.rotate(pic, 180)
            self.image = pic
        else:
            self.image = pic
    def blit_me(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.textSurfaceObj, self.textRectObj)

class Text:
    def __init__(self, screen, x, y, color, text, size, style):
        self.screen = screen
        fontObj = pygame.font.Font(style, size)
        self.textSurfaceObj = fontObj.render(text, True, color)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.x = x
        self.textRectObj.y = y
    def blit_me(self):
        self.screen.blit(self.textSurfaceObj, self.textRectObj)


def run_tmp(screen):
    fl  = 0
    txt = Text(screen, 0, 0, white, "This game was programmed by young hackers and the best programmers in the", 20, 'freesansbold.ttf')
    txt1 = Text(screen, 0, 30, white, "world. Actually, one of them still haven't written Acho-Korasic algorithm)", 20, 'freesansbold.ttf')
    txt2 = Text(screen, 0, 60, white, "The second will say smt about himself later.", 20, 'freesansbold.ttf')
    butt1 = button(screen, 100, 100, "back")
    while True:
        if fl == 1:
            break
        screen.fill(black)
        txt.blit_me()
        txt1.blit_me()
        txt2.blit_me()
        butt1.update()
        butt1.blit_me()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if butt1.rect.collidepoint(i.pos):
                    fl = 1
        pygame.display.flip()


def draw_prefie(a, b, c):
    a.update()
    b.update()
    c.update()
    a.blit_me()
    b.blit_me()
    c.blit_me()

fl = 0

def run_prefie():
    global fl, tut, level
    s = ""
    bg = pygame.image.load("C:/arcade/prefie.png")
    bg = pygame.transform.scale(bg, (800, 500))
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    Name = Text(screen, 100, 100, aqua, "color labyrinth", 80, "C:/arcade/schrifts/3.otf")
    button1 = button(screen, 500, 200, "Tutorial")
    button2 = button(screen, 500, 300, "Play")
    button3 = button(screen, 500, 400, "About Authors")
    pygame.display.set_caption("Our project")
    while True:
        if (s == "auth"):
            run_pic()
            s += "o"
            screen =  pygame.display.set_mode((800, 500))
        screen.blit(bg, [0, 0])
        Name.blit_me()
        if fl == 1:
            clean()
            break
        draw_prefie(button1, button2, button3)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    s += "a"
                if event.key == pygame.K_u:
                    s += "u"
                if event.key == pygame.K_t:
                    s += "t"
                if event.key == pygame.K_h:
                    s += "h"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.rect.collidepoint(event.pos):
                    fl = 1
                    tut = 1
                    level = 0
                    break
                if button2.rect.collidepoint(event.pos):
                    fl = 1
                    level = max(1, level)
                    clean()
                    break
                if button3.rect.collidepoint(event.pos):
                    run_tmp(screen)
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

def run_pic():
    pygame.init()
    fl = 0
    pic = pygame.image.load("C:/arcade/eggs/authors.png")
    pic = pygame.transform.scale(pic, (480, 600))
    screen = pygame.display.set_mode((pic.get_rect().width, pic.get_rect().height))
    pygame.display.set_caption("Our project")
    while True:
        screen.blit(pic, pic.get_rect())
        if fl == 1:
            break
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.KEYDOWN:
                fl = 1
        pygame.display.flip()


def run_win():
    s = ""
    global level, fl
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Our project")
    but = button(screen, 250, 300, "Next")
    txt = Text(screen, 250, 100, green, "You win!", 100, "C:/arcade/schrifts/1.otf")
    while True:
        if s == "play":
            pygame.mixer.music.load('C:/arcade/eggs/song.mp3')
            pygame.mixer.music.play()
            s = "a"
        screen.fill(black)
        txt.blit_me()
        but.update()
        but.blit_me()
        if (fl != 2):
            pygame.mixer.music.pause()
            break
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if but.rect.collidepoint(event.pos):
                    fl = 1; level += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    s += "p"
                if event.key == pygame.K_l:
                    s += "l"
                if event.key == pygame.K_a:
                    s += "a"
                if event.key == pygame.K_y:
                    s += "y"
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

def run_tutorial(screen):
    global tut
    flw1 = flying_window(screen, "Hello")
    flw2 = flying_window(screen, "You have to escape the labyrinth")
    flw3 = flying_window(screen, "Rules:")
    flw4 = flying_window(screen, "1) You can paint blocks only")
    flw5 = flying_window(screen, "if you have already painted")
    flw6 = flying_window(screen, "its neighbours!")
    flw7 = flying_window(screen, "2) You can't brake and paint")
    flw8 = flying_window(screen, "steel blocks")
    flw9 = flying_window(screen, "3) You can push blocks which")
    flw10 = flying_window(screen, "look like wooden boxes")
    flw11 = flying_window(screen, "Controls:")
    flw12 = flying_window(screen, "Move your character using arrows")
    flw13 = flying_window(screen, "press 'F' to take paint")
    flw14 = flying_window(screen, "press 'Q' to paint block")
    flw15 = flying_window(screen, "press 'S' to break wall")
    flw16 = flying_window(screen, "Good luck!")
    fly(flw1)
    fly(flw2)
    fly(flw3)
    fly(flw4)
    fly(flw5)
    fly(flw6)
    fly(flw7)
    fly(flw8)
    fly(flw9)
    fly(flw10)
    fly(flw11)
    fly(flw12)
    fly(flw13)
    fly(flw14)
    fly(flw15)
    fly(flw16)
    tut = 0

while fl != -1:
    if fl == 0:
        run_prefie()
    elif fl == 1:
        run_game()
    elif fl == 2:
        run_win()

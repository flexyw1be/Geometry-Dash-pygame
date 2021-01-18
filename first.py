import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


def settings():
    im = load_image('settings_screen.png')
    backgournd = load_image('background.png')
    exit_button1 = Button('icon_button', 420, 120, 120, 120, pygame.transform.scale(load_image('exit.png'), (100, 100)))
    volume_none = Button('volume_none', 500, 300, 58, 58, pygame.transform.scale(load_image('volume_none.png'),
                                                                                 (100, 100)))
    volume100 = Button('volume100', 650, 300, 58, 58, pygame.transform.scale(load_image('volume100.png'),
                                                                             (120, 100)))
    volume50 = Button('volume50', 800, 300, 58, 58, pygame.transform.scale(load_image('volume50.png'),
                                                                           (100, 100)))
    screen.blit(backgournd, (0, 0))
    screen.blit(im, (400, 100))
    while True:
        global stop
        exit_button1.draw()
        volume_none.draw()
        volume100.draw()
        volume50.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if exit_button1.isMotion():
                    stop = True
                    start_screen()
                    return
                if volume_none.isMotion():
                    volume_none.isPressed()
                if volume100.isMotion():
                    volume100.isPressed()
                if volume50.isMotion():
                    volume50.isPressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if cube:
                        stop = True
                    start_screen()
                    return
        pygame.display.flip()
        clock.tick(180)


def start_screen():
    global running
    exit_button = Button('icon_button', 10, 10, 120, 120, pygame.transform.scale(load_image('exit.png'), (100, 100)))
    screen.blit(load_image('start1.png'), (0, 0))
    icon_button = Button('icon_button', 481, 400, 213, 213, load_image('icon_button.png'))
    main_button = Button('main_button', 785, 332, 320, 320, load_image('main_button.png'))
    settings_button = Button('settings_button', 1200, 400, 200, 200, load_image('settings.png'))
    pygame.mixer.music.load('data/menu_sound.mp3')
    pygame.mixer.music.play()

    while True:
        settings_button.draw()
        icon_button.draw()
        main_button.draw()
        exit_button.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if icon_button.isMotion():
                    icon_screen()
                    return
                if main_button.isMotion():
                    main_button.isPressed()
                    level_screen()
                    return
                if settings_button.isMotion():
                    settings_button.isPressed()
                    settings()
                    return
                if exit_button.isMotion():
                    running = False
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return
        icon_button.changeIm()
        main_button.changeIm()
        settings_button.changeIm()
        pygame.display.flip()
        clock.tick(180)


def end_screen():
    global stop, first_do, second_do
    if name == 'level1.txt':
        first_do = True
    elif name == 'level2.txt':
        second_do = True
    im = load_image('end_screen.png')
    y = -1080
    exit_button2 = Button('icon_button', 420, 120, 120, 120, pygame.transform.scale(load_image('exit.png'), (100, 100)))
    while True:
        draw_background(name)
        screen.blit(im, (400, y))
        if y != 100:
            y += 20
        else:
            exit_button2.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if exit_button2.isMotion():
                exit_button2.isPressed()
                start_screen()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stop = True
                    start_screen()
                    return
        pygame.display.flip()
        clock.tick(180)


def level_screen():
    global im, rect, name
    im = load_image('level_screen.png')
    exit_button = Button('icon_button', 10, 10, 120, 120, pygame.transform.scale(load_image('exit.png'), (100, 100)))
    first_level_button = Button('first_level_button', 140, 150, 1550, 290,
                                load_image('first_level.png'))

    second_level_button = Button('second_level_button', 140, 550, 1550, 290, load_image('second_level.png'))
    check = load_image('check.png')

    while True:
        screen.blit(im, (0, 0))
        exit_button.draw()
        first_level_button.draw()
        second_level_button.draw()
        if first_do:
            screen.blit(check, (1600, 150))
        if second_do:
            screen.blit(check, (1600, 550))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.isMotion():
                    start_screen()
                    return
                if first_level_button.isMotion():
                    name = 'level1.txt'
                    generate_level(name)
                    play_sound.play()
                    return
                if second_level_button.isMotion():
                    name = 'level2.txt'
                    generate_level(name)
                    play_sound.play()
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_sound.play()
                    start_screen()
                    return
        first_level_button.changeIm()
        second_level_button.changeIm()
        pygame.display.flip()
        clock.tick(180)


def icon_screen():
    screen.blit(pygame.transform.scale(cube.image, (310, 310)), (820, 160))
    player_icon1 = Icon('player_icon1', 377, 510, pygame.transform.scale(load_image('player_icon1.png'), (124, 124)))
    player_icon2 = Icon('player_icon2', 530, 510, pygame.transform.scale(load_image('player_icon2.png'), (124, 124)))
    player_icon3 = Icon('player_icon3', 685, 510, pygame.transform.scale(load_image('player_icon3.png'), (124, 124)))
    while True:
        screen.blit(load_image('icon_center.png'), (0, 0))
        screen.blit(pygame.transform.scale(cube.image, (155, 155)), (820, 160))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_screen()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_icon1.isMotion():
                    player_icon1.isPressed()
                if player_icon2.isMotion():
                    player_icon2.isPressed()
                if player_icon3.isMotion():
                    player_icon3.isPressed()
                x, y = event.pos
                if 0 <= x <= 150 and 0 <= y <= 150:
                    start_screen()
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_sound.play()
                    start_screen()
                    return
        player_icon1.draw()
        player_icon2.draw()
        player_icon3.draw()
        pygame.display.flip()
        clock.tick(180)


def generate_level(name):
    global len_level
    level = load_level(name)
    len_level = len(level[1]) * 100
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == '#':
                Map(map_sprite, (j + 1) * 100, (i + 1) * 100 - 20,
                    pygame.transform.scale(load_image('Block1.png'), (100, 100)))
            if level[i][j] == '+':
                Map(map_sprite, (j + 1) * 100, (i + 1) * 100 - 20,
                    pygame.transform.scale(load_image('Block2.png'), (100, 100)))
            elif level[i][j] == '!':
                Spike(spike_sprite, (j + 1) * 100, (i + 1) * 100 - 20)
            elif level[i][j] == '/':
                Portal(portal_sprite, (j + 1) * 100, i * 100 - 20, 1)
            elif level[i][j] == '|':
                Portal(portal_sprite, (j + 1) * 100, i * 100 - 20, 0)


class Cube(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.transform.scale(load_image('player_icon1.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 980
        self.onGround = False
        self.vy = 0
        self.mask = pygame.mask.from_surface(self.image)

    def jump(self):
        global countJump, make_jump, min_y
        if countJump > -41:
            self.rect = self.rect.move(0, -countJump / 3)
            countJump -= 1
        else:
            self.image = pygame.transform.rotate(self.image, 180)
            countJump = 40
            make_jump = False

    def update(self):
        global min_y, im
        im = self.image
        self.rect = self.rect.move(0, self.vy)
        if self.rect.y > min_y:
            self.rect.y = min_y


class Check_cube(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.rect = pygame.Rect(300, 980, 100, 100)
        self.rect.x = 300
        self.rect.y = 980
        self.image = pygame.transform.scale(load_image('player_icon2.png'), (100, 100))

    def update(self):
        if cube.rect.y in [x * 100 + 80 for x in range(0, 9)]:
            self.rect.y = cube.rect.y + 100
        if cube.onGround and not pygame.sprite.spritecollideany(self, map_sprite) and cube.rect.y % 100 == 80:
            cube.onGround = False
            cube.vy = 5
        if cube.onGround or cube.rect.y == 980:
            cube.vy = 0


class Wave(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image('wave_icon.png')
        self.bad_image = pygame.transform.scale(load_image('wave_icon.png'), (80, 80))
        self.true_image = pygame.transform.scale(load_image('wave_icon_true.png'), (80, 80))
        self.straight_image = pygame.transform.scale(load_image('wave_icon_straight.png'), (80, 80))
        self.image = self.bad_image
        self.rect = self.image.get_rect()
        self.rect.x = cube.rect.x
        self.rect.y = cube.rect.y
        self.mask = pygame.mask.from_surface(self.image)
        self.v = 5

    def update(self):
        global stop
        self.rect = self.rect.move(0, self.v)
        if self.v < 0:
            self.image = self.true_image
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.image = self.bad_image
            self.mask = pygame.mask.from_surface(self.image)
        if self.rect.y < 0:
            self.v = 0
            self.image = self.straight_image
        if self.rect.y > 1000:
            self.v = 0
            self.image = self.straight_image


class Spike(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = pygame.transform.scale(load_image('Spike2.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        global running, stop, im
        self.rect = self.rect.move(-5, 0)
        if pygame.sprite.collide_mask(self, cube):
            death_sound.play()
            im = cube.image
            stop = True
        if isWave and wave != 0:
            if pygame.sprite.spritecollideany(self, wave_sprite):
                death_sound.play()
                stop = True


class Map(pygame.sprite.Sprite):
    def __init__(self, group, x, y, image):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        global stop, im
        self.rect = self.rect.move(-5, 0)
        if pygame.sprite.collide_mask(self, cube):
            if cube.rect.y <= self.rect.y - 10:
                cube.rect.y = self.rect.y - 100
                cube.onGround = True
            else:
                death_sound.play()
                im = cube.image
                stop = True
        if isWave and wave != 0:
            if pygame.sprite.spritecollideany(self, wave_sprite):
                death_sound.play()
                stop = True


class Button():
    def __init__(self, name, x, y, sizex, sizey, image):
        self.name = name
        self.rect = pygame.Rect(x, y, sizex, sizey)
        self.x, self.y, self.sizex, self.sizey = x, y, sizex, sizey
        self.image = image

    def changeIm(self):
        if self.isMotion():
            if self.name == 'icon_button':
                self.image = load_image('icon_button_true.png')
            elif self.name == 'main_button':
                self.image = load_image('main_button_true.png')
            elif self.name == 'first_level_button':
                self.image = load_image('first_level_true.png')
            elif self.name == 'second_level_button':
                self.image = load_image('second_level_true.png')
            elif self.name == 'settings_button':
                self.image = load_image('settings_true.png')
        else:
            if self.name == 'icon_button':
                self.image = load_image('icon_button.png')
            elif self.name == 'main_button':
                self.image = load_image('main_button.png')
            elif self.name == 'first_level_button':
                self.image = load_image('first_level.png')
            elif self.name == 'second_level_button':
                self.image = load_image('second_level.png')
            elif self.name == 'settings_button':
                self.image = load_image('settings.png')

    def isMotion(self):
        x, y = pygame.mouse.get_pos()
        return self.x <= x <= self.x + self.sizex and self.y <= y <= self.y + self.sizey

    def isPressed(self):
        global stop
        if self.isMotion():
            if self.name == 'volume_none':
                pygame.mixer.music.set_volume(0.0)
            if self.name == 'volume100':
                pygame.mixer.music.set_volume(1)
            if self.name == 'volume50':
                pygame.mixer.music.set_volume(0.5)
            if self.name == 'exit_button2':
                stop = True

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Icon():
    def __init__(self, name, x, y, image):
        self.name = name
        self.rect = pygame.Rect(x, y, 125, 125)
        self.x, self.y, self.size = x, y, size
        self.image = image

    def isMotion(self):
        x, y = pygame.mouse.get_pos()
        return self.x <= x <= self.x + 124 and self.y <= y <= self.y + 124

    def isPressed(self):
        if self.isMotion():
            cube.image = pygame.transform.scale(self.image, (100, 100))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Portal(pygame.sprite.Sprite):
    def __init__(self, group, x, y, id):
        super().__init__(group)
        self.image = pygame.transform.scale(load_image('portal.png'), (100, 200))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.id = id
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        global isWave, wave, make_jump
        self.rect = self.rect.move(-5, 0)
        if self.rect.x + 100 == cube.rect.x and self.rect.y < cube.rect.y < self.rect.y + 200 and self.id == 1:
            wave = Wave(wave_sprite)
            isWave = True
        if wave != 0:
            if self.rect.x == wave.rect.x + 100 and self.rect.y - 100 < wave.rect.y < self.rect.y + 200 and self.id == 0:
                cube.rect.y = wave.rect.y - 50
                cube1.rect.y = wave.rect.y - 150
                cube.vy = 5
                make_jump = False

                wave = 0
                isWave = False


def draw_background(name):
    if name == 'level1.txt':
        pygame.draw.rect(screen, 'pink', (0, 0, 1920, 1080))
        pygame.draw.rect(screen, '#FF69B4', (0, 0, 1920, 80))
        pygame.draw.rect(screen, 'black', (0, 0, 1920, 80), 5)
    if name == 'level2.txt':
        pygame.draw.rect(screen, '#3CB371', (0, 0, 1920, 1080))
        pygame.draw.rect(screen, '#008000', (0, 0, 1920, 80))
        pygame.draw.rect(screen, 'black', (0, 0, 1920, 80), 5)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Yandex dash')
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    pygame.display.set_icon(load_image('icon.bmp'))
    cube_sprite, map_sprite, spike_sprite = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    wave_sprite, portal_sprite, check_cube = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    cube, stop = Cube(cube_sprite), False
    im, countJump, wave, isWave, make_jump, min_y, name, len_level, x = 0, 40, 0, False, False, 980, '', '', 0
    cube1, clock = Check_cube(check_cube), pygame.time.Clock()
    pygame.mixer.music.load('data/menu_sound.mp3')
    first_do, second_do = False, False
    running = True
    pygame.mixer.music.play()
    quit_sound, death_sound = pygame.mixer.Sound('Data/quit.ogg'), pygame.mixer.Sound('data/Death.mp3')
    pygame.mixer.music.set_volume(1)
    play_sound = pygame.mixer.Sound('Data/play.ogg')
    start_screen()
    if running:
        pygame.mixer.music.load(f'Data/{name[:6]}.mp3')
        pygame.mixer.music.play()
    while running:
        if stop:
            pygame.mixer.music.load(f'Data/{name[:6]}.mp3')
            map_sprite, spike_sprite, cube_sprite = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
            wave_sprite, portal_sprite = pygame.sprite.Group(), pygame.sprite.Group()
            cube = Cube(cube_sprite)
            cube.image, stop, isWave, countJump, make_jump, wave, x = im, False, False, 40, False, 0, 0
            generate_level(name)
            pygame.mixer.music.play()
        draw_background(name)
        if -x == len_level:
            end_screen()
        else:
            x -= 5
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if cube.vy == 0:
                        make_jump = True
                    if isWave:
                        if wave.v == 5:
                            wave.v = -5
                        else:
                            wave.v = 5
                        if wave.rect.y > 1000:
                            wave.v = -5
                        if wave.rect.y == 0:
                            wave.v = 5
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        settings()

            if isWave:
                cube.rect.y = 1090
                wave_sprite.draw(screen)
                wave_sprite.update()
            else:
                cube_sprite.draw(screen)
                if make_jump:
                    cube.jump()
        map_sprite.draw(screen)
        spike_sprite.draw(screen)
        portal_sprite.draw(screen)
        map_sprite.update()
        spike_sprite.update()
        cube_sprite.update()
        portal_sprite.update()
        pygame.display.flip()
        check_cube.update()
        clock.tick(180)

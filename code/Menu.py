import pygame
from code.Const import C_BLUE, MENU_SELECTION, C_ORANGE, DISPLAY_WIDTH, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.font_title = pygame.font.Font('./asset/BROTHERBOLD.OTF', 70)
        self.font_option = pygame.font.Font('./asset/Ithaca.ttf', 60)
        self.font_main = pygame.font.Font('./asset/Ithaca.ttf', 40)
        self.font_regular = pygame.font.Font('./asset/Ithaca.ttf', 30)
        self.font_small = pygame.font.Font('./asset/Ithaca.ttf', 20)
        self.font_keys = pygame.font.Font('./asset/Ithaca.ttf', 27)
        self.player_icon = pygame.image.load('./asset/PlayerBg0.png').convert_alpha()
        self.player_icon = pygame.transform.scale(self.player_icon, (25, 20))
        self.sound_select = pygame.mixer.Sound('./asset/MenuSelection.wav')
        self.sound_select.set_volume(0.2)

    def menu_text(self, font_obj, text, color, center_pos):
        text_surf = font_obj.render(text, True, color).convert_alpha()
        text_rect = text_surf.get_rect(center=center_pos)
        self.window.blit(text_surf, text_rect)
        return text_rect

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            # Título
            self.menu_text(self.font_title, "Deep Sea", C_BLUE, ((DISPLAY_WIDTH / 2), 60))
            self.menu_text(self.font_title, "Dodge", C_BLUE, ((DISPLAY_WIDTH / 2), 120))
            self.menu_text(self.font_small, "Demo", C_BLUE, ((DISPLAY_WIDTH / 2 + 90), 100))
            # Show game controls
            self.menu_text(self.font_regular, "Controles", C_WHITE, (90, 195))
            self.menu_text(self.font_keys, "W", C_ORANGE, (90, 245))
            self.menu_text(self.font_small, "sobe", C_WHITE, (90, 225))
            self.menu_text(self.font_keys, "A", C_ORANGE, (75, 260))
            self.menu_text(self.font_small, "recua", C_WHITE, (45, 260))
            self.menu_text(self.font_keys, "D", C_ORANGE, (105, 260))
            self.menu_text(self.font_small, "avança", C_WHITE, (140, 260))
            self.menu_text(self.font_keys, "S", C_ORANGE, (90, 275))
            self.menu_text(self.font_small, "desce", C_WHITE, (90, 295))
            # Menu Selection
            self.menu_text(self.font_regular, "Aperte ENTER", C_WHITE, (470, 220))
            self.menu_text(self.font_regular, "para selecionar", C_WHITE, (470, 245))
            for i in range(len(MENU_SELECTION)):
                if i == menu_option:  # Highlight the current selection
                    text_rect = self.menu_text(self.font_option, MENU_SELECTION[i], C_ORANGE,
                                               ((DISPLAY_WIDTH / 2), 200 + 40 * i))
                    # Show fish sprite with the current selection
                    icon_rect = self.player_icon.get_rect()
                    icon_rect.right = text_rect.left - 10
                    icon_rect.centery = text_rect.centery - 5
                    self.window.blit(self.player_icon, icon_rect)
                else:
                    self.menu_text(self.font_main, MENU_SELECTION[i], C_WHITE, ((DISPLAY_WIDTH / 2), 200 + 40 * i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    # Navigate through menu options with W and S keys
                    if event.key == pygame.K_s:
                        if menu_option < len(MENU_SELECTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_w:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_SELECTION) - 1
                    if event.key == pygame.K_RETURN:
                        # Play a selection effect
                        self.sound_select.play()
                        return MENU_SELECTION[menu_option]
            pygame.display.flip()

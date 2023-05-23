import pygame
import win32api
import win32con
import win32gui


class CrosshairOverlay:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Crosshair')
        icon = pygame.image.load('img\crosshairIcon.png')
        pygame.display.set_icon(icon)

        self.width = 200
        self.height = 200
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.is_visible = True

        self.crosshair_color = ('#00FFF4')
        self.crosshair_thickness = 2
        self.crosshair_size = 2
        self.crosshair_pos = (self.width // 2, self.height // 2)


    def draw_crosshair(self):
        pos = self.crosshair_pos
        size = self.crosshair_size
        thickness = self.crosshair_thickness
        color = self.crosshair_color
        pygame.draw.line(self.screen, color, (pos[0] - 5 - size, pos[1]), (pos[0] - 5 + size, pos[1]), thickness)
        pygame.draw.line(self.screen, color, (pos[0] + 5 - size, pos[1]), (pos[0] + 5 + size, pos[1]), thickness)
        pygame.draw.line(self.screen, color, (pos[0], pos[1] + 5 - size), (pos[0], pos[1] + 5 + size), thickness)
        pygame.draw.line(self.screen, color, (pos[0], pos[1] - 5 - size), (pos[0], pos[1] - 5 + size), thickness)

        # pygame.draw.line(self.screen, color, (pos[0], pos[1] - size), (pos[0], pos[1] + size), thickness)


    def transparent(self, color):
        hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*color), 0, win32con.LWA_COLORKEY)


    def toggle_visibility(self):
        self.is_visible = not self.is_visible
        if self.is_visible:
            self.screen = pygame.display.set_mode((self.width, self.height))

        else:
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)
            
            
    def alwaysOnTop(self):
        hwnd = win32gui.GetForegroundWindow()
        screen_width, screen_height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
        x_pos, y_pos = (screen_width - self.width) // 2, (screen_height - self.height) // 2
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x_pos, y_pos, 0, 0, win32con.SWP_NOSIZE)


    def run(self):
        running = True
        fuchsia = (255, 0, 128)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        running = False
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.toggle_visibility()
                        self.alwaysOnTop()
                
                self.transparent(fuchsia)
                self.screen.fill(fuchsia)
                self.draw_crosshair()
                pygame.display.update()


if __name__ == '__main__':
    overlay = CrosshairOverlay()
    overlay.run()

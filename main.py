import pygame,sys,random,math
from configs import *
from Point import Point

class Simulation():
    def __init__(self):
        # Game's data
        self.Points = []

        pygame.init()
        self.get_data()
        pygame.display.set_caption("Project 101")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def get_data(self):
        def create_points(number, color):
            for i in range(number):
                self.Points.append(
                    Point(color, random.randint(1, SCREEN_WIDTH - 2), random.randint(1, SCREEN_HEIGHT - 2)))

        create_points(1,(255,0,0))
        create_points(1,(0,255,0))
        # create_points(50,(0,0,255))

        Dictionary_Color[str([(255,0,0), (0,255,0)])] = 35
        Dictionary_Color[str([(0,255,0), (255,0,0)])] = 35
        # Dictionary_Color[str([(255, 0, 0), (0,0,255)])] = 7.8
        # Dictionary_Color[str([(0,0,255), (255, 0, 0)])] = 7.8
        # Dictionary_Color[str([(0,0,255), (0, 255, 0)])] = -1
        # Dictionary_Color[str([(0, 255, 0), (0,0,255)])] = -1
        # Dictionary_Color[str([(0,0,255), (0,0,255)])] = 40
        Dictionary_Color[str([(0,255,0), (0,255,0)])] = 6.7
        Dictionary_Color[str([(255,0,0), (255,0,0)])] = 4


    def draw_points(self):
        for i in range(len(self.Points)):
            pygame.draw.rect(self.screen,"black", self.Points[i].image)
            for k in range(i+1,len(self.Points)):
                distance = math.sqrt((self.Points[k].x - self.Points[i].x) ** 2 + (self.Points[k].y - self.Points[i].y) ** 2)
                self.Points[i].data.append(
                    [distance,
                     self.Points[k].x - self.Points[i].x,
                     self.Points[k].y - self.Points[i].y,
                     Dictionary_Color[str([self.Points[i].color,self.Points[k].color])]])
                self.Points[k].data.append(
                    [distance,
                     self.Points[i].x - self.Points[k].x,
                     self.Points[i].y - self.Points[k].y,
                     Dictionary_Color[str([self.Points[i].color,self.Points[k].color])]])
            self.Points[i].move_point()
            pygame.draw.rect(self.screen, self.Points[i].color, self.Points[i].image)

    def run(self):
        PAUSE_TIMER = 1
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        while True:
                            for event1 in pygame.event.get():
                                if event1.type == pygame.KEYDOWN:
                                    if event1.key == pygame.K_SPACE:
                                        break
                                if event1.type != pygame.KEYDOWN:
                                    self.clock.tick(60)
            self.draw_points()
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    sim = Simulation()
    sim.run()
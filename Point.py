from configs import *
import pygame

class Point():
    def __init__(self,color,coord_x,coord_y):
        self.color = color
        self.x = coord_x
        self.y = coord_y
        self.velocity = [0,0]
        self.data = []
        self.move_point()

    def move_point(self):
        for d in self.data:
            if d[0] != 0:

                self.velocity[0] += ((d[1] * d[3]) / (d[0] ** 2))
                self.velocity[1] += ((d[2] * d[3]) / (d[0] ** 2))


        self.data.clear()
        if self.x >= SCREEN_WIDTH or self.x <= 0:
            self.velocity[0] *= -1
        if self.y >= SCREEN_HEIGHT or self.y <= 0:
            self.velocity[1] *= -1
        self.x += self.velocity[0] * POINT_SPEED
        self.y += self.velocity[1] * POINT_SPEED
        self.image = pygame.Rect(self.x, self.y, POINT_WIDTH, POINT_HEIGHT)




        # for d in self.data:
        #     if d[0] != 0:
        #         self.acceleration[0] += G / d[0]
        #     if d[1] != 0:
        #         self.acceleration[1] += G / d[1]
        #
        # self.data.clear()
        #
        # self.velocity[0] += self.acceleration[0]
        # self.velocity[1] += self.acceleration[1]
        # self.acceleration[0],self.acceleration[1] = 0,0
        # if self.x >= SCREEN_WIDTH or self.x <= 0:
        #     self.velocity[0] *= -1
        # if self.y >= SCREEN_HEIGHT or self.y <= 0:
        #     self.velocity[1] *= -1
        # self.x += self.velocity[0]
        # self.y += self.velocity[1]


        # for i in self.acceleration_list:
        #     self.velocity[0] += i[0] * POINT_SPEED
        #     self.velocity[1] += i[1] * POINT_SPEED
        # # make points move with velocity
        # if self.x >= SCREEN_WIDTH or self.x <= 0:
        #     self.velocity[0] *= -1
        # if self.y >= SCREEN_HEIGHT or self.y <= 0:
        #     self.velocity[1] *= -1
        # self.x += self.velocity[0]
        # self.y += self.velocity[1]




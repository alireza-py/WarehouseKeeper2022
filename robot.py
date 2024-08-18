import cv2
import csv
import sys
import math
# import pygame
import numpy as np
from time import sleep
from re import search, findall
from hsv_color import control_hsv
from find_color import find_colors
from plan import robot_distanation
from send_serial_command import command
from find_distanse import dis

class storage_keeper:
    def __init__(self):
        self.open_capture = True
        self.fund_robot = False
        self.hsv = ()
        self.x = []
        self.y = []

    def goto_target(self, frame, x, y, robot_xy):
        
        copy_frame = frame

        tup = robot_distanation.distanation(self, copy_frame, False)

        (x1, y1), fund_r1, (x2, y2), fund_r2, (x3, y3), fund_r3 = (tup[0][0], tup[0][1], tup[1][0],
                                                                   tup[1][1], tup[2][0], tup[2][1]) 
        
        self.x = [x1, x2]
        self.y = [y1, y2]


        if robot_xy:
            if fund_r1 and fund_r2:
                self.fund_robot = True
                return False, copy_frame
            else:
                self.fund_robot = False
                return False, copy_frame


        if fund_r1 and fund_r2 :#and fund_r3

            self.fund_robot = True
            if self.open_capture:
                for _ in range(3):
                    sleep(0.1)
                    command.send_command('o')
                self.open_capture = False
            
            dis_lin_1 = dis.distance(x1, y1, x, y)
            dis_lin_2 = dis.distance(x2, y2, x, y)
            dis_lin_3 = dis.distance(x3, y3, x, y)

            round_number = 0

            cv2.line(copy_frame, (x1, y1), (x, y), (0, 200, 0), 2)
            cv2.line(copy_frame, (x2, y2), (x, y), (0, 200, 0), 2)
            # cv2.line(copy_frame, (x3, y3), (x, y), (0, 200, 0), 2)

            motion_data = [round(dis_lin_1, round_number), round(dis_lin_2, round_number), round(dis_lin_3, round_number)]
            add = motion_data[0] - motion_data[1]
            dist = (dis_lin_1 + dis_lin_2) / 2

            print(motion_data[0], motion_data[1], add, dist)
            if motion_data[2] > motion_data[1] and motion_data[2] > motion_data[0]:
                if add > -5 and add < 5:
                    for _ in range(2):
                        command.send_command('g')
                        sleep(0.004)

                elif add >= 5:
                    command.send_command('r')
                    
                elif add <= -5:
                    command.send_command('l')
            else: 
                command.send_command('l')
                

            return dist, copy_frame

        else:
            command.send_command('s')
            self.fund_robot = False
            return 700, copy_frame

    def get_object(self, frame):
        
        copy_frame = frame.copy()

        fund_object = []
        dis_lins = {}

        tup = robot_distanation.distanation(self, copy_frame, True)
                                                                    
        (x4, y4), fund_o1, h1, (x5, y5), fund_o2, h2, (x6, y6), fund_o3, h3 = (tup[3][0], tup[3][1], tup[3][2], tup[4][0],
                                                                    tup[4][1], tup[4][2], tup[5][0], tup[5][1], tup[5][2])


        if self.fund_robot and (fund_o1 or fund_o2 or fund_o3):

            x1, x2 = self.x
            y1, y2 = self.y

                
            if fund_o1:
                fund_object.append((x4, y4))
                self.hsv = h1

            elif fund_o2:
                fund_object.append((x5, y5))
                self.hsv = h2

            elif fund_o3:
                fund_object.append((x6, y6))
                self.hsv = h3

            for x, y in fund_object:
                    
                dis_lins[sum([dis.distance(x1, y1, x, y) , dis.distance(x2, y2, x, y)])] = (x, y)

            m = min(dis_lins)

            (x, y) = dis_lins[m]
            dist, _ = self.goto_target(frame, x, y, False)
            print(dist)
            if dist < 30:
                for _ in range(15):
                    command.send_command('g')
                    sleep(0.01)
                for _ in range(3):
                    command.send_command('c')
                    sleep(0.3)
                for _ in range(1):
                    sleep(0.01)
                    
                # command.send_command('s')
                print('----  I got the target !!  ----')

                return True, copy_frame


            # else:
            #     self.open_capture = False
        else:
            self.goto_target(frame, 0, 0, True)

        return False, copy_frame
                    
    def goto_color_position_board(self, frame):
    
        copy_frame = frame.copy()
        
        tup = robot_distanation.distanation(self, copy_frame, True)
        
        (x4, y4), fund_o1, h1, (x5, y5), fund_o2, h2, (x6, y6), fund_o3, h3 = (tup[6][0], tup[6][1], tup[6][2], tup[7][0],
                                                                    tup[7][1], tup[7][2], tup[8][0], tup[8][1], tup[8][2])

        if fund_o1 or fund_o2 or fund_o3:
            if fund_o1 and h1 == self.hsv:
                dist, copy_frame = self.goto_target(frame, x4, y4, False)
            
            elif fund_o2 and h2 == self.hsv:
                dist, copy_frame = self.goto_target(frame, x5, y5, False)

            elif fund_o3 and h3 == self.hsv:
                dist, copy_frame = self.goto_target(frame, x6, y6, False)
            try:
                if dist < 38:

                    self.open_capture = True
                    for _ in range(20):
                        command.send_command('o')
                        sleep(0.1)

                    for _ in range(130):
                        command.send_command('b')
                        sleep(0.01)

                    for _ in range(200):
                        command.send_command('l')
                        sleep(0.01)
                    command.send_command('s')

                    print('----- finished -----')
                    return True, copy_frame
            except: 
                for _ in range(3):
                    command.send_command('o')
                    sleep(0.02)

                for _ in range(130):
                    command.send_command('b')
                    sleep(0.01)

                for _ in range(200):
                    command.send_command('l')
                    sleep(0.01)

                print('----- finished -----')
                return True, copy_frame
        else:
            return False, copy_frame
        return False, copy_frame

a = storage_keeper()
camera = cv2.VideoCapture(2)
# camera.set(cv2.CAP_PROP_FPS, 1)

while 1:
    _, frame = camera.read()

    f, _ = a.get_object(frame)

    if f:
        while 1:
            _, frame = camera.read()
            # print(frame)
            d, s  = a.goto_color_position_board(frame)
            # print(d)
            cv2.imshow('winname', frame)

            cv2.waitKey(1)

            if d:
                break

    cv2.imshow('winname', frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()





import cv2
from hsv_color import control_hsv
from find_color import find_colors

class robot_distanation:
    def __init__(self):

        self.data_robot1 = []
        self.data_robot2 = []
        self.data_robot3 = []
        self.data_color1 = []
        self.data_color2 = []
        self.data_color3 = []
        self.data_color4 = []
        self.data_color5 = []
        self.data_color6 = []
        
    def distanation(self, frame, T_F):
        xcut = 190
        ycut = 65
        cut_frame2 = frame.copy()
        cut_frame1 = frame[ycut:480-ycut, xcut:640-xcut]
        cut_frame2[ycut:480-ycut, xcut:640-xcut] = (255, 255, 255)
   
        self.robot_color_1 = control_hsv.hsv_controls(self, 1)
        self.robot_color_2 = control_hsv.hsv_controls(self, 2)
        self.robot_color_3 = control_hsv.hsv_controls(self, 3)

        self.color_1 = control_hsv.hsv_controls(self, 4)
        self.color_2 = control_hsv.hsv_controls(self, 5)
        self.color_3 = control_hsv.hsv_controls(self, 6)

        self.data_robot1 = find_colors.find(frame, 0, self.robot_color_1)
        self.data_robot2 = find_colors.find(frame, 0, self.robot_color_2)
        self.data_robot3 = find_colors.find(frame, 0, self.robot_color_3)

        self.data_color1 = find_colors.find(cut_frame1, 250, self.color_1)
        self.data_color2 = find_colors.find(cut_frame1, 200, self.color_2)
        self.data_color3 = find_colors.find(cut_frame1, 210, self.color_3)

        self.data_color4 = find_colors.find(cut_frame2, 1000, self.color_1)
        self.data_color5 = find_colors.find(cut_frame2, 1000, self.color_2)
        self.data_color6 = find_colors.find(cut_frame2, 1000, self.color_3)

        cv2.imshow('color robot 1', self.data_robot1[3])
        cv2.imshow('color robot 2', self.data_robot2[3])
        cv2.imshow('color robot 3', self.data_robot3[3])

        cv2.circle(frame, (self.data_robot1[0][0], self.data_robot1[0][1]), 10, (0, 0, 255), -1)
        cv2.circle(frame, (self.data_robot2[0][0], self.data_robot2[0][1]), 10, (0, 0, 255), -1)
        cv2.circle(frame, (self.data_robot3[0][0], self.data_robot3[0][1]), 10, (0, 0, 255), -1)

        self.data_color1[0][0] += xcut; self.data_color1[0][1] += ycut
        cv2.circle(frame, (self.data_color1[0][0], self.data_color1[0][1]), 10, (0, 0, 255), -1)

        self.data_color2[0][0] += xcut; self.data_color2[0][1] += ycut
        cv2.circle(frame, (self.data_color2[0][0], self.data_color2[0][1]), 10, (0, 0, 255), -1)

        self.data_color3[0][0] += xcut; self.data_color3[0][1] += ycut
        cv2.circle(frame, (self.data_color3[0][0], self.data_color3[0][1]), 10, (0, 0, 255), -1)
        
        cv2.circle(frame, (self.data_color4[0][0], self.data_color4[0][1]), 10, (0, 255, 255), -1)
        cv2.circle(frame, (self.data_color5[0][0], self.data_color5[0][1]), 10, (0, 255, 255), -1)
        cv2.circle(frame, (self.data_color6[0][0], self.data_color6[0][1]), 10, (0, 255, 255), -1)

        if T_F:

            cv2.imshow('object 1', self.data_color1[3])
            cv2.imshow('object 2', self.data_color2[3])
            cv2.imshow('object 3', self.data_color3[3])
            cv2.imshow('object 4', self.data_color4[3])
            cv2.imshow('object 5', self.data_color5[3])
            cv2.imshow('object 6', self.data_color6[3])

            return (self.data_robot1, self.data_robot2, self.data_robot3, self.data_color1, self.data_color2,
                                      self.data_color3, self.data_color4, self.data_color5, self.data_color6) 
        else:

            return (self.data_robot1, self.data_robot2, self.data_robot3)



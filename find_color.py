import cv2
import numpy as np

class find_colors:
    
    def find(frame, number_min_maxcontour, low_high_color_list):

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_color, upper_color = np.array([[low_high_color_list[0], low_high_color_list[1], low_high_color_list[2]],
                                             [low_high_color_list[3], low_high_color_list[4], low_high_color_list[5]]])

        mask = cv2.inRange(frame, lower_color, upper_color)
        frame = cv2.bitwise_and(frame, frame, mask = mask)
        cnts, hir = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(cnts) > 0:
            maxcontour = max(cnts, key=cv2.contourArea)
            m = cv2.moments(maxcontour)
            if m['m00'] > 0 and cv2.contourArea(maxcontour) > number_min_maxcontour:
                cx = int(m['m10']/m['m00'])
                cy = int(m['m01']/m['m00'])
                return [[cx, cy], True, low_high_color_list, mask]
            else: 
                return [[700, 700], False, low_high_color_list, mask]
        else:
            return [[700, 700], False, low_high_color_list, mask]
import cv2

cv2.namedWindow(f'hsv_color_1')
cv2.createTrackbar('low_b',f'hsv_color_1',71,255, lambda x:x)
cv2.createTrackbar('low_g',f'hsv_color_1',0,255, lambda x:x)
cv2.createTrackbar('low_r',f'hsv_color_1',84,255, lambda x:x)
cv2.createTrackbar('high_b',f'hsv_color_1',133,255, lambda x:x)
cv2.createTrackbar('high_g',f'hsv_color_1',79,255, lambda x:x)
cv2.createTrackbar('high_r',f'hsv_color_1',161,255, lambda x:x)

cv2.namedWindow(f'hsv_color_2')
cv2.createTrackbar('low_b',f'hsv_color_2',0,255, lambda x:x)
cv2.createTrackbar('low_g',f'hsv_color_2',101,255, lambda x:x)
cv2.createTrackbar('low_r',f'hsv_color_2',113,255, lambda x:x)
cv2.createTrackbar('high_b',f'hsv_color_2',110,255, lambda x:x)
cv2.createTrackbar('high_g',f'hsv_color_2',255,255, lambda x:x)
cv2.createTrackbar('high_r',f'hsv_color_2',255,255, lambda x:x)

cv2.namedWindow(f'hsv_color_3')
cv2.createTrackbar('low_b',f'hsv_color_3',2,255, lambda x:x)
cv2.createTrackbar('low_g',f'hsv_color_3',41,255, lambda x:x)
cv2.createTrackbar('low_r',f'hsv_color_3',96,255, lambda x:x)
cv2.createTrackbar('high_b',f'hsv_color_3',48,255, lambda x:x)
cv2.createTrackbar('high_g',f'hsv_color_3',77,255, lambda x:x)
cv2.createTrackbar('high_r',f'hsv_color_3',156,255, lambda x:x)

cv2.namedWindow(f'hsv_color_4')
cv2.createTrackbar('low_b',f'hsv_color_4',1,255, lambda x:x)
cv2.createTrackbar('low_g',f'hsv_color_4',0,255, lambda x:x)
cv2.createTrackbar('low_r',f'hsv_color_4',62,255, lambda x:x)
cv2.createTrackbar('high_b',f'hsv_color_4',66,255, lambda x:x)
cv2.createTrackbar('high_g',f'hsv_color_4',33,255, lambda x:x)
cv2.createTrackbar('high_r',f'hsv_color_4',126,255, lambda x:x)

cv2.namedWindow(f'hsv_color_5')
cv2.createTrackbar('low_b',f'hsv_color_5',0,255, lambda x:x)
cv2.createTrackbar('low_g',f'hsv_color_5',67,255, lambda x:x)
cv2.createTrackbar('low_r',f'hsv_color_5',0,255, lambda x:x)
cv2.createTrackbar('high_b',f'hsv_color_5',67,255, lambda x:x)
cv2.createTrackbar('high_g',f'hsv_color_5',108,255, lambda x:x)
cv2.createTrackbar('high_r',f'hsv_color_5',53,255, lambda x:x)

cv2.namedWindow(f'hsv_color_6')
cv2.createTrackbar('low_b',f'hsv_color_6',64,255, lambda x:x)
cv2.createTrackbar('low_g',f'hsv_color_6',0,255, lambda x:x)
cv2.createTrackbar('low_r',f'hsv_color_6',0,255, lambda x:x)
cv2.createTrackbar('high_b',f'hsv_color_6',148,255, lambda x:x)
cv2.createTrackbar('high_g',f'hsv_color_6',117,255, lambda x:x)
cv2.createTrackbar('high_r',f'hsv_color_6',28,255, lambda x:x)

class control_hsv:
    def __init__(self):
        pass

    def hsv_controls(self, number_color):

        low_blue = int(cv2.getTrackbarPos('low_b', f'hsv_color_{number_color}'))
        low_green = int(cv2.getTrackbarPos('low_g', f'hsv_color_{number_color}'))
        low_red = int(cv2.getTrackbarPos('low_r', f'hsv_color_{number_color}'))
        high_blue = int(cv2.getTrackbarPos('high_b', f'hsv_color_{number_color}'))
        high_green = int(cv2.getTrackbarPos('high_g', f'hsv_color_{number_color}'))
        high_red = int(cv2.getTrackbarPos('high_r', f'hsv_color_{number_color}'))   

        return low_blue, low_green, low_red, high_blue, high_green, high_red     
import cv2

video = cv2.VideoCapture('C:\python class\2022-06-01 14-55-01.mkv')
while True:
    state ,img = video.read()
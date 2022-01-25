import cv2

cap = cv2.VideoCapture(0)

while True:
    try:
        success, img = cap.read()

        cv2.imshow('Image', img)
        cv2.waitKey(1)
    except Exception as e:
        print("Exception happened: {}".format(e))
        continue
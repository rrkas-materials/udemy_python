import cv2, time

video = cv2.VideoCapture(0)
    # idx   (int): index of camera hardware to capture video from
    # path  (str): path of video

a=1

while True:
    a=a+1
    check, frame = video.read()

    # print(check)  #check video is running or not
    # print(frame)  #3-d array of 1st image of video

    # time.sleep(5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('', gray)

    key = cv2.waitKey(10)

    if key==ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
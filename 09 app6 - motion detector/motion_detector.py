from datetime import datetime

import cv2, pandas

video = cv2.VideoCapture(0)
first_frame = None
status_list = [0]
times = []
column_start = 'Start'
column_end = 'End'
df = pandas.DataFrame(columns=[column_start, column_end])

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    status_list.append(status)

    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow('frame', frame)
    cv2.imshow('delta', delta_frame)
    cv2.imshow('gray', gray)
    cv2.imshow('thresh', thresh_delta)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)

for i in range(0, len(times), 2):
    df = df.append({column_start: times[i], column_end: times[i + 1]}, ignore_index=True)

df.to_csv('Times.csv')

video.release()
cv2.destroyAllWindows()

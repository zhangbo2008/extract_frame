# 视频分针.
#!/usr/bin/env python
import cv2
numer = 18
cap=cv2.VideoCapture("huabu.MP4")

if cap.isOpened():
    ret,frame=cap.read()
else:
    ret = False

n=0
i=0
timeF = 1
path=u'huabu/{}'
while ret:
    n = n + 1
    ret,frame=cap.read()
    if (n%timeF == 0) :
        i = i+1
        print(i)
        filename=str(numer)+"_"+str(i)+".jpg"
        kkk=path.format(filename)
        cv2.imwrite(kkk,frame)
    cv2.waitKey(1)

cap.release()

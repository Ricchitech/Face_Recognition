import cv2
face_cascade= cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade= cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_eye.xml')
img = cv2.imread('b.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces= face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    img= cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0),2)
    gray_img=gray[y:y+h, x:x+w]
    color_img=img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(gray_img)

    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(color_img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
from cv2 import cvtColorTwoPlane
# from emotion_dec import ExpressionModel
import emotion_dec
import numpy as np

faceCasc = cv2.CascadeClassifier('haar_cascade.xml')
model = emotion_dec.ExpressionModel('model.json', 'model_weights.h5')
font = cv2.FONT_HERSHEY_COMPLEX


class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_video(self):
        _, fr = self.video.read()
        cor_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = faceCasc.detectMultiScale(cor_fr, 1.3, 5)

        for (x, y, w, z) in faces:

            fc = cor_fr[y:y+z, x:x+w]

            roi = cv2.resize(fc, (48, 48))

            predic = model.emotionDec(roi[np.newaxis, :, :, np.newaxis])

            cv2.putText(fr, predic, (x, y), font, 0.5, (0, 255, 0), 2)
            cv2.rectangle(fr,(x,y),(x+w, y+z), (241, 226, 180), 2)

        return fr
        

def gen(camera):
    while True:
        frame = camera.get_video()
        cv2.imshow('Face_Rec',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

gen(Video())

#Otimizar o código para reconhecimento facial

# gen(cv2.imshow("Grayscale", cv2.COLOR_BGR2GRAY))
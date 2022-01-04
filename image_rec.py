from fer import FER
import matplotlib.pyplot as plt
import cv2
from plyer import notification
def capture():
    camera_port=0
    ramp_frames=30
    camera=cv2.VideoCapture(camera_port)

    def getimage():
        retval, im=camera.read()
        return im
    for i in range(ramp_frames):
        temp=getimage()
    camera_capture=getimage()
    file="C:\\Users\\Lenovo\\MiniProject\\face1.jpeg"
    cv2.imwrite(file,camera_capture)

    del camera
activate=False
def notice(emotion):
    notification.notify(
        title="Emotion detected",
        message="Emotion found: "+emotion,
        timeout=10,
    )
capture()
img4=plt.imread("C:\\Users\\Lenovo\\MiniProject\\face1.jpeg")
detector=FER(mtcnn=True)
emotion, score=detector.top_emotion(img4)
if emotion=="sad":
    notice(emotion)
    activate=True
    print("happy")
elif emotion=="angry":
    notice(emotion)
    activate=True
    print("calm")
elif emotion=="disgust":
    notice(emotion)
    activate=True
    print("pleasure")
elif emotion=="neutral":
    notice(emotion)
    activate=True
    print("soothing")
elif emotion=="happy":
    notice(emotion)
    activate=True
    print("done")
else:
    print("None")
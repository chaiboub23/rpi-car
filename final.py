from LaneDetect import getLaneCurve
import cam
import explorerhat

def main():
    img = cam.get()
    curveVal = getLaneCurve(img, 1)

    sen = 1.3  # SENSITIVITY
    if curveVal==1:
        explorerhat.motor.stop()
        explorerhat.motor.one.forwards(0.20* sen)
        explorerhat.motor.two.forwards(0.20)
    elif curveVal==-1:
        explorerhat.motor.stop()
        explorerhat.motor.two.forwards(0.20* sen)
        explorerhat.motor.one.forwards(0.20)
    elif curveVal==0:
        explorerhat.motor.stop()
        explorerhat.motor.forwards(0.20)
    else:
        explorerhat.motor.stop()
    # cv2.waitKey(1)


if __name__ == '__main__':
    while True:
        main()
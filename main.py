import cv2
import time
face_cascade = cv2.CascadeClassifier(
    "D:\\COLLEGE\\programs\\py\\haarcascade_frontalface_default.xml")
default_img = "C:\\Users\\NAVYA JAIN\\Pictures\\s.jpg"
img_path = "D:\\COLLEGE\\programs\\py\\capturedImage.jpg"
imgPath = ""
print("|"+"-"*48+"|")
print("| "+"Welcome to Face Recognizer".center(47)+"|")
print("|"+"-"*48+"|")
time.sleep(1)
Run = True
while Run:
    print("| 1. Open From Device.".ljust(48)+" |")
    print("| 2. Capture New Image".ljust(48)+" |")
    print("| 3. Select Defult Image".ljust(48)+" |")
    print("| 4. Exit".ljust(48)+" |")
    print("|"+"-"*48+"|")
    choice = int(input("| Enter Your Choice:(1-4):- ".ljust(48)+" |"))
    if choice == 1:
        while not imgPath:
            imgPath = input(
                "| Enter Image Path for Face Detection : ".ljust(48)+" |")
            if imgPath:
                img = cv2.imread(imgPath)
    elif choice == 2:
        image = True
        print("| Capturing Image".ljust(48)+" |")
        while image:
            cam = cv2.VideoCapture(0)
            s, capture = cam.read()
            if s:
                print("| Image Captured".ljust(48)+" |")
                time.sleep(1)
                print("| Verify Image".ljust(48)+" |")
                time.sleep(1)
                cv2.imshow("| Enter y for Select and r for Retake ", capture)
                key = cv2.waitKey(0)
                if key == ord('y'):
                    image = False
                    cv2.destroyAllWindows()
                    print("| Image Verified".ljust(48)+" |")
                    time.sleep(1)
                else:
                    print("| Recapturing Image".ljust(48)+" |")
                    cv2.destroyAllWindows()
            cv2.imwrite("capturedImage.jpg", capture)
            img = cv2.imread(img_path)
    elif choice == 4:
        Run = False
        print("|"+"-"*48+"|")
        print("| "+"Thanks for using Face Recognizer...".center(47)+"|")
        print("|"+"-"*48+"|")
        cv2.release()
        break
    else:
        img = cv2.imread(default_img)
    print("| "+"Reading Image".ljust(47)+"|")
    time.sleep(1)
    print("| "+"Searching for faces".ljust(47)+"|")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray_img, scaleFactor=1.14, minNeighbors=3, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)
    if len(faces) != 0:
        for x, y, w, h in faces:
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
        resize = cv2.resize(img, (600, 600))
        print("| "+"{} Faces Found".format(len(faces)).ljust(47)+"|")
        cv2.imshow("{} Face Found".format(len(faces)), resize)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("| "+"Selected Image Does Not have any Face".ljust(47)+"|")
    time.sleep(2)
    print("|"+"-"*48+"|")

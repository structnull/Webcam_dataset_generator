import cv2 as cv
import os

camera = cv.VideoCapture(0)
path = '~/path/to/folder/for/dataset'

if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()

#creating a list of Labels
Labels = ["Happy","Calm","Angry","Sad","Suprised"]

for folder in Labels:
    count = 0
    print("Press 's' to start data collection for"+folder)
    userinput = input()
    if userinput != 's':
        print("Wrong Input..........")
        exit()
    while count<200:
        status, frame = camera.read()
        if not status:
            print("Frame is not been captured..Exiting...")
            break
        #convert the image into gray format for fast caculation
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("Video Window",gray)
        #resizing the image to store it
        gray = cv.resize(gray, (1280,720))
        #Store the image to specific label folder
        cv.imwrite(path+folder+'/img'+str(count)+'.png',gray)
        count=count+1
        # count data taken
        for i in range(count):
            print(count)
        #to quit the display window press 'q'
        if cv.waitKey(1) == ord('q'):
            break
camera.release()
cv.destroyAllWindows()


#creating folders for each label to store images
for label in Labels:
    if not os.path.exists(label):
        os.mkdir(label)

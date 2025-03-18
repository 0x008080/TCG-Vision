import cv2
import os

cap = cv2.VideoCapture(2)
img_counter = 0
folder_path = "images/"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to grab frame")
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'): #q key to quit program
        print("Exiting webcam view")
        break

    elif cv2.waitKey(1) == ord('s'): # s key to take picture
        img = "pokemon_{}.png".format(img_counter)
        save_path = os.path.join(folder_path, img)
        cv2.imwrite(save_path, frame)
        print("{} written!".format(img))
        #img_counter += 1

cap.release()
cv2.destroyAllWindows()
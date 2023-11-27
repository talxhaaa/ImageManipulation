import cv2
#initialize the webcam
cap = cv2.VideoCapture(0)
#Main loop for real-time image manipulation
while True:
    #Capture a frame from the webcam status
    photo = cap.read()
    #Extract a region of interest (ROI) from the captured frame
    photo1 = photo[150:400, 200:450]
    #Resize the extracted ROI
    photo1_resized = cv2.resize(photo1,(200, 200))
    #Replace a portion of the original frame with the resized ROI
    photo[0:200, 0:200, :] = photo1_resized
    #display the merged image
    cv2.imshow("Merged Photo", photo) 
    if cv2.waitKey(100) == 13: 
        break
#close all OpenCV windows and release webcam
cv2.destroyAllWindows() 
cap.release() 
 
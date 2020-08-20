# import the opencv library
import cv2
# definig a video capture object
# cap = cv2.VideoCapture('http://0.0.0.0:5000/video_feed')
cap = cv2. VideoCapture(0)
# Capturing video from webcam (default)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    # q is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
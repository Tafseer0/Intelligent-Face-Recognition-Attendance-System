import cv2

# Replace 'http://IP_ADDRESS:PORT_NUMBER/video' with the IP camera URL
url = 'http://100.92.150.188:8080/video'

cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Process the frame as needed
    cv2.imshow('IP Camera Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

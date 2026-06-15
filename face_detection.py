import cv2
import os

print("Current Folder:", os.getcwd())
print("Files:", os.listdir())

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load image
# Load image

print(os.path.exists(r"C:\Users\ELCOT\Documents\MissingpersonsAI\test.jpeg"))
print(os.path.exists(r"uploads\WIN_20260423_03_02_13_Pro.jpg"))

img = cv2.imread(r"uploads\WIN_20260423_03_02_13_Pro.jpg")

print(img)


# Check image loaded
if img is None:
    print("Error: test.jpg not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

print("Faces Detected:", len(faces))

# Draw rectangle around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Show result
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

# Load the thermal image
img = cv2.imread("thermal_image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to the image to segment the objects
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Find the contours of the objects in the image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over the contours
for cnt in contours:
    # Get the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(cnt)
    if (h < (img.shape[0]/2)):
        print("Non-Human")
    else:
        print("Human")

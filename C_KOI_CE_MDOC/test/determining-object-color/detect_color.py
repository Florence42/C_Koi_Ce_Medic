# USAGE
# python detect_color.py --image example_shapes.png

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
from pyimagesearch.colorlabeler import ColorLabeler
import imutils
import cv2


cam = cv2.VideoCapture(0)

if (cam.isOpened()== False):
  print("Error opening video stream or file")

# Read until video is completed
while(cam.isOpened()):
  ret, image = cam.read()
  resized = imutils.resize(image, width=300)
  ratio = image.shape[0] / float(resized.shape[0])

  if ret == True:
      blurred = cv2.GaussianBlur(resized, (5, 5), 0)
      gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
      lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
      thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]
      cv2.imshow("Thresh", thresh)

      cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      cnts = cnts[0] if imutils.is_cv2() else cnts[1]

      sd = ShapeDetector()
      cl = ColorLabeler()
      for c in cnts:
          M = cv2.moments(c)
          try:
            cX = int((M["m10"] / M["m00"]) * ratio)
          except:
            cX = 0
          try:
            cY = int((M["m01"] / M["m00"]) * ratio)
          except:
            cY = 0

      shape = sd.detect(c)
      color = cl.label(lab, c)

      c = c.astype("float")
      c *= ratio
      c = c.astype("int")
      text = "{} {}".format(color, shape)
      cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
      cv2.putText(image, text, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

      cv2.imshow("Image", image)
      cv2.waitKey(0)
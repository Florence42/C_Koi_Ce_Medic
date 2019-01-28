import cv2
print(cv2.__version__)
import numpy as np



def get_m_color(pixel) :
    some = [0,0,0]
    size = len(pixel)
    for i in range(0,size):
        some[0] +=  pixel[i][0]
        some[1] +=  pixel[i][1]
        some[2] +=  pixel[i][2]
    some[0] = int(some[0]/size)
    some[1] = int(some[1]/size)
    some[2] = int(some[2]/size)
    return some

def make_mask(uper,lower):
    # uper = np.array([30, 255, 255]) #([55,254,248])
    # lower=  np.array([10, 70, 70]) #([44,199,194])
    mask = cv2.inRange(hsv, lower, uper)
    return mask
    

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0)
nb_pixel = 50
pixel = []
moyen = []
# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    y_mask = make_mask(np.array([30, 255, 255]) ,np.array([10, 70, 70]))
    # r_mask =  make_mask(np.array([0,255,255]), np.array([0,70,70])) # pas top
    # b_mask =  make_mask(np.array([0,100,100]), np.array([0,40,20])) # pas top

    cv2.imshow('mask',y_mask)
    

    # uncoment for pixelle moyenne au centre 
    # on recupere un pixel
    # height, width = frame.shape[:2]
    # print(width,height)
    # pixel = []
    # for x  in  range(0,nb_pixel):  #on recuper un groupement de pixel de nb_pixel
    #     for y in range(0,nb_pixel):
    #         pixel.append(frame[int(height/2 - nb_pixel/2  + x), int(width/2  - (nb_pixel/2)+ y)])
    # # print(pixel)
    # moyen = get_m_color(pixel) # on fait la moyenne des couleur des pixelle
    # # print(moyen)
    # for x  in  range(0,nb_pixel):  #trace la zone de detection
    #     for y in range(0,nb_pixel):
    #         if ( (x == 0)  | (y == 0)): # manque de borne mais vous avez lidé
    #             x_p = int((height/2) - nb_pixel/2 + x)
    #             y_p = int((width/2) - nb_pixel/2 + y)
    #             # print(x_p , y_p)
    #             frame[x_p][y_p] = [255,255,255]

    # pixel = frame[int(height/2), int(width/2)]
    # print(pixel)

    # Display the resulting frame
    cv2.imshow('Frame',frame)
    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Break the loop
#   else:
#     break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

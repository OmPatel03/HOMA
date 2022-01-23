# Import cv2 and pytesseract libraries
import cv2 
from pytesseract import pytesseract 

# tesseract function uses pytesseract library to convert the image text 
# into a string and prints it out  

def tesseract(): 
  path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
  Imagepath = 'test1.jpg' 
  img = cv2.imread('test1.jpg') 
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
  pytesseract.tesseract_cmd = path_to_tesseract 
  text = pytesseract.image_to_string(img) 
  print (text[:-1]) 
  
# readImage function accesses the users webcam to take a picture and then uses 
# openCV library to recognize text in the image

def readImage(): 
  cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
  while True: 
    _,Image = cam.read() 
    cv2.imshow('Text detection', Image) 
    if cv2.waitKey(1)& 0xFF==ord('s'): 
      cv2.imwrite('test1.jpg', Image) 
      break 
    
  cam.release() 
  cv2.destroyAllWindows() 
  return tesseract()

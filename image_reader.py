
import cv2 
from pytesseract import pytesseract 
  
def tesseract(): 
  
  path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
  Imagepath = 'test1.jpg' 
  img = cv2.imread('test1.jpg') 
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
  pytesseract.tesseract_cmd = path_to_tesseract 
  text = pytesseract.image_to_string(img) 
  print (text[:-1]) 
    
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

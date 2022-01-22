def read_Image(file_path): 
  
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
  
  # Reading image 
  img = cv2.imread(file_path) 
  
  # Convert to RGB 
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
  
  # Detect texts from image 
  texts = pytesseract.image_to_string(img) print(texts)

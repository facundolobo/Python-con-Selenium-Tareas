import cv2
import pytesseract #para leer imagenes y mas

imagen = cv2.imread("ejemplo pytesseract.jpg")
pytesseract.pytesseract.tesseract_cmd= "C:\Program Files\Tesseract-OCR\\tesseract.exe"

texto = pytesseract.image_to_string(imagen)

print (texto)
#opencv
import cv2 as cv
import docx as doc

from PIL import Image
import pytesseract as pyt

#print(pyt.image_to_string(Image.open('/Users/viniciusm/Desktop/projects/projects-python/cpfl.jpeg')))

#pyt.pyt.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

teste = input("Você quer tirar uma foto? S/N ")

if((teste == "S") or (teste == "s")):
    video = cv.VideoCapture("http://192.168.33.107:8080/video")

    while(True):
        ret, frame = video.read()
        cv.imshow('frame',frame) 
        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.imwrite('frame.png',frame)
            cv.destroyAllWindows() 
            break
    captura = cv.imread("frame.png") 
else:
    captura = cv.imread(input("Digite o nome do arquivo: ")) 

resultado = pyt.image_to_string(captura)
print(resultado)

wordDoc = doc.Document() 
wordDoc.add_paragraph(resultado) 
wordDoc.save('teste.docx')


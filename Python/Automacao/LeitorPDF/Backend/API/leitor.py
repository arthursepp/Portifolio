import pytesseract
from PIL import Image
import fitz
from pypdf import PdfReader
import cv2
import io
import re
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class TesseractOCR:
    def get_text(self, img_path):
        img = cv2.imread(img_path)
        text = pytesseract.image_to_string(img, lang='por')
        return text
    
ocr = TesseractOCR()

conteudo = ""

# Verificando se o pdf contém alguma imagem:
def tem_imagem(caminho):
    doc = fitz.open(caminho)
    try:
        for numero_pagina in range(len(doc)):
            pagina = doc[numero_pagina]
            imagens = pagina.get_images(full=True)
            if len(imagens) > 0:
                return True
        return False
    finally:
        doc.close()
        
# Extraindo e lendo o conteúdo do pdf
def leitor_texto(caminho):
    leitor = PdfReader(caminho)
    texto_total = ""
    for numero_pagina in range(len(leitor.pages)):
        pagina = leitor.pages[numero_pagina]
        texto = pagina.extract_text()
        texto_total += texto + "\n"
        
    conteudo = texto_total
    return texto_total

# Extraindo e lendo o texto de uma imagem:
def leitor_imagem(caminho):
    doc = fitz.open(caminho)
    texto_total = ""
    
    for numero_pagina in range(len(doc)):
        pagina = doc[numero_pagina]
        imagens = pagina.get_images(full=True)
        
        if imagens:  # Se a página tiver imagens
            for img_index, img in enumerate(imagens):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                imagem = Image.open(io.BytesIO(image_bytes))
                texto = pytesseract.image_to_string(imagem, lang="por")
                texto_total += texto + "\n"
        else:  # Se a página NÃO tiver imagens, usa o leitor de texto
            texto_pagina = pagina.get_text("text")  # Usando o método para obter o texto da página
            texto_total += texto_pagina + "\n"
    
    return texto_total

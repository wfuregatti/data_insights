import os, fitz
from openpyxl import Workbook

pth = "./Certificates"

workbook = Workbook()
worksheet = workbook.active

line = 0

def get_info(tx,par):
    if par == 'I':
        for ln in tx:
            if ln[0:15] == 'Certificate Id:' or ln[0:15] =='Certificate No:':
                return ln[16:]
    elif par == 'C':
        for ln in tx:
            if ln[0:19] == 'Course completed on':
                return ln
 

for certificate in os.listdir(path=pth):
    if certificate.endswith('.pdf'):
        line += 1
        
        pdfFileObj = fitz.open(pth+"/"+certificate)
        pageObj = pdfFileObj.loadPage(0)
        pageText = pageObj.getText()
        
        textlines = pageText.split('\n')
        
        worksheet["A"+str(line)]=textlines[2]
        worksheet["B"+str(line)]=get_info(textlines, 'C')
        worksheet["C"+str(line)]=get_info(textlines, 'I')

workbook.save("Certificates.xlsx")


        
        








import PyPDF2 
import sys
import os

merger = PyPDF2.PdfWriter()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combinedUniDocs.pdf")    
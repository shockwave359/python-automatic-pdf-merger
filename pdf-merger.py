import PyPDF2 
import os
from datetime import datetime

merger = PyPDF2.PdfWriter()
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
combinedName = now + ".pdf"

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)

with open(combinedName, 'wb') as output_file:
    merger.write(output_file)
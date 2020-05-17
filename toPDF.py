import pdfkit 
from PyPDF2 import PdfFileMerger


pdfkit.from_file('index-page-1-fr.html', 'cv-1-fr.pdf')
pdfkit.from_file('index-page-2-fr.html', 'cv-2-fr.pdf')
cvPdfPages = ['cv-1-fr.pdf', 'cv-2-fr.pdf']

merger = PdfFileMerger(strict=False)

for pdf in cvPdfPages:
    merger.append(pdf)

merger.write("cv-fr.pdf",)
merger.close()
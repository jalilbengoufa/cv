import pdfkit 
from PyPDF2 import PdfFileMerger


pdfkit.from_file('index-page-1-fr.html', 'cv-1-fr.pdf')
pdfkit.from_file('index-page-2-fr.html', 'cv-2-fr.pdf')
pdfkit.from_file('index-page-1-en.html', 'cv-1-en.pdf')
pdfkit.from_file('index-page-2-en.html', 'cv-2-en.pdf')
cvPdfPagesFr = ['cv-1-fr.pdf', 'cv-2-fr.pdf']
cvPdfPagesEn = ['cv-1-en.pdf', 'cv-2-en.pdf']

mergerFr = PdfFileMerger(strict=False)

for pdf in cvPdfPagesFr:
    mergerFr.append(pdf)
    
mergerFr.write("Jalil-Bengoufa-cv-fr.pdf",)
mergerFr.close()

mergerEn = PdfFileMerger(strict=False)

for pdf in cvPdfPagesEn:
    mergerEn.append(pdf)

mergerEn.write("Jalil-Bengoufa-cv-en.pdf",)
mergerEn.close()
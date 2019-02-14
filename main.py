import PyPDF2

#pdf import code from https://www.geeksforgeeks.org/working-with-pdf-files-in-python/

#file Object
pdfFileObj = open('samplePDF.pdf', 'rb')
#reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
#page Object
pageObj = pdfReader.getPage(0)
#extract Text from Page
print(pageObj.extractText())
pdfFileObj.close()
print('Imported PyPDF2');
print('Imported PyPDF2');
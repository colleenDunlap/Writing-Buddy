import PyPDF2
import unicodedata
import binascii
#pdf import code from https://www.geeksforgeeks.org/working-with-pdf-files-in-python/

#file Object
pdfFileObj = open('samplePDFMultiPage.pdf', 'rb')
#reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
numPages = pdfReader.numPages
words = []
#page Object
for iPage in range(0,numPages):
	pageObj = pdfReader.getPage(iPage)
	text = pageObj.extractText()
	#text.remove('\n')
	words2 = text.split(' ')
	words2 = list(filter(lambda x: x!= '\n', words2))
	words2 = list(filter(lambda x: x!= '', words2))
	words2 = list(filter(lambda x: len(x)>3, words2))
	print(words2)
	words.extend(words2)
for iWord in range(0, len(words)):
	words[iWord] = words[iWord].replace(",","")
	words[iWord] = words[iWord].replace("/","")
	words[iWord] = words[iWord].replace("(","")
	words[iWord] = words[iWord].replace(")","")
	words[iWord] = words[iWord].replace(".","")
	words[iWord] = words[iWord].replace("-","")
	words[iWord] = words[iWord].replace("\n","")
	words[iWord] = words[iWord].lower()
	print(words[iWord])
print(words)
pdfFileObj.close()


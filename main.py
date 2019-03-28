import PyPDF2
import unicodedata
import binascii
#pdf import code from https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
#array of object code inspiration https://www.daniweb.com/programming/software-development/code/216631/a-list-of-class-objects-python
#linked list object code inspiration https://dbader.org/blog/python-linked-list
def calcHash(word):
	wordSum = 0;
	for iLetter in range(0, len(word)):
		wordSum = wordSum + (ord(word[iLetter]))#return ascii
	return (wordSum%89)
class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, frequency=None, next=None, word=None):
        self.frequency = frequency
        self.next = next
        self.word = word
    def __repr__(self):
        return repr(self.frequency)
class SinglyLinkedList:
	def __init__(self):
		self.head = None
	def append(self, word):
		if not self.head:
			self.head = ListNode(word=word, frequency = 1)
			return self.head
		curr = self.head
		while curr.next:
			if curr.word == word:
				curr.frequency = curr.frequency + 1;
				return curr;
			curr = curr.next	
		curr.next = ListNode(word=word, frequency = 1)
		return curr.next;
	def __repr__(self):
		nodes = []
		curr = self.head
		while curr:
			nodes.append(repr(curr))
			curr = curr.next
		return '[' + ', '.join(nodes) + ']'

#file Object
pdfFileObj = open('samplePDFMultiPage.pdf', 'rb')
#reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numPages = pdfReader.numPages
words = []
chainList = []
for iList in range(0, 89):#because we mod by 89, only 89 possible hashes
	chainList.append(SinglyLinkedList())
#page Object
for iPage in range(0,numPages):
	pageObj = pdfReader.getPage(iPage)
	text = pageObj.extractText()
	#text.remove('\n')
	words2 = text.split(' ')
	words2 = list(filter(lambda x: x!= '\n', words2))
	words2 = list(filter(lambda x: x!= '', words2))
	words2 = list(filter(lambda x: len(x)>3, words2))
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

pdfFileObj.close()
for iWord in range(0, len(words)):
	hash = calcHash(words[iWord])
	print(hash);
	test = chainList[hash].append(words[iWord])
	print(test.word);
print(chainList[18])


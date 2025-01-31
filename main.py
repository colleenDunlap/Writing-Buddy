import PyPDF2
import unicodedata
import time
import binascii
from thesaurus import Word
from PyDictionary import PyDictionary

#pdf import code from https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
#array of object code inspiration https://www.daniweb.com/programming/software-development/code/216631/a-list-of-class-objects-python
#linked list object code inspiration https://dbader.org/blog/python-linked-list

#Function to calculate the ascii sum and return hash index using key of 89
def calcHash(word):
	wordSum = 0;
	for iLetter in range(0, len(word)):
		wordSum = wordSum + (ord(word[iLetter]))#return ascii
	return (wordSum%89)

#Function to handle when a synonym cannot be found
def synonymErrorHandle(curr):
	#assert ('linux' in sys.platform), "Function can only run on Linux systems."
	print("Common Word: " + curr.word);
	input_word = Word(curr.word)
	print(input_word.synonyms())


#a node in a singly-linked list
class ListNode:
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

class DoubleListNode:
	def __init__(self, frequency=None, next=None, word=None, prev = None):
		self.frequency = frequency
		self.next = next
		self.prev = prev
		self.word = word
	def __repr__(self):
		return repr(self.word)

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	def append(self, word):
		if not self.head:
			self.head = DoubleListNode(word=word, frequency = 0)
			self.tail = self.head
			self.head.next = None;
			return self.head
		curr = self.head
		while curr.next:
			curr = curr.next	
		curr.next = DoubleListNode(word=word, frequency = 0)
		curr.prev = curr;
		return curr.next;
	def insert(self, word, frequency):
		curr = self.head;
		while curr:
			if(curr.word==word):
				
				return;
			curr = curr.next;
		curr = self.head;
		while curr.next:

			if(curr.frequency<frequency):
				n = DoubleListNode(word = word, frequency=frequency)
				
				if(curr == self.head):
					self.head = n;
				n.next = curr.next;
				curr.next.prev = n;
				n.prev = curr.prev;
				curr.prev.next = n;
				return;
			curr = curr.next;
	def printSynonyms(self):
		curr = self.head;
		while curr.next:
			try:
    				synonymErrorHandle(curr)
			except:
    				print("no synonym found")
			print(" ")
			curr = curr.next
	def printDefinitions(self):
		dictionary= PyDictionary
		curr = self.head;
		while curr.next:
			print("Common Word: " + curr.word);
			definition = dictionary.meaning(curr.word)
			print(definition)
			print("")
			curr = curr.next
	def __repr__(self):
		nodes = []
		curr = self.head
		while curr:
			nodes.append(repr(curr))
			curr = curr.next
		return '[' + ', '.join(nodes) + ']'


#file Object
start = time.time()
pdfFileObj = open('language.pdf', 'rb')

#reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numPages = pdfReader.numPages

words = []
chainList = []

cacheMin = 0;

cacheList = []
cacheList = DoublyLinkedList();
for iList in range(0,20):#frequent words cache
	cacheList.append("")

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
	words2 = list(filter(lambda x: len(x)>4, words2))
	words.extend(words2)
for iWord in range(0, len(words)):
	words[iWord] = words[iWord].replace(",","")
	words[iWord] = words[iWord].replace("%","")
	words[iWord] = words[iWord].replace(":","")
	words[iWord] = words[iWord].replace("/","")
	words[iWord] = words[iWord].replace("(","")
	words[iWord] = words[iWord].replace(")","")
	words[iWord] = words[iWord].replace(".","")
	words[iWord] = words[iWord].replace("-","")
	words[iWord] = words[iWord].replace("that","")
	words[iWord] = words[iWord].replace("\n","")
	words[iWord] = words[iWord].lower()

pdfFileObj.close()
#loop to store each word in the hash table
for iWord in range(0, len(words)):
	hash = calcHash(words[iWord])
	node = chainList[hash].append(words[iWord])
	if (node.frequency>cacheMin):
		cacheList.insert(node.word, node.frequency)
		cacheMin = cacheList.tail.prev.frequency;

print("For n of " + str(len(words)))
end = time.time()
print("Execution Time Was " + str((end-start)))
print("") #return to new line for clarity

print("would you like to a)revise or b)learn?")
response = input(); #read in user response

print("Most common words: ")
print(cacheList)
print("") #return to new line for clarity

if response == 'a':
	print("Synonyms: ")
	cacheList.printSynonyms()

else:
	cacheList.printDefinitions()

#spacing added at the bottom for clarity
print("")
print("")
print("")
import spacy

class Ontobot:
	def __init__(self, language='en'):
		if language == 'en':
			self.nlp = spacy.load('en')
		else:
			self.nlp = spacy.load('en')

	#Copper ears
	def listen(text_string):
		print('s')
		
	#Tin braing
	def reason(concepts):
		print('s')
		
	#Leather tongue
	def answer(text_string):
		concepts = listen(text_string)
		answer = reason(concepts)
		return answer;	
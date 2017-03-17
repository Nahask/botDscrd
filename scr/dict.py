import json

class DictionaryHandler(object):
	"""docstring for DictionaryHandler"""
	def __init__(self):
		self.file = 'dictionary.txt'
		self.dictionary = {}
		self.loadDict()
		self.loop = 0

	def loadDict(self):
		try:
			with open(self.file, 'r') as file:
				s = file.read()
				self.dictionary = json.loads(s)
		except Exception:
			return
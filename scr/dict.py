import json

class DictionaryHandler(object):
	"""docstring for DictionaryHandler"""
	def __init__(self):
		self.file = './dictionary.txt'
		self.dictionary = {}
		self.loadDict()
		self.loop = 0

	def loadDict(self):
		try:
			with open(self.file, 'r') as f:
				s = f.read()
				self.dictionary = json.loads(s)
		except Exception:
			print("error opening file")
			return

	def readEntry(self, entry, channelName):
		self.loop = self.loop + 1
		if self.loop > 10:
			print("error loop")
			return None
		if entry in self.dictionary:
			while entry in self.dictionary:
				entry = self.dictionary[entry]
			return entry
		else:
			entryText = entry.split('.')[0] if isinstance(entry, str) else ''
			chName = channelName if isinstance(channelName, str) else ''
			return self.readEntry(entryText + '.' + chName, chName)
		

	def commandHandler(self, params, channelName = ''):
		self.loop = 0
		return self.readEntry('.'.join(params.split(' ')), channelName)

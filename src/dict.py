import json
import random

class DictionaryHandler(object):
	"""docstring for DictionaryHandler"""
	def __init__(self):
		self.file = './dictionary.json'
		self.dictionary = {}
		self.hidden = []
		self.loadDict()
		for test in self.dictionary['hidden']:
			self.hidden.append(test)
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

	def selectResponse(self, target, channelName):
		arrayTargetSize = len(self.dictionary['hidden'][target])
		randomMessage  = random.randint(0, arrayTargetSize - 1)
		message = self.dictionary['hidden'][target][str(randomMessage)]
		return(message)



	def hiddenMessageHandler(self, message, channelName = ''):
		for target in self.hidden:
			if target in message:
				return self.selectResponse(target, channelName)

	def commandHandler(self, message, channelName = ''):
		self.loop = 0
		return self.readEntry('.'.join(message.split(' ')), channelName)

import pyjd # this is dummy in pyjs.
import pygwt

# async request
class HTTPAsyncRequestHandler:
	"""
		Usage: 
			- 	Instantiation
			-	Subclassing:
			In both cases setting (texts, messagePanels), and/or (callbacks) parameter(s)
			in construction or through attributs
	"""
	texts = None
	messagePanel = None
	callbacks = None

	def __init__(self, texts=None, messagePanel=None, callbacks=None):
		self.texts = texts
		self.messagePanel = messagePanel
		self.callbacks = callbacks	

	def onCompletion(self, text):
		if self.messagePanel and self.texts and 'onCompletion' in self.texts:
			self.messagePanel.add(HTML(self.texts['onCompletion']))
		if self.callbacks and 'onCompletion' in self.callbacks:
			self.callbacks['onCompletion'](text)

	def onError(self, text, code):
		if self.messagePanel and self.texts and 'onError' in self.texts:
			self.messagePanel.add(HTML(texts['onError'] % (text, code)))
		if self.callbacks and 'onError' in self.callbacks:
			self.callbacks['onError'](text, code)

	def onTimeout(self, text):
		if self.messagePanel and self.texts and 'onTimeout' in self.texts:
			self.messagePanel.add(HTML(texts['onTimeout'] % text))
		if self.callbacks and 'onTimeout' in self.callbacks:
			self.callbacks['onTimeout'](text)



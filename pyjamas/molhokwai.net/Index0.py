import pyjd # this is dummy in pyjs.
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Hyperlink import Hyperlink
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Grid import Grid
from pyjamas.ui.Label import Label
from pyjamas.HTTPRequest import HTTPRequest
from pyjamas import Window
import pygwt
location = Window.getLocation()


def locationObjPanel():
	vpl = VerticalPanel();
	vpl.add(HTML(location.getPageHref(self)))
	vpl.add(HTML(location.getSearchVar('theme')))
	vpl.add(HTML(location.getSearch(self)))
	return vpl

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


class Index():
	themesRequestTexts = None
	themesRequestCallbacks = None

	def __init__(self):
		self.themesRequestTexts = {
			'onCompletion' : 'Themes fetched, displaying/displayed.',
			'onError' : 'An error occured fecthing themes, displaying static themes (error details - text:%s, code:%s)',
			'onTimeout' : 'Timed out fetching themes, displaying static themes (error details - text:%s)'
		}
		self.themesRequestCallbacks = {
			'onCompletion' : self.addThemesPanel
		}

	def messagePanel(self):
		return self.htmlElements()[1][1]

	def onModuleLoad(self):
		self.htmlElements()
		try:
			HTTPRequest().asyncGet("http://localhost:8081/a/default/json/themes", 
					HTTPAsyncRequestHandler(texts=self.themesRequestTexts, messagePanel=self.messagePanel(), 
									callbacks=self.themesRequestCallbacks))	
		except Exception, ex:
			self.htmlElements()[1][1].setHTML(str(ex))

	_htmlElements = None
	def htmlElements(self, addList = None):
		if not self._htmlElements:
			h = HTML("<h1>Hello from %s</h1>" % location.getHref(), StyleName='font-s07em')
			p = HorizontalPanel(HTML('Valid/tested combinations'))
			grid = Grid(2,2)
			grid.setHTML(0, 0, "app")
			grid.setHTML(0, 1, "themes")
			grid.setHTML(1, 0, "a")
			grid.setHTML(1, 1, "0 - 1 - ff0000 - cms - pypress - wordpress")
			self._htmlElements = [['h', h], ['p', p], ['grid', grid]]	
			for i in range(len(self._htmlElements)):
 				RootPanel().add(self._htmlElements[i][1])
		if addList:
			self._htmlElements+=addList
			for i in range(len(self._htmlElements)):
 				RootPanel().add(addList[i][1])

		return self._htmlElements

	def addThemesPanel(self, themes):
		htmlElements(addList=[['tp', self.themesPanel(themes)]])
		Window.alert('line:108 - %s' % str(self.htmlElements()))

	def themesPanel(self, themes=None):
		Window.alert('line:111')
		themes = None
		if not themes: themes=['0','1', 'cms', 'pypress']

		vPanel = VerticalPanel()
		for i in range(len(themes)):
			"""
			a_n = location.getPathName().split('/')[1]
			lambda1 = lambda x: w_l.pathname.replace('/'+a_n+'/', '/'+x+'/')+'?theme='+x
        	lambda2 = lambda x: w_l.pathname.replace('/'+a_n+'/', '/a/')+'?theme='+x
			href = {
				'cms' : lambda1, 
				'pypress' : lambda1,
				'o' : lambda2, 
				'1' : lambda2 
			}.get(themes[i], lambda2)(themes[i])
			"""

			a=Button('theme '+themes[i], 
					lambda x: location.setSearchDict({'theme': x.getID()}), 
					StyleName='link')
			a.setID(themes[i])
			vPanel.add(a)
	
		return vPanel

if __name__ == '__main__':
	pyjd.setup("public/Index.html")
	app = Index()
	app.onModuleLoad()
	pyjd.run()



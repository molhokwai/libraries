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

import _locationObj

"""
############ SAMPLE ##############

!!!!!!!!!!	WARNING	!!!!!!!!!!!!!!
This may not be a working version.
For a working version if necessary, code has to be downloaded from a working a.pages.themes app version
running on gae
"""
class Index():
	themesRequestTexts = None
	themesRequestCallbacks = None

	def __init__(self):
		"""
		@vars
			self.themesRequestTexts : used in async server (ajax) requests
				see HTTPAsyncRequestHandler in "pyjamas/molhokwai.net/library" folder
			self.themesRequestCallbacks : idem 
				
		"""
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
		"""
		@vars
			
			HTTPRequest().asyncGet(...
				see HTTPAsyncRequestHandler in "pyjamas/molhokwai.net/library" folder
		"""
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

	def themesPanel(self, themes=None):
		themes = None
		if not themes: themes=['0','1', 'cms', 'pypress']

		vPanel = VerticalPanel()
		for i in range(len(themes)):
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



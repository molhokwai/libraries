import pyjd # this is dummy in pyjs.
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Hyperlink import Hyperlink
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Grid import Grid
from pyjamas.ui.Label import Label
from pyjamas.ui.TextArea import TextArea
from pyjamas.HTTPRequest import HTTPRequest
from pyjamas import Window
import pygwt
from __pyjamas__ import JS

location = Window.getLocation()

from CreationTimeFrame.Mayan import Mayan
from CreationTimeFrame.Cycle import Cycle
from CreationTimeFrame.Mind import Mind

class Index():
	"""
	Index page
	"""
	def __init__(self):
		"""
		@vars
							
		"""
		_Mayan = Mayan
		_Cycle = Cycle
		_Mind = Mind
		JS(
			"""
				Mayan = _Mayan;
				Cycle = _Cycle;
				Mind = _Mind;
			"""
		)
		pass

	def messagePanel(self):
		return self.htmlElements()[2][1]

	def textArea(self):
		return self.htmlElements()[3][1]

	def submitButton(self):
		return self.htmlElements()[4][1]


	def onModuleLoad(self):
		"""
		@vars
			
			HTTPRequest().asyncGet(...
				see HTTPAsyncRequestHandler in "pyjamas/molhokwai.net/library" folder
		"""
		self.htmlElements()
		try:
			pass
		except Exception, ex:
			self.htmlElements()[1][1].setHTML(str(ex))


	_htmlElements = None
	def htmlElements(self, addList = None):
		if not self._htmlElements:
			h = HTML("<h1>Hello from %s</h1>" % location.getHref(), StyleName='font-s07em')
			p = HTML('<p>Enter vaild CreationTimeFrame code and submit...</p>')
			m = HorizontalPanel()
			t = TextArea(StyleName='page-textarea')
			b=Button('submit', self, StyleName='link')
			b.setID('submitButton')

			self._htmlElements = [['h', h], ['p', p], ['m', m], ['t', t], ['b', b]]
			for i in range(len(self._htmlElements)):
 				RootPanel().add(self._htmlElements[i][1])

		if addList:
			self._htmlElements+=addList
			for i in range(len(self._htmlElements)):
 				RootPanel().add(addList[i][1])

		return self._htmlElements


	def onClick(self, sender):
		if (sender.getID()==self.submitButton().getID()):
			js = self.textArea().getText()
			JS(
				"""
					eval(js);
				"""
			)



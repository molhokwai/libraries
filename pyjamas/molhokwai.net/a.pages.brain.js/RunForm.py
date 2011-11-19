import pyjd # this is dummy in pyjs.
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.FormPanel import FormPanel
from pyjamas.ui.Hyperlink import Hyperlink
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Grid import Grid
from pyjamas.ui.Label import Label
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.TextBox import TextBox
from pyjamas.HTTPRequest import HTTPRequest
from pyjamas import Window
import pygwt

from library.LocationObj import LocationObj
from library.Widget import Widget as LWidget
location = LocationObj.get()


class RunForm():
	ADD_FIELD_BUTTON = 'addFieldButton'

	"""
	Index page
	"""
	def __init__(self):
		"""
		@vars
							
		"""
		pass

	def getWidgetObj(self, w=TextBox()):
		return {'w' : w, 'kwargs' : {'name' : 'data_%i'%self._fieldIndex, 
									'id' : 'data_%i'%self._fieldIndex, 'StyleName' : 'nr'}}

	_fieldIndex = 0
	def addWidgetObj(self):
		_fieldIndex += 1
		wO = self.getWidgetObj()
		self.formPanel().add(wO)	

	def fieldPanel(self, widgets):
		h = HorizontalPanel()
		h.setStyleName('field')
		l = Label()
		for i in range(len(widgets)):
			if i==0:
				if 'name' in widgets[0]['kwargs']:
					l = Label(widgets[0]['kwargs']['name'])
				h.add(l)
			_i = i
			if isinstance(widgets[i], int): 
				_i = widgets[i]
			w = LWidget.make(widgets[_i]['w'], **widgets[_i]['kwargs'])
			h.add(w)
		return h 

	def formPanel(self):
		return self._htmlElements[3][1]

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
			h = HTML("<h1>Run data</h1>", StyleName='font-s07em')
			p = HTML('<p>Enter <em>weighed</em> data to get information, through the neural network...</p>')
			b=Button('addField', self, StyleName='link')
			b.setID(ADD_FIELD_BUTTON)

			f = FormPanel()
			_f = self.fieldPanel([self.getWidgetObj(),0,0])
			f.add(_f)
			"""
			t = TextArea(StyleName='page-textarea')
			s=Button('submit', self, StyleName='link')
			s.setID('submitButton')
			"""
			self._htmlElements = [['h', h], ['p', p], ['b', b], ['f', f]]
			for i in range(len(self._htmlElements)):
 				RootPanel().add(self._htmlElements[i][1])

		if addList:
			self._htmlElements+=addList
			for i in range(len(self._htmlElements)):
 				RootPanel().add(addList[i][1])

		return self._htmlElements

	def onClick(self, sender):
		if (sender.getID()==self.ADD_FIELD_BUTTON):
			self.addWidgetObj()
		


if __name__ == '__main__':
    pyjd.setup("public/RunForm.html")
    app = RunForm()
    app.onModuleLoad()
    pyjd.run()



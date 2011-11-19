
import pyjd # this is dummy in pyjs.
from pyjamas import Window
from pyjamas.ui.Widget import Widget
from pyjamas.ui.TextBox import TextBox
import pygwt

class Widget(Widget):
	@staticmethod    
	def make(w, **kwargs):
		for kw in kwargs:
			if kw.lower()=='name': w.setName(kwargs[kw])
			if kw.lower()=='id': w.setID(kwargs[kw])
			if kw.lower() in ['class', 'classname', 'stylename']:
				w.setStyleName(kwargs[kw])
			if kw.lower() in ['listeners']:
				for k in kwargs[kw]:
					aLs = 'add%sListener' % str(k).lower().capitalize()
					if aLs in w.__dict__:
						f = eval('w.%s' % aLs)
						f(kwargs[kw][k])
		return w


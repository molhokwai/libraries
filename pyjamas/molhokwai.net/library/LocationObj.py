import pyjd # this is dummy in pyjs.
from pyjamas import Window
import pygwt

class LocationObj:
	@staticmethod
	def get():
		return Window.getLocation()	

	def locationObjPanel():
		"""Sample"""
		vpl = VerticalPanel();
		vpl.add(HTML(location.getPageHref(self)))
		vpl.add(HTML(location.getSearchVar('theme')))
		vpl.add(HTML(location.getSearch(self)))
		return vpl


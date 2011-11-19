import pyjd # this is dummy in pyjs.
from pyjamas import Window
import pygwt
from __pyjamas__ import JS

class Base:
	args = None 

	def __init__(self, args):
		"""
            @params:
				args: dictionary of arguments (not *args or *kwargs for javascript translation) 
		"""
		self.args = args

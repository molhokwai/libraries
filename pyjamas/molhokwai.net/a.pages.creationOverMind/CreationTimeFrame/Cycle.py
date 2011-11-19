import datetime
import math

import pyjd # this is dummy in pyjs.
from pyjamas import Window
import pygwt
from __pyjamas__ import JS

from Base import Base

class ReferencePoint:
	CYCLE='Universal'
	START_DATE=datetime.datetime(2011,3,9)
	CREATION_SPEED=float(1/1728000)
	"""fps: frames per seconds"""
	

class Cycle(Base):
	referencePoint=ReferencePoint()

	_jumps = None
	def jumps(self):
		"""
			@vars
				Dates allowed in one of these two formats:
					[YYYY,MM,dd]
					[YYYY,MM,dd,hh,mm,ss]
		"""
		if not self._jumps:
			gd = self.args.gregorianDate
			if len(gd)==3: gd+=[0,0,0]
			gregorianDate = datetime.datetime(gd[0],gd[1],gd[2],
												gd[3],gd[4],gd[5])
			self._jumps = self.jumpsFromGregorian(gregorianDate)
		return self._jumps

	def jumpsFromGregorian(self, gregorianDate):
		"""
    	-   Obtention of Number of seconds ahead or before reference point
    	-   Calculation*:
        	-   Calculation of _Number of Cycle Jumps_ from reference point in number of seconds
		"""
		Window.alert(gregorianDate)
		gregorianDate = datetime.datetime(gregorianDate)
		Window.alert(isinstance(gregorianDate, datetime.datetime))
		Window.alert(gregorianDate)
		jumps = 0
		diff = datetime.datetime(gregorianDate) - datetime.datetime(self.referencePoint.START_DATE)
		Window.alert(diff.days)
		f = diff>0

		diff = math.abs(diff)
		while diff>0:
			jumps = jumps+1
			Window.alert(float(self.referencePoint.CREATION_SPEED))
			if f:
				"""original formula: (1*13/(self.referencePoint.SPEED*13^jumps))"""
				diff = diff - (1/(self.referencePoint.CREATION_SPEED*13^(jumps-1)))
			else:
				"""original formula: (1*13/(self.referencePoint.SPEED/13^jumps))"""
				diff = diff - (1/(self.referencePoint.CREATION_SPEED/13^(jumps+1)))

		return jumps


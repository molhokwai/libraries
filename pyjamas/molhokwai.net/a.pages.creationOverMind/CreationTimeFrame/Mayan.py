from Base import Base
from Cycle import Cycle

class Mayan(Base):
	
	_cycle = None
	def cycle(self):
		if not self._cycle:
			"""
			args = {'caller' : self}
			for k in self.args:
				args[k] = self.args
			"""
			self._cycle = Cycle(self.args)
			# self._cycle.args = [self]

		return self._cycle

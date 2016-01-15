# coding=utf-8
from pyleus.storm import Spout


class UserLocationSpout(Spout):
	def next_tuple(self, tup):
		self.emit(tup)


if __name__ == '__main__':
    UserLocationSpout().run()

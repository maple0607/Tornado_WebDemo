#coding=utf8

class CacheData:
	def __init__(self, cache_size = 200):
		self.__cache_size = cache_size
		self._cache = []
		self.__writers = set()
	def addWriter(self, writer):
		self.__writers.add(writer)

	def removeWriter(self, writer):
		self.__writers.remove(writer)

	def msgtocache(self, chat):
		self._cache.append(chat)
		if len(self._cache) > self.__cache_size:
			self._cache = self._cache[-self.__cache_size:]
		for writer in self.__writers:
			try:
				writer.write_message(chat)
			except:
				logging.error("Error sending message", exc_info=True)

	def getCache(self):
		return self._cache
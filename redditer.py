from PIL import Image
import requests
from io import StringIO, BytesIO

class Reddit:
	def __init__(self, subreddits):
		self.subreddits = subreddits
		self.size = (1080,1080)

	def requestRandom(self):
		pass

	def requestBuffer(self, link):
		r = requests.get(link)#"https://i.redd.it/vx275wl93b551.jpg")
		return r.content

	def resizeBuffer(self, Buffer):
		img = Image.open(BytesIO(Buffer))
		img = img.resize(self.size, Image.ANTIALIAS)
		return img
		# img.show()



Red = Reddit("idk")
buffer = Red.requestBuffer()
Red.resizeBuffer(buffer)
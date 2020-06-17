from io import StringIO, BytesIO
from PIL import Image
import instaWrapper
import requests

class BOT:
	def __init__(self, subreddits, auth):
		self.subreddits = subreddits
		self.API = instaWrapper.InstagramBot(auth)
		self.size = (1080,1080)

	def requestRandom(self):
		return "https://i.redd.it/vx275wl93b551.jpg"

	def requestBuffer(self, link):
		r = requests.get(link)
		return r.content

	def resizeBuffer(self, Buffer):
		img = Image.open(BytesIO(Buffer))
		img = img.resize(self.size, Image.ANTIALIAS)
		return img

	def post(self, buffer, caption):
		pass


with open("config.json") as f:
	config = f.read()
Red = BOT([], config)
buffer = Red.requestBuffer(Red.requestRandom())
Red.resizeBuffer(buffer)
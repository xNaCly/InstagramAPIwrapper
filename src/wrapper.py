import requests
import json
from time import sleep as s
import urllib.parse
import time


default = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
		"Accept": "*/*",
		"Accept-Language": "en-US;q=0.7,en;q=0.3",
		"Accept-Encoding": "gzip, deflate, br",
		"Content-Type": "application/x-www-form-urlencoded",
		"X-Requested-With": "XMLHttpRequest",
		"Content-Length": "0",
		"Origin": "https://www.instagram.com",
	}

class Instagram:
	"""
	reverse engineered instagram wrapper

	see docs here: [DOCS](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs)
	"""
	def __init__(self, auth: dict):
		if not auth:
			raise ValueError("No auth given")
		# self.auther = json.loads(auth)
		self.auth = {
			"X-CSRFToken": auth["X-CSRFToken"],
			"Cookie": auth["Cookie"],
			"X-Instagram-AJAX": auth["X-Instagram-AJAX"]
		}
		self.headers = {}
		self.headers.update(default)
		self.headers.update(self.auth)


	def	getPost(self, link):
		"""
		converts share link to internal id

		throws error if not available/found
		"""
		Host = link.split("?")[0] + "?__a=1"
		r = requests.get(Host, headers=self.headers)
		if r.status_code != 200:
			raise ValueError("Post isnt availabe")
		rr = json.loads(r.text)
		rr = rr["graphql"]["shortcode_media"]
		u = rr["owner"]
		postObject = {
			'id': rr["id"],
			'type': rr["__typename"],
			'url': link,
			'caption': rr["edge_media_to_caption"]["edges"][0]["node"]["text"],
			'media_url': rr["display_url"],
			'dimensions': rr["dimensions"],
			'owner': {
				'user':{
					'username': u["username"],
					'full_name': u["full_name"],
					'id': u["id"],		
				}
			}
		}
		return postObject

	def search(self, user):
		"""
		searches for given user

		returns array of users sorted by relevance

		throws error if none are available/found
		"""
		Host = default["Origin"] + "/web/search/topsearch/?query=" + user
		r = requests.get(Host, headers=self.headers)
		if r.status_code != 200:
			raise ValueError("Query isnt availabe")
		rr = json.loads(r.text)
		if len(rr["users"]) == 0:
			raise ValueError("Query isnt availabe")
		userarray = []
		for x in rr["users"]:
			userarray.append(x["user"]["username"])
		return userarray

	def getUser(self, user):
		"""
		returns info about the given user

		throws error if not found/not available
		"""
		Host = default["Origin"] + "/"+ user + "/?__a=1"
		r = requests.get(Host, headers=self.headers)
		if len(r.text) < 10:
			raise ValueError("User isnt availabe")
		rr = json.loads(r.text)
		u = rr["graphql"]["user"]
		userobject = {
			'user':{
				'username': u["username"],
				'full_name': u["full_name"],
				'id': u["id"],
				'bio': u["biography"],
				'url': f'https://www.instagram.com/{u["username"]}/',
				'profile_pic': u["profile_pic_url_hd"]
			},
			'followers': u["edge_followed_by"]["count"],
			'following': u["edge_follow"]["count"],
			'relationship':{
				'following': u["followed_by_viewer"],
				'blocked': u["blocked_by_viewer"],
				'restricted': u["restricted_by_viewer"],
				'mutual_follows': u["edge_mutual_followed_by"]["count"]
			},
			'about':{
				'private':u["is_private"],
				'business':u["is_business_account"],
				'joinend_recently':u["is_joined_recently"],
				'verified': u["is_verified"]
			}
		}
		return userobject


	def likePost(self, id):
		"""
		likes post with given id
		"""
		Host =  default["Origin"] +  f"/web/likes/{id}/like/"
		r = requests.post(Host, headers=self.headers)
		robject = {
			'status': r.status_code,
			'message': r.json()
		}
		return robject
	
	def unlikePost(self, id):
		"""
		removes like from post with given id
		"""
		Host =  default["Origin"] + f"/web/likes/{id}/unlike/"
		r = requests.post(Host, headers=self.headers)
		robject = {
			'status': r.status_code,
			'message': r.json()
		}
		return robject


	def addComment(self, id, comment):
		"""
		comments on post with given id
		"""
		comment = urllib.parse.quote(comment)
		Host = default["Origin"] + f"/web/comments/{id}/add/"
		self.headers["Content-Length"] = str(len(comment))
		payload = f"comment_text={comment}s"
		r = requests.post(Host, data=payload, headers=self.headers)
		robject = {
			'status': r.status_code,
			'message': r.json()
		}
		return robject

	def removeComment(self, postID, commentID):
		"""
		removes a comment on post with given postID & commentID
		"""
		Host = default["Origin"] +f"/web/comments/{postID}/delete/{commentID}/"
		r = requests.post(Host, headers=self.headers)
		robject = {
			'status': r.status_code,
			'message': r.json()
		}
		return robject
	

	def follow(self, username):
		"""
		follows the given user
		"""
		id = self.getUser(username)
		Host = default["Origin"] + "/web/friendships/" + id["user"]["id"] + "/follow/"
		r = requests.post(Host, headers=self.headers)
		try:
			robject = {
				'status': r.status_code,
				'message': r.json()
			}
		except:
			raise ValueError(f"Error - either {username} doesnt exist, or auth is invalid")	
		return robject
	
	def unfollow(self, username):
		"""
		unfollow the given user
		"""
		id = self.getUser(username)
		Host = default["Origin"] + "/web/friendships/" + id["user"]["id"] + "/unfollow/"
		r = requests.post(Host, headers=self.headers)
		try:
			robject = {
				'status': r.status_code,
				'message': r.json()
			}
		except:
			raise ValueError(f"Error - either {username} doesnt exist, or auth is invalid")	
		return robject
	
	def changeSettings(self, settings: dict = {'first_name':'','email':'','username':'','phone_number':'','biography':'','website':''}):
		"""
		change settings
		"""
		form = f"first_name={str(urllib.parse.quote(settings['first_name'])).replace('%20','+')}&email={urllib.parse.quote(settings['email'])}&username={urllib.parse.quote(settings['username'])}&phone_number={urllib.parse.quote(settings['phone_number'])}&biography={str(urllib.parse.quote(settings['biography']).replace('%20','+'))}&external_url={settings['website']}&chaining_enabled=on"
		Host = default["Origin"] + "/accounts/edit"
		r = requests.post(Host, headers=self.headers,data=form)
		try:
			robject = {
				'status': r.status_code,
				'message': r.json()
			}
		except:
			raise ValueError(f"Error - auth is invalid")	
		return robject


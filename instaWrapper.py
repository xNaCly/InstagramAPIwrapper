"""
reverse engineered instagram wrapper

currently supports: `getID, likePost, commentPost, deletePost, User, search`
"""
import requests
import json
from time import sleep as s
import urllib.parse
import time


default = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
		"Accept": "*/*",
		"Accept-Language": "de,en-US;q=0.7,en;q=0.3",
		"Accept-Encoding": "gzip, deflate, br",
		"Content-Type": "application/x-www-form-urlencoded",
		"X-Requested-With": "XMLHttpRequest",
		"Content-Length": "0",
		"Origin": "https://www.instagram.com",
	}

class InstagramBot:
	def __init__(self, auth):
		self.auther = json.loads(auth)
		self.auth = {
		"X-CSRFToken": self.auther["X-CSRFToken"],
		"Cookie": self.auther["Cookie"],
		"X-Instagram-AJAX": self.auther["X-Instagram-AJAX"]
		}
		self.headers = {}
		self.headers.update(default)
		self.headers.update(self.auth)



	def	getID(self, link):
		"""
		converts share link to internal id

		throws error if not available
		"""
		Host = link.split("?")[0] + "?__a=1"
		r = requests.get(Host, headers=self.headers)
		if r.status_code != 200:
			raise ValueError("Post isnt availabe")
		rr = json.loads(r.text)
		return rr["graphql"]["shortcode_media"]["id"]

	def search(self, user):
		"""
		searches for given user

		returns array of users sorted by relevance

		throws error if none are available
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

	def User(self, user):
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


	def likePost(self, id, unlike):
		"""
		likes post with given id
		"""
		ty = "like"
		if  unlike == True:
			ty = "unlike"
		Host =  f"/web/likes/{id}/{ty}/"
		r = requests.post(Host, headers=self.headers)
		robject = {
			'status': r.status_code,
			'message': r.json()
		}
		return robject


	def commentPost(self, id, comment):
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

	def deleteComment(self, postID, commentID):
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
	
	def post(self, image, caption):
		pass

	def follow(self, username):
		id = self.User(username)
		Host = default["Origin"] + "/web/friendships/" + id["user"]["id"] + "/follow/"
		r = requests.post(Host, headers=self.headers)
		robject = {
			'status': r.status_code,
			'message': r.json()
		}
		return robject

	
	# def unfollow(self, username):
	# 	pass

	def post(self, img, caption):
		date = str(time.time())
		Host = default["Origin"] + "/rupload_igphoto/fb_uploader_"+date
		newHeaders = {
			"X-Instagram-Rupload-Params":'{"media_type":1,"upload_id":"'+date+'","upload_media_height":500,"upload_media_width":500}',
			"X-Entity-Name": "fb_uploader_"+date
		}

		newHeaders.update(default)
		newHeaders.update(self.headers)
		newHeaders["Content-Type"] = "image/jpeg"
		r = requests.post(Host, data=img, headers=newHeaders )
		robject = {
			'status': r.status_code,
			'message': r.json()
		}
		return robject

import instaWrapper

config = {
	"X-CSRFToken": "",
	"Cookie": ""
}

# init class with auth
InstaApi = instaWrapper.InstagramBot(config)

# ---------------------------------------------------------

# get internal id for link
InstaApi.getID("https://www.instagram.com/p/CBYRpUnF4Vh/")
"""
2330690413584156001
"""

# search for users
InstaApi.search("Lorum")
"""
[
	'lorumaricat', 
	'lorum', 
	'lorumsa',
	'lightxlloyd',
	'lorumlashes',
	'lo.rum',
	'lorum_shop',
	'remni_koja_rostov_na_dony',
	'lorumalexandre24',
	'lorumrectory',
	'lorumcraft',
	'lo_rumeno',
	'cesar.skantze',
	'nicolaslorum',
	'ballinkillenlorumccc',
	'katjakaizen',
	'lorumannabell941',
	'lorumgrayson3lu',
	'johannlorum',
	'annehelenenielsenlorum',
	'lor.um',
	'lorum_men',
	'lorum_ipsum',
	'valerielorum'
]
"""

# get info about specified username
InstaApi.User("lorum")
"""
{
    "user": {
        "username": "lorum",
        "full_name": "",
        "id": "48742205",
        "bio": "",
        "profile_pic": "https://instagram.fgbb2-2.fna.fbcdn.net/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=instagram.fgbb2-2.fna.fbcdn.net&_nc_ohc=rwWGQ6X4qT4AX_1qa-8&oh=e2dfb5000fdeffb94d2c6f21ba152b6b&oe=5F0FB80F&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2"
    },
    "followers": 2,
    "following": 0,
    "relationship": {
        "following": false,
        "blocked": false,
        "restricted": false,
        "mutual_follows": 0
    },
    "about": {
        "private": false,
        "business": false,
        "joinend_recently": false,
        "verified": false
    }
}
"""

# like/unlike a post
InstaApi.likePost(2330690413584156001, False)
"""
{'status': 200, 'message': '{"status": "ok"}'}
/
{'status': 400, 'message': 'Sorry, this photo has been deleted'}
"""

# comment on a post
InstaApi.commentPost(2330690413584156001, "Cogito ergo sum")
"""
{
    "status": 200,
    "message": {
        "id": "18138683704070412",
        "from": {
            "id": "7632716064",
            "username": "xnacly",
            "full_name": "teo",
            "profile_picture": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/s150x150/94195398_4348654338493989_4951452463078047744_n.jpg?_nc_ht=scontent-ber1-1.cdninstagram.com\\u0026_nc_ohc=u7fYF3h6ZGYAX-SDFaL\\u0026oh=142c85b4db612e2dc94440605ecc0a18\\u0026oe=5F10530B"
        },
        "text": "Cogito ergo sums",
        "created_time": 1592235836,
        "status": "ok"
    }
}
"""

InstaApi.deleteComment(2330690413584156001, 18138683704070412):
"""
{'status': 200, 'message': {'status': 'ok'}}
/
{'status': 400, 'message': {'message': 'You cannot delete this comment', 'status': 'fail'}}
"""
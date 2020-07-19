# getUser

## Args:

-   username [string]

```
fortnite
```

## Return:

-   [UserObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#userobject)

```
{
  "user": {
    "username": "fortnite",
    "full_name": "Fortnite",
    "id": "1192899491",
    "bio": "The official Instagram account for #Fortnite, Battle Royale, Creative, and Save the World.",
    "url": "https://www.instagram.com/fortnite/",
    "profile_pic": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/s320x320/103452576_1135154500184004_1849401560886556420_n.jpg?_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_ohc=6TbvwyNKm4kAX8EfhrW&oh=49e654a628771fa9c73567a8b214e756&oe=5F3F6633"
  },
  "followers": 24640242,
  "following": 8,
  "relationship": {
    "following": True,
    "blocked": False,
    "restricted": False,
    "mutual_follows": 2
  },
  "about": {
    "private": False,
    "business": True,
    "joinend_recently": False,
    "verified": True
  }
}
```

## Code Example:

```python
import wrapper
auth = {
	"X-CSRFToken": "",
	"X-Instagram-AJAX": "",
	"Cookie": ""
}
API = wrapper.Instagram(auth)
print(API.getUser("fortnite"))
```

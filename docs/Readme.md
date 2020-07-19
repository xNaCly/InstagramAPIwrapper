# Docs:

## General Info:
- all methods are well documented [here](https://github.com/xNaCly/InstagramAPIwrapper/blob/master/docs)
- all returnObjects are formated as Python-dicts

## General Terms:

#### StatusObject:

```
{
  "status": 200,
  "message": {
    "status": "ok"
  }
}
```

#### UserObject:

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

#### CommentObject:

```
{
  "status": 200,
  "message": {
    "id": "17897224696526065",
    "from": {
      "id": "",
      "username": "",
      "full_name": "",
      "profile_picture": ""
    },
    "text": "",
    "created_time": 1595162878,
    "status": ""
  }
}
```

#### PostObject:

```
{
  "id": "2330690413584156001",
  "type": "GraphImage",
  "url": "https://www.instagram.com/p/CBYRpUnF4Vh/",
  "caption": "Wacky designs = free publicity \nsource: u/adityapatel149",
  "media_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/103332275_285012022683137_1361234643068352553_n.jpg?_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=105&_nc_ohc=FeDgrXEGCeMAX9TmWCr&oh=aebc4c4063e36a9f22daa7f6e361e7f9&oe=5F3F94EA",
  "dimensions": {
    "height": 1350,
    "width": 1080
  },
  "owner": {
    "user": {
      "username": "zucctheberg",
      "full_name": "Memes that make you go 🐕",
      "id": "5728490480"
    }
  }
}
```

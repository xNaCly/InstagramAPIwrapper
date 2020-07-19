# getPost

## Args:
- link:
```
Example: 
https://www.instagram.com/p/CBYRpUnF4Vh
```

## Return:
- [PostObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#postobject)
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

## Code example:
```
import wrapper
auth = {
	"X-CSRFToken": "",
	"X-Instagram-AJAX": "",
	"Cookie": ""
}
API = wrapper.Instagram(auth)
print(API.getPost("https://www.instagram.com/p/CBYRpUnF4Vh/"))
```
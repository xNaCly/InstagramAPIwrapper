# addComment

## Args:
- postID [str]/[int]
- comment [str]

## Return:
- [commentObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#commentobject) [type]

```python
{
  "status": 200,
  "message": {
    "id": "17930105290396452",
    "from": {
      "id": "7632716064",
      "username": "xnacly",
      "full_name": "teo",
      "profile_picture": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/s150x150/94195398_4348654338493989_4951452463078047744_n.jpg?_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_ohc=g0DFLVQF90YAX_Gqhyn&oh=4e4c94645ff17289a14db209f181a26e&oe=5F3FC90B"
    },
    "text": "funny :smile:s",
    "created_time": 1595178938,
    "status": "ok"
  }

```

## Code example:
```python
import wrapper
auth = {
	"X-CSRFToken": "",
	"X-Instagram-AJAX": "",
	"Cookie": ""
}
API = wrapper.Instagram(auth)
print(API.addComment(2356803465986446994, "funny :smile:"))
```
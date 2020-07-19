# removeComment

## Args:

-   postID [str]/[int]
-   commentID [str]/[int]

## Return:

-   [statusObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#statusobject) [type]

```python
{
  "status": 200,
  "message": {
    "status": "ok"
  }
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
print(API.removeComment(2356803465986446994, 17930105290396452))
```

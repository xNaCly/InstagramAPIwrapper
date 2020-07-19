# unfollow

## Args:

-   username `[str]`

## Return:

- [StatusObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#statusobject) `[object]`

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
print(API.unfollow("fortnite"))
```

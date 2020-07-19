# follow

## Args:
- username [string]

## Return:
- StatusObject [Object]

```python
{
  "status": 200,
  "message": {
    "result": "following",
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
print(API.follow("fortnite"))
```
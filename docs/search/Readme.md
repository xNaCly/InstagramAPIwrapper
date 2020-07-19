# search

## Args:

-   username [string]

```
fortnite
```

## Return:

-   UserArray

```
[
  "fortnite",
  "fortnitede",
  "fortnitees",
  "fortnite.chaptix",
  "fortnite_itemshop_daily",
  "kcin_fortnite.top100",
  "fortnitesgift",
  "fortniteoficjalnie",
  "fortnitefr_officiel",
  "fortniteita",
  "dailyfortshop",
  "fortniteapokalypse",
  "fortnitebr",
  "fortnite.game",
  "itemshoproyale",
  "fortnitecosmetics",
  "fortnites",
  "fortnitebrainiac",
  "fortnitescreative",
  "fortleaks",
  "leakskin",
  "fortniteitemshop",
  "fortnite.empire",
  ...
]
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
print(API.search("fortnite"))
```

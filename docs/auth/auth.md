# How to authenticate and how to get the authentication:

### How to AUTH:

-   Three values/tokens needed for the authentication:

```
  	1. X-CSRFToken
	2. X-Instagram-AJAX
  	3. Cookie
```

### How to get these Values:

-   each of these values/tokens can be found with inspecting networkrequests while being logged in into Instragram.

```
	1. open dev tools (F12)
	2. unfollow someone
	3. look out for a request named: https://www.instagram.com/web/friendships/['numbers']/unfollow/
	4. go to request headers
	5. and search for X-CSRFToken, X-Instagram-AJAX and Cookie
```

<img scr="https://cdn.discordapp.com/attachments/568847750226116609/734382276376395806/Untitled-2.png">

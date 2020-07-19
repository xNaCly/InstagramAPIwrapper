# Docs:

## Setup
- to get started please take a look [here](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs/auth)


## Features:
| Method        | return        | args             |
|---------------|---------------|------------------|
| [getPost](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs/getPost)        | [PostObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#postobject)           | link             |
| [likePost](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs/likePost)      | [StatusObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#statusobject)  | PostID           |
| [unlikePost](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs/unlikePost)    | [StatusObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#statusobject)  | PostID           |
| [addComment](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs/addComment)    | [CommentObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#commentobject) | PostID, comment   |
| [removeComment](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs/addComment) | [StatusObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#statusobject)  | PostID,CommentID |
| [follow](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs/follow)        | [StatusObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#statusobject)  | Username         |
| [unfollow](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs/unfollow)      | [StatusObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#statusobject)  | Username         |
| [getUser](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs/getUser)          | [UserObject](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs#userobject)    | Username         |
| [search](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs/search)        | UserArray     | string           |

## General Info:

-   all methods are well documented [here](https://github.com/xNaCly/InstagramAPIwrapper/blob/master/docs)
-   all methods require the usage of basic [auth](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs/auth)
-   all returnObjects are formated as [Python-dicts](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## General Terms:

#### StatusObject:

```python
{
  "status": int (httpstatuscode),
  "message": {
    "status": str
  }
}
```

#### UserObject:

```python
{
  "user": {
    "username": str,
    "full_name": str,
    "id": int,
    "bio": str,
    "url": str,
    "profile_pic": str
  },
  "followers": int,
  "following": int,
  "relationship": {
    "following": bool,
    "blocked": bool,
    "restricted": bool,
    "mutual_follows": int
  },
  "about": {
    "private": bool,
    "business": bool,
    "joinend_recently": bool,
    "verified": bool
  }
}
```

#### CommentObject:

```python
{
  "status": int (httpstatuscode),
  "message": {
    "id": str,
    "from": {
      "id": str,
      "username": str,
      "full_name": str,
      "profile_picture": str
    },
    "text": str,
    "created_time": int (timestamp),
    "status": str
  }
}
```

#### PostObject:

```python
{
  "id": str,
  "type": str,
  "url": str,
  "caption": str,
  "media_url": str,
  "dimensions": {
    "height": int,
    "width": int
  },
  "owner": {
    "user": {
      "username": str,
      "full_name": str,
      "id": str
    }
  }
}
```

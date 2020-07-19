# Docs:

## General Info:

-   all methods are well documented [here](https://github.com/xNaCly/InstagramAPIwrapper/blob/master/docs)
-   all returnObjects are formated as Python-dicts

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

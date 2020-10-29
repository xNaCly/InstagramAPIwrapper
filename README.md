<p align="center">
    <img style="border-radius: 100px" width="128" height="128" src="https://avatars0.githubusercontent.com/u/47723417?s=460&amp;u=10c488f1c4e0644b839df15ecefbfef2a9869305&amp;v=4">
</p>

# Please refrain from usage on your private instagram account, 
# Using this wrapper will propably flag your account !

### Private Instagram API wrapper
- reverse engineered internal instagram api wrapper

# [Docs](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs)

# Features:
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


# Planned Features:
- [ ] add Login with Username & Password (not possible with api due to encryption)
- [x] add Docs
- [ ] add uploading posts (from url?/from file, with caption)
- [ ] add usersettings (change profilepic/change username/other settings)
- [ ] add comments to PostObject (comments from Post to PostObject)
- [ ] make a video showcasing all methods

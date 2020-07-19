<p align="center">
    <img style="border-radius: 100px" width="128" height="128" src="https://cdn.discordapp.com/avatars/417699816836169728/8ea8764772217e66ce7b7f9c3dd1561e.png?size=2048">
</p>

### Private Instagram API wrapper
- reverse engineered internal instagram api wrapper

# Features:
| Method        | return        | args             |
|---------------|---------------|------------------|
| getID         | ID            | link             |
| likePost      | StatusObject  | PostID           |
| unlikePost    | StatusObject  | PostID           |
| addComment    | CommentObject | PostID, string   |
| deleteComment | StatusObject  | PostID,CommentID |
| follow        | StatusObject  | Username         |
| unfollow      | StatusObject  | Username         |
| user          | UserObject    | Username         |
| search        | UserArray     | string           |

# [Docs](https://github.com/xNaCly/InstagramAPIwrapper/tree/master/docs)

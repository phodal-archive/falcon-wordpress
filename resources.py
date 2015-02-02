import json

import falcon

from blog_models import WpPosts, WpUsers, WpComments


class PostsResource():
    def __init__(self):
        pass

    @staticmethod
    def on_get(req, resp, post_id):
        post = WpPosts.get(WpPosts.id == post_id)
        user = WpUsers.get(WpUsers.id == post.post_author)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({"post_content": post.post_content,
                                "author": user.display_name})


class AllPostsResource():
    def __init__(self):
        pass

    @staticmethod
    def on_get(req, resp):
        store = {}
        offset = req.get_param('offset', store=store)
        result = []
        blog_posts = WpPosts.select().where(
            (WpPosts.post_status == "publish") &
            (WpPosts.post_type == "post")
        ).offset(offset).limit(10)
        for post in blog_posts:
            user = WpUsers.get(WpUsers.id == post.post_author)
            result.append({
                "author": user.display_name,
                "id": post.id,
                "comment": post.comment_count,
                "title": post.post_title,
                "posts": post.post_content[:140]
            })

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(result)


class CommentsResource():
    def __init__(self):
        pass

    @staticmethod
    def on_get(req, resp, comment_id):
        comment = WpComments.get(WpComments.comment == comment_id)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({"comment_author": comment.comment_author,
                                "comment_content": comment.comment_content})


class PostsCommentsResource():
    def __init__(self):
        pass

    @staticmethod
    def on_get(req, resp, post_id):
        result = []
        comments = WpComments.select().where(WpComments.comment_post == post_id)
        for comment in comments:
            result.append({
                "comment_author": comment.comment_author,
                "comment_content": comment.comment_content
            })
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(result)
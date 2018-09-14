from graphene import ObjectType, String, Boolean, ID, Field, Int, List


class Source_Resolution(ObjectType):
    height = Int()
    url = String()
    width = Int()


class Images(ObjectType):
    id = String()
    resolutions = List(Source_Resolution)
    source = Field(Source_Resolution)
    # variants = Field(variants)


class Preview(ObjectType):
    enabled = Boolean()
    images = List(Images)


class Post(ObjectType):
    author = String()
    author_fullname = String()
    can_mod_post = Boolean()
    content_categories = List(String)
    contest_mode = Boolean()
    created_utc = Int()
    domain = String()
    full_link = String()
    gilded = Int()
    id = ID()
    is_crosspostable = Boolean()
    is_meta = Boolean()
    is_reddit_media_domain = Boolean()
    is_self = Boolean()
    is_video = Boolean()
    link_flair_background_color = String()
    link_flair_text_color = String()
    link_flair_type = String()
    locked = Boolean()
    media_only = Boolean()
    no_follow = Boolean()
    num_comments = Int()
    num_crossposts = Int()
    over_18 = Boolean()
    parent_whitelist_status = String()
    permalink = String()
    pinned = Boolean()
    post_hint = String()
    preview = Field(Preview)
    pwls = Int()
    retrieved_on = Int()
    score = Int()
    selftext = String()
    send_replies = Boolean()
    spoiler = Boolean()
    stickied = Boolean()
    subreddit = String()
    subreddit_id = ID()
    subreddit_subscribers = Int()
    subreddit_type = String()
    thumbnail = String()
    thumbnail_height: Int()
    thumbnail_width: Int()
    title = String()
    url = String()
    whitelist_status = String()
    wls = Int()
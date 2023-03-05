# 1 - Import the need modules
import pytumblr
import datetime
import config
# import os

# 2 - Add important infomation
client = config.client
blogName = "hellobot2023"

# 3 - Set the message and hashtag
message = "Hello Tumblr"
hashtag = "#HelloTumblr"

# 4 - Set the post date and time
now = datetime.datetime.now()
post_date = now + datetime.timedelta(days=1)
post_time = datetime.time(hour=12, minute=0)

# 5 - Combine the post date and time
post_datetime = datetime.datetime.combine(post_date, post_time)

# 6 - Create the post
post = {
    'type': 'text',
    'title': message,
    'body': message + ' ' + hashtag,
    'tags': ['HelloTumblr'],
    'publish_on': post_datetime.strftime('%Y-%m-%d %H:%M:%S GMT')
}

# 7 - Post the message

#config.client.create_text('hellobot2023', body='Hello')
client.create_quote('hellobot2023', state="draft", quote="I am the Walrus", source="Ringo")

# 1 - Import the need modules
import pytumblr
import datetime
import config
import os

# 2 - Add important infomation
client = os.environ['client']

# 3 - Set the message and hashtag
message = "Hello Tumblr"
hashtag = "#HelloTumblr"

# 4 - Set the post date and time
now = datetime.datetime.now()
post_date = now + datetime.timedelta(days=1)
post_time = datetime.time(hour=12, minute=0)
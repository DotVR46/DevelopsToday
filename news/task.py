import schedule
import time

from news.models import News


def clean_upvote():
    News.objects.all().update(upvote=0)


schedule.every().day.at("00:00").do(clean_upvote)

while True:
    schedule.run_pending()
    time.sleep(1)

import requests
from django.conf import settings


def send_to_telegram(news):
    caption = f"""
 {news.title}

 {news.category.name}

{news.content[:500]}...

#Yangilik
"""

    if news.image:
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendPhoto"

        with open(news.image.path, "rb") as photo:
            files = {
                "photo": photo
            }

            data = {
                "chat_id": settings.TELEGRAM_CHANNEL,
                "caption": caption,
            }

            requests.post(url, data=data, files=files)

    else:
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"

        data = {
            "chat_id": settings.TELEGRAM_CHANNEL,
            "text": caption,
        }

        requests.post(url, data=data)
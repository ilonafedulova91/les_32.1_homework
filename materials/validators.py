from urllib.parse import urlparse

from rest_framework.exceptions import ValidationError


def validate_youtube_url(value):
    parsed_url = urlparse(value)
    domain = parsed_url.netloc.lower()

    allowed_domains = {
        "youtube.com",
        "www.youtube.com",
    }

    if domain not in allowed_domains:
        raise ValidationError("Можно использовать только ссылки на YouTube.")

    return value

# https://kgu0724.tistory.com/99 참고

from django.urls.converters import StringConverter

class HangulSlugConverter(StringConverter):
    regex = "[-\w]"
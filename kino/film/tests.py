import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Film


class FilmModelTests(TestCase):

    def test_was_published_recently_with_future_task(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_add_film = Film(add_date=time)
        self.assertIs(future_add_film.was_published_recently(), False)


    def test_was_published_recently_with_old_question(self):

        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_add_film = Film(add_date=time)
        self.assertIs(old_add_film.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):

        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_add_film = Film(add_date=time)
        self.assertIs(recent_add_film.was_published_recently(), True)

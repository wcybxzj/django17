# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'

import datetime
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from polls.models import Question


class QuesitonMethodTests(TestCase):
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), True)
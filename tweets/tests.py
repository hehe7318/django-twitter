from testing.testcases import TestCase
from datetime import timedelta
from utils.time_helpers import utc_now


class TweetTests(TestCase):
    def setUp(self):
        self.xuanqi = self.create_user('xuanqi')
        self.tweet = self.create_tweet(self.xuanqi, content='Hello~I am Xuanqi')

    def test_hours_to_now(self):
        self.tweet.created_at = utc_now() - timedelta(hours=10)
        self.tweet.save()
        self.assertEqual(self.tweet.hours_to_now, 10)

    def test_like_set(self):
        self.create_like(self.xuanqi, self.tweet)
        self.assertEqual(self.tweet.like_set.count(), 1)

        self.create_like(self.xuanqi, self.tweet)
        self.assertEqual(self.tweet.like_set.count(), 1)

        he = self.create_user('he')
        self.create_like(he, self.tweet)
        self.assertEqual(self.tweet.like_set.count(), 2)

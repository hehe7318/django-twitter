from testing.testcases import TestCase


class CommentModelTests(TestCase):

    def setUp(self):
        self.xuanqi = self.create_user('xuanqi')
        self.tweet = self.create_tweet(self.xuanqi)
        self.comment = self.create_comment(self.xuanqi, self.tweet)

    def test_comment(self):
        self.assertNotEqual(self.comment.__str__(), None)

    def test_like_set(self):
        self.create_like(self.xuanqi, self.comment)
        self.assertEqual(self.comment.like_set.count(), 1)

        self.create_like(self.xuanqi, self.comment)
        self.assertEqual(self.comment.like_set.count(), 1)

        he = self.create_user('he')
        self.create_like(he, self.comment)
        self.assertEqual(self.comment.like_set.count(), 2)

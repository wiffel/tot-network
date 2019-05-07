from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from faker import Faker

from totaliatarian_network.posts.test.factories import PostFactory
from totaliatarian_network.users.test.factories import UserFactory


fake = Faker()

class TestPostsViews(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.actor = UserFactory()
        cls.public_post = PostFactory()
        cls.private_post = PostFactory(private=True)

        cls.url_post_list = reverse('post-list')
    
    def get_posts_list(self, actor=None):
        """
        Shortcut to get posts list as actor or as anonymous (if actor == None).
        """
        self.client.force_authenticate(self.actor)
        return self.client.get(self.url_post_list)
    
    def post_in_response(self, post, response):
        """
        Check if the post with given text is in the response
        
        Arguments:
            post {django.db.Model} -- posts.models.Post object
            response {requests.Response} -- response object
        """
        post_in_response=(post.text in [post['text'] for post in response.data['results']])
        return post_in_response

    def test_user_can_create_post(self):
        self.client.force_authenticate(self.actor)
        request_data = {
            'text': fake.sentence(),
        }
        self.client.post(self.url_post_list, data=request_data)
        actors_post = self.actor.post_set.first()
        self.assertEqual(actors_post.text, request_data['text'])

    def test_user_can_read_other_posts(self):
        response = self.get_posts_list(self.actor)
        assert self.post_in_response(self.public_post, response)
    
    def test_user_can_read_private_post(self):
        response = self.get_posts_list(self.actor)
        assert self.post_in_response(self.private_post, response)

    def test_anonymous_user_can_not_read_private_posts(self):
        """
        Test that non-authenticated user can not read private posts
        """
        response = self.get_posts_list(actor=None)
        assert self.post_in_response(self.private_post, response)

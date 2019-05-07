import os.path
import time

from django.conf import settings
from faker import Faker
from django.test.utils import patch_logger
from rest_framework.test import APITestCase, APIRequestFactory
from requests import Response

from totaliatarian_network.users.middleware import TrackAccessMiddleware

fake = Faker()


class TestTrackUserMiddleware(APITestCase):

    
    @classmethod
    def setUpTestData(cls):
        cls.test_ip=fake.ipv4_private()
        cls.request = APIRequestFactory().get('/', REMOTE_ADDR=cls.test_ip)

    def test_middleware_saves_log(self):
        with patch_logger('access', 'debug') as log_messages:
            # check ip was logged
            TrackAccessMiddleware(lambda x: x)(self.request)
            self.assertIn(self.test_ip, log_messages)

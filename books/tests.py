from django.test import TestCase
from django.http import HttpResponse
import os
from .views import hello
# from django.test import Client

# Create your tests here.
class InitialBooksTests(TestCase):

    # c = Client()
    
    def test_assertion(self):
        self.assertTrue(True)

    def test_hello_world(self):
        """
        Hello World of Django Testing
        """
        # self.assertTrue(True)
        result = hello(None)
        try:
            env = os.environ['APPLICATION_ENVIRONMENT'] or "testing"
        except KeyError:
            env = "review_app"

        # print("actual", result.content)
        expected = '<h2>Hello {}</h2>'.format(env)
        
        # the request.content is encoded as a byte array, must use
        # encode to match
        expected = expected.encode('UTF-8')
        
        # print("expected: ", expected)
        self.assertEqual(result.content, expected)
        
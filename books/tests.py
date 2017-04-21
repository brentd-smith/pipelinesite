from django.test import TestCase
from django.http import HttpResponse
import os
from .views import hello
from django.test import Client

# Create your tests here.
class InitialBooksTests(TestCase):


    """
    NOTE: this demonstrates using the django.test.Client object to simulate
    actual GET or POST requests to the django server.
    """
    def test_hello_with_client(self):
        c = Client(HTTP_USER_AGENT='Mozilla/5.0')
        r = c.get('/hello/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.content, "<h2>Hello review_app</h2>".encode('UTF-8'))
    
    
    def test_assertion(self):
        self.assertTrue(True)

    # This simply calls the view as a python method...
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
        
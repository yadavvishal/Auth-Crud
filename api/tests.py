from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Post

class PostAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='###', password='###')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create a sample post
        self.post = Post.objects.create(title="Test Post", content="Test Content")

    def test_create_post(self):
        data = {"title": "New Post", "content": "New Content"}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, 201)

    def test_read_posts(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_post(self):
        data = {"title": "Updated Post", "content": "Updated Content"}
        response = self.client.put(f'/api/posts/{self.post.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Updated Post")

    def test_delete_post(self):
        response = self.client.delete(f'/api/posts/{self.post.id}/')
        self.assertEqual(response.status_code, 204)

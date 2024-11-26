from django.test import TestCase

# Create your tests here.


from django.contrib.auth.models import User
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Cria um usuário
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        # Cria um post
        testpost = Post.objects.create(autor=testuser1, titulo='PostTitle1', body="PostBody...")
        testpost.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        autor = f'{post.autor}'
        titulo = f'{post.titulo}'
        body = f'{post.body}'

        self.assertEqual(autor, 'testuser1')
        self.assertEqual(titulo, 'PostTitle1')
        self.assertEqual(body, 'PostBody...')

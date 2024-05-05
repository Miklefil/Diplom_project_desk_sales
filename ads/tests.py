from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from ads.models import Ad, Review
from users.models import User


class AdTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@example.com', password='test', first_name='Test',
                                        last_name='Testov')
        self.client.force_authenticate(user=self.user)

        self.ad = Ad.objects.create(
            title="Test",
            price=100,
            author=self.user,
            description="Test",
            created_at="2022-02-03T09:10:16.332479Z"
        )

    def test_create_ad(self):
        """Тестирование создания объявления"""
        data = {
            "title": "Test1",
            "price": 100,
            "author": self.user,
            "description": "Test1",

        }

        response = self.client.post(
            path='/api/ads/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Ad.objects.all().exists()
        )

    def test_list_ads(self):
        """Тестирование вывода списка объявлений"""

        response = self.client.get(
            path='/api/ads/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Ad.objects.all().count(),
            1
        )

    def test_retrieve_ad(self):
        """Тестирования детальной информации об объявлении"""
        response = self.client.get(
            path=f'/api/ads/{self.ad.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": self.ad.pk,
                "author": self.user.pk,
                "author_first_name": "Test",
                "author_last_name": "Testov",
                "author_email": "test@example.com",
                "author_phone": None,
                "title": "Test",
                "price": 100,
                "description": "Test",
                "created_at": "2022-02-03T09:10:16.332479Z",
                "image": None,
            }
        )

    def test_update_ad(self):
        """Тестирование обновления объявления"""
        data = {
            "title": 'test_update'
        }

        response = self.client.patch(
            path=f'/api/ads/{self.ad.pk}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['title'],
            data['title']
        )

    def test_destroy_ad(self):
        """Тестирование удаления объявления"""
        response = self.client.delete(
            path=f'/api/ads/{self.ad.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class ReviewTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@example.com', password='test', first_name='Test',
                                        last_name='Testov')
        self.client.force_authenticate(user=self.user)

        self.ad = Ad.objects.create(
            title="Test",
            price=100,
            author=self.user,
            description="Test",
            created_at="2022-02-03T09:10:16.332479Z"
        )

        self.review = Review.objects.create(
            text="Test",
            author=self.user,
            ad=self.ad,
            created_at="2022-02-04T09:10:16.332479Z"
        )

    def test_create_review(self):
        """Тестирование создания отзыва"""
        data = {
            "text": "Test1",
            "author": self.user.pk,
            "ad": self.ad.pk,
            "created_at": "2022-02-04T09:10:16.332479Z",

        }

        response = self.client.post(
            path=f'/api/ads/{self.ad.pk}/comments/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Review.objects.all().exists()
        )

    def test_list_ads(self):
        """Тестирование вывода списка отзыва у объявления"""

        response = self.client.get(
            path=f'/api/ads/{self.ad.pk}/comments/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Review.objects.all().count(),
            1
        )

    def test_retrieve_review(self):
        """Тестирования детальной информации об отзыве"""
        response = self.client.get(
            path=f'/api/ads/{self.ad.pk}/comments/{self.review.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": self.review.pk,
                "text": "Test",
                "ad": self.ad.pk,
                "author": self.user.pk,
                "author_first_name": "Test",
                "author_last_name": "Testov",
                "author_avatar": None,
                "created_at": "2022-02-04T09:10:16.332479Z",
            }
        )

    def test_update_review(self):
        """Тестирование обновления отзыва"""
        data = {
            "text": 'test_update'
        }

        response = self.client.patch(
            path=f'/api/ads/{self.ad.pk}/comments/{self.review.pk}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['text'],
            data['text']
        )

    def test_destroy_review(self):
        """Тестирование удаления отзыва"""
        response = self.client.delete(
            path=f'/api/ads/{self.ad.pk}/comments/{self.review.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

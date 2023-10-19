from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from habits.models import Habit
from users.models import Users


class HabitTestCase(APITestCase):

    def setUp(self):
        """ Prepare testing """
        self.user = Users(
            email="test@gmail.com",
            is_superuser=True,
            is_staff=False,
            is_active=True,
            )

        self.user.set_password("test")
        self.user.save()

        self.client = APIClient()
        token = AccessToken.for_user(user=self.user)
        self.token = token
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_list_habit(self):
        response = self.client.get("/habit/habits/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_habit(self):
        """ Test habit creation """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 1
            }

        response = self.client.post("/habit/habit/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.all().exists())

    def test_get_share_habits(self):
        """ Test get info about user public habits """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink beer.",
            "duration": 10,
            "is_public": "True",
            "owner": 2
        }

        data2 = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 2
        }

        self.client.post("/habit/habit/create/", data)
        self.client.post("/habit/habit/create/", data2)
        response = self.client.get("/habit/share_habits/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_habits(self):
        """ Test get info about user habits """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 2
        }

        data2 = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink beer.",
            "duration": 10,
            "is_public": "True",
            "owner": 2
        }

        self.client.post("/habit/habit/create/", data)
        self.client.post("/habit/habit/create/", data2)
        response = self.client.get("/habit/habits/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_full_information_habit(self):
        """ Test get full information about user habit """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink beer.",
            "duration": 10,
            "is_public": "True",
            "owner": 2
        }

        self.client.post("/habit/habit/create/", data)
        response = self.client.get("/habit/habit/2/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        """ Test updating user habit """
        habit = Habit.objects.create(
            owner=self.user,
            place='home',
            time='17:00:00',
            action='test',
            is_pleasant=False,
            frequency='SUNDAY',
            award='To drink beer.',
            duration=10,
            is_public=False,
        )
        new_place = {'place': 'bridge'}
        habit_update = reverse('habits:habit_update', kwargs={'pk': habit.pk})

        response = self.client.patch(habit_update, new_place, format='json', **self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['place'], 'bridge')

    def test_validate_duration_create_habit(self):
        """ Test that user con not create habit with duration greater than 120 seconds """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink beer.",
            "duration": 200,
            "is_public": "True",
            "owner": 5
        }

        response = self.client.post("/habit/habit/create/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_pleasant_create_habit(self):
        """ Test that pleasant habit does not have award """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "True",
            "frequency": "SUNDAY",
            "award": "To drink beer.",
            "duration": 10,
            "is_public": "True",
            "owner": 5
        }

        response = self.client.post("/habit/habit/create/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_usual_create_habit(self):
        """ Test that usual habit must has award or pleasant habit """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "duration": 10,
            "is_public": "True",
            "owner": 5
        }

        response = self.client.post("/habit/habit/create/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


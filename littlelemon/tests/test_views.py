from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(
            title="Ham",
            price=120,
            inventory=10
        )

        Menu.objects.create(
            title="Burger",
            price=80,
            inventory=15
        )

    def test_getall(self):
        items = Menu.objects.all()

        serialized_data = MenuSerializer(items, many=True).data

        self.assertEqual(len(serialized_data), 2)
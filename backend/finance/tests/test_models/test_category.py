from uuid import uuid4

from django.test import TestCase

from ...models import Category


class CategoryTest(TestCase):
    """ Test module for Category model """
    category_id = uuid4()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Category.objects.create(
            id=cls.category_id,
            name="category_test",
            must_show=True,
            expected=150,
            is_active=True
        )

    def test_str_method(self):
        category = Category.objects.get(id=CategoryTest.category_id)
        self.assertEqual(str(category), "category_test, 150.00")

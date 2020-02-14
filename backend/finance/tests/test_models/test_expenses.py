from django.test import TestCase
from finance.tests.factories import ExpenseFactory

class Expenses(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("this")

    def setUp(self):
        print("testeando")

    def test_this(self):
        assert(True)

    def test_that(self):
        assert(True)
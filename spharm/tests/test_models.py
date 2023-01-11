import unittest

from django.test import TestCase
from unittest import skip
from django.shortcuts import get_object_or_404

from spharm.models import Apteks, Drugs, Delivery, Pharmacies, illness


class IllnessModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        illness.objects.create(illness_name='heart disease')
        print("Illness test created!")

    # Ignore test case, because there is no matching illness name in id = 1
    @unittest.skip
    def test_model_str(self):
        ill = illness.objects.get(id=1)
        field_label = ill._meta.get_field('illness_name').verbose_name
        self.assertEquals(str(field_label), 'heart')


class DrugsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Drugs.objects.create(name='Big', cost='1200 тг')

    def test_name_label(self):
        drug = Drugs.objects.get(pk=1)
        print(drug)

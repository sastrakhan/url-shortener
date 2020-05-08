from django.test import TestCase
from .models import URL, URLVisit, CustomURL
from .utilities import generate_id_from_url
from .views import show_url_stats, _process_visits
from django.http import HttpResponse, JsonResponse
from datetime import date


class URLModelTestCase(TestCase):
    base_url = "a test url"
    base_url_slug = "a-test-url"

    def setUp(self):
        url = URL.objects.create(original_name=self.base_url, latest_custom_url="1-2-3 test")
        URLVisit.objects.create(url=url)
        URLVisit.objects.create(url=url)

    def test_url_model_populates_properly(self):
        url = URL.objects.get(original_name=self.base_url_slug)
        self.assertEqual(url.latest_custom_url, "1-2-3-test")

    def test_id_generator_matches_model(self):
        url = URL.objects.get(original_name=self.base_url_slug)
        generated_short_link = str(generate_id_from_url(self.base_url_slug))
        self.assertEqual(url.shortened_version, generated_short_link)

    def test_url_stats_aggregation(self):
        non_existent_url = show_url_stats({}, "Non existent URL")
        self.assertIsInstance(non_existent_url, HttpResponse)

        url = URL.objects.get(original_name=self.base_url_slug)
        url_visits = URLVisit.objects.filter(url=url)
        visit_totals = _process_visits(url_visits)

        date_time_key = str(date.today())

        self.assertEqual(visit_totals.get("total"), 2)
        self.assertEqual(visit_totals.get("grouped").get(date_time_key), 2)

    # TODO: More robust testing on ensuring duplicates aren't being generated
    # and all relationships are being properly created






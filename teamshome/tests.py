from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, TextVideoPageView


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self): # new
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class TextVideoPageTests(SimpleTestCase): # new

    def setUp(self):
        url = reverse('textvideo_about')
        self.response = self.client.get(url)

    def test_textvideopage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_textvideopage_template(self):
        self.assertTemplateUsed(self.response, 'textvideo_about.html')

    def test_textvideopage_contains_correct_html(self):
        self.assertContains(self.response, 'Text and Video Call')

    def test_textvideopage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_textvideopage_url_resolves_textvideopageview(self):
        view = resolve('/textvideo/')
        self.assertEqual(
            view.func.__name__,
            TextVideoPageView.as_view().__name__
        )
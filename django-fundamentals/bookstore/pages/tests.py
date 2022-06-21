from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    ## URL Tests
    def test_homepage_status_code(self):
        self.assertEqual(200, self.response.status_code)


    def test_hompage_url_name(self):
        self.assertEqual(200, self.response.status_code)

    ## Template Test
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')


    ## HTML Test
    def test_homepage_template_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_hompage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'This BS should not be on the page')

    ## Resolving Test
    def test_homepage_url_resolves_homepage_view(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__, 
            HomePageView.as_view().__name__
        )
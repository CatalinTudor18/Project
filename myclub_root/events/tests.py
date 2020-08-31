from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from events.models import Item
from events.views import *

# Create your tests here.
class HomePageTest(TestCase):

    def test_Cv_view(self):
        found = resolve('/CV/')
        self.assertEqual(found.func, CV)

    def test_Cv_Page_html(self):
        request = HttpRequest()
        response = CV(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Create your CV</title>', html)
        self.assertIn('input type="name" name="name" class="form-control" id="name"', html)

    def test_redirects_after_POST(self):
        response = self.client.post('/CV/', data={'name': 'Catalin Tudor'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    # def test_only_saves_items_when_necessary(self):
    #     self.client.get('/')
    #     self.assertEqual(Item.objects.count(), 0)
    #
    # def test_displays_all_list_items(self):
    #     Item.objects.create(text='itemey 1')
    #     Item.objects.create(text='itemey 2')
    #
    #     response = self.client.get('/')
    #
    #     self.assertIn('itemey 1', response.content.decode())
    #     self.assertIn('itemey 2', response.content.decode())

# class ItemModelTest(TestCase):
#     def test_saving_and_retrieving_items(self):
#         first_item = Item()
#         first_item.text = 'The first (ever) list item'
#         first_item.save()
#
#         second_item = Item()
#         second_item.text = 'Item the second'
#         second_item.save()
#
#         saved_items = Item.objects.all()
#         self.assertEqual(saved_items.count(), 2)
#
#         first_saved_item = saved_items[0]
#         second_saved_item = saved_items[1]
#         self.assertEqual(first_saved_item.text, 'The first (ever) list item')
#         self.assertEqual(second_saved_item.text, 'Item the second')

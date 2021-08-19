from django.test import SimpleTestCase

from impresses.forms import ImpressForm


class TestForms(SimpleTestCase):

    def test_impress_form_valid_data(self):
        form = ImpressForm(data={
            'name': 'qwe',
            'info': 'wqe',
            'location': '92.87558310090435,56.009795429060546',
            'address': "People's, ул. Сурикова, 12, Красноярск, Красноярский край 660097, Россия"
        })

        self.assertTrue(form.is_valid())

    def test_impress_form_no_data(self):
        form = ImpressForm(data={'location': '92.87558310090435,56.009795429060546',})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
        #qwe

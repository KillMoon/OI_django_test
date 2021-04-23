from django.test import SimpleTestCase

from impresses.forms import ImpressForm


class TestForms(SimpleTestCase):

    def test_impress_form_valid_data(self):
        form = ImpressForm(data={
            'name': 'qwe',
            'info': 'wqe'
        })

        self.assertTrue(form.is_valid())

    def test_impress_form_no_data(self):
        form = ImpressForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

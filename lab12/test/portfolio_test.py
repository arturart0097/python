from flask import url_for
from .base import BaseTest

class PortfolioTest(BaseTest):
    def test_view_index(self):
        '''Tests if the portfolio index page loads correctly.'''
        with self.client:
            response = self.client.get(url_for('portfolio.index'))

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'hi', response.data)
            self.assertIn(b"I'm", response.data)
            self.assertIn(b"Sabetskyiii", response.data)

    def test_view_about(self):
        '''Tests if the portfolio about page loads correctly.'''
        with self.client:
            response = self.client.get(url_for('portfolio.about'))

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Artur Sabetskyi', response.data)

    def test_view_contact(self):
        ''' Tests if the portfolio contact page loads correctly.'''
        with self.client:
            response = self.client.get(url_for('portfolio.contact'))

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Contacts', response.data)

    def test_view_skills(self):
        '''Tests if the portfolio skills page loads correctly.'''
        with self.client:
            response = self.client.get(url_for('portfolio.skill'))

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Rest', response.data)
            self.assertIn(b'Rust', response.data)
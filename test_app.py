from app import app
from unittest import TestCase, main

class ColorViewsTestCase(TestCase):
    
    def test_color_form(self):
        with app.test_client() as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            
            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>Color Form</h1>', html)
if __name__ == '__main__':
    main(verbosity=2)
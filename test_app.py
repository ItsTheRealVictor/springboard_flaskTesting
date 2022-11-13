from app import app
from flask import session
from unittest import TestCase, main


# turns errors into python errors
app.config['TESTING'] = True

# stopping the debug toolbar from working during our tests. We don't want that html to interfere with our tests
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']



class ColorViewsTestCase(TestCase):
    
    @classmethod
    def setUpClass(cls):
        '''Runs only once, before all tests'''
        print('INSIDE SET UP CLASS. I ONLY RUN ONE TIME')
    
    @classmethod
    def tearDownClass(cls):
        '''Runs only once, after all tests'''
        print('INSIDE TEARDOWN CLASS. I ALSO ONLY RUN ONE TIME')
    
    
    
    def setUp(self):
        '''
        This is stuff we want to do BEFORE every test. It has logic that we want all our tests to have in common
        '''
        print('THIS IS A SETUP')
    
        
    def tearDown(self):
        '''
        This is stuff we want to do AFTER every test. Usually for cleaning up any changes to a database and returning it
        to its original state (before the tests)
        '''
        print('THIS IS A TEARDOWN')
    
    
    def test_color_form(self):
        '''
        tests GET requests
        '''
        
        with app.test_client() as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            
            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>Color Form</h1>', html)
            
    def test_color_form_post(self):
        '''
        tests POST requests
        '''
        
        with app.test_client() as client:
            response = client.post('/fav-color', data={'color':'orange'})
            html = response.get_data(as_text=True)
            
            self.assertEqual(response.status_code, 200)
            self.assertIn('<h3>Woah! I like orange, too</h3>', html)
            
        
    def test_redirecting(self):
        '''
        testing the redirect
        '''
        with app.test_client() as client:
            response = client.get('/redirect-me')
            
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/')
    
    def test_redirect_follow(self):
        '''
        tests to make sure we get the html we want after the redirect is made
        '''
        
        with app.test_client() as client:
            response = client.get('/redirect-me', follow_redirects=True)
            html = response.get_data(as_text=True)
            
            
            
            self.assertEqual(response.status_code, 200)
            self.assertIn('h1>Color Form</h1>', html)
            
    def test_session(self):
        '''
        testing to see that the session data is properly updated
        '''
        with app.test_client() as client:
            response = client.get('/')
            
            
            # testing if the very first request results in a session count of 1.
            self.assertEqual(response.status_code, 200)
            self.assertEqual(session['count'], 1)
            
    def test_session_count(self):
        with app.test_client() as client:
            
            
            # explicitly initializing session data to something we want to test
            with client.session_transaction() as session_change:
                session_change['count'] = 999
                
            response = client.get('/')
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(session['count'], 1000)




            
if __name__ == '__main__':
    main(verbosity=2)
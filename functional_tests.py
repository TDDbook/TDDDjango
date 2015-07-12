from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Bob wants to create a to-do list. He hears about this app,
        # and goes to its homepage
        self.browser.get('http://localhost:8000')

        # He sees that the title of the page mentions to-do lists.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!') # Indicates the test is not complete.

        # He is invited to enter a to-do item immediately after the page loads.

        # He types "Buy peacock feathers" into a text box labelled...

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list.

        # There is still a text box inviting him to add another item. He
        # enters "Use peacock feathers to make a fly."

        # The page updates again, and now shows both items on his list.

        # Bob wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # He visits the URL - his to-do list is still there.
if __name__ == '__main__':
    unittest.main(warnings='ignore')

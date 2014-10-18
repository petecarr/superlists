from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

   def setUp(self):
      self.browser = webdriver.Firefox()
      self.browser.implicitly_wait(3)

   def tearDown(self):
      self.browser.quit()

   def test_can_start_a_list_and_retrieve_it_later(self):

      # User has heard about a cool new online to-do app. Goes
      # to check out its home page.
      self.browser.get('http://localhost:8000')

      # Notices the page title and header mention to-do lists
      self.assertIn('To-Do', self.browser.title) 
      self.Fail('Finish the test!')
      
      # User is invited to enter a to-do item straight away

      # User types "Buy Peacock feathers" into a text box. 
      #(Everyone needs Peacock feathers)

      # When user hits enter, the page updates, and now the page lists
      # 1. "Buy peacock feathers" as an item in a to-do list.

      # There is still a text box inviting the user to add another item. 
      # Enters "Use Peacock feathers to make a fly"

      # Page updates again, and now shows both items on the list.

      # User wonders whether the site will remember her list. Then she sees
      # that the site has generated a unique URL for her -- there is some 
      # explanatory text to that effect.

      # She visits that URL - her to-do list is still there.

      # Satisfied sho goes back to sleep.

if __name__ == '__main__': #
   unittest.main(warnings='ignore') #

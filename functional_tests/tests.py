from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):

   def setUp(self):
      self.browser = webdriver.Firefox()
      self.browser.implicitly_wait(3)

   def tearDown(self):
      self.browser.quit()

   def check_for_row_in_list_table(self, row_text):
      table = self.browser.find_element_by_id('id_list_table')
      rows = table.find_elements_by_tag_name('tr')
      self.assertIn(row_text, [row.text for row in rows])


   def test_can_start_a_list_and_retrieve_it_later(self):

      # User has heard about a cool new online to-do app. Goes
      # to check out its home page.
      self.browser.get(self.live_server_url)

      # Notices the page title and header mention to-do lists
      #print("Title is :" + self.browser.title)
      self.assertIn('To-Do', self.browser.title) 
      header_text = self.browser.find_element_by_tag_name('h1').text
      #print(header_text + '\n')
      self.assertIn('To-Do', header_text) 

      # User is invited to enter a to-do item straight away
      inputbox = self.browser.find_element_by_id('id_new_item')
      self.assertEqual(
             inputbox.get_attribute('placeholder'),
	     'Enter a to-do item'
	     )

      # User types "Buy peacock feathers" into a text box. 
      #(Everyone needs peacock feathers)
      inputbox.send_keys('Buy peacock feathers')

      # When user hits enter, the page updates, and now the page lists
      # 1. "Buy peacock feathers" as an item in a to-do list.
      inputbox.send_keys(Keys.ENTER)
      self.check_for_row_in_list_table('1: Buy peacock feathers')


      # There is still a text box inviting the user to add another item. 
      # Enters "Use Peacock feathers to make a fly"
      inputbox = self.browser.find_element_by_id('id_new_item')
      inputbox.send_keys('Use peacock feathers to make a fly')
      inputbox.send_keys(Keys.ENTER)

      # Page updates again, and now shows both items on the list.
      self.check_for_row_in_list_table('2: Use peacock feathers to make a fly') 
      self.check_for_row_in_list_table('1: Buy peacock feathers')


      # User wonders whether the site will remember her list. Then she sees
      # that the site has generated a unique URL for her -- there is some 
      # explanatory text to that effect.

      # She visits that URL - her to-do list is still there.

      # Satisfied sho goes back to sleep.
      self.fail('Finish the test!')

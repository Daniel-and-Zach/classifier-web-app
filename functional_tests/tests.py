from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


#
# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')
class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def make_text_entry(self, text):
        inputbox = self.browser.find_element_by_id('code_box')
        inputbox.send_keys(text)
        inputbox.send_keys(Keys.ENTER)

    def test_open_browser(self):
        # User Opens browser, and goes to the index.
        self.browser.get(self.live_server_url)
        # User knows it's the correct page by the title/header.
        self.assertIn('Language Classifier', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Language Classifier', header_text)
        # User sees a text box to enter code.
        text_area = self.browser.find_element_by_tag_name('textarea').is_displayed()
        self.assertTrue(text_area)
        # User enters code:
        self.make_text_entry('def my_function(): pass')
        # User is redirected to a new page and it now lists the code type:
        user_answer_url = self.browser.current_url
        self.assertRegex(user_answer_url, '/result/.+')

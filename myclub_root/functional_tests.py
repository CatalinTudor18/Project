from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000/CV')


        inputbox = self.browser.find_element_by_id('fname')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'ff'
        )
        inputbox.send_keys("Catalin")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('lname')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'll'
        )
        inputbox.send_keys("Tudor")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # self.check_for_row_in_list_table('1: Buy peacock feathers')
        # self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

assert 'Django' in browser.title

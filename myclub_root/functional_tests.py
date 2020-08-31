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


        inputbox = self.browser.find_element_by_id('name')
        self.assertEqual(
            inputbox.get_attribute('name'),
            'name'
        )
        inputbox.send_keys("Catalin Tudor")
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('email')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter Email'
        )
        inputbox.send_keys("tudorkatalin2000@gmail.com")

        inputbox = self.browser.find_element_by_id('phone')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Phone No.'
        )
        inputbox.send_keys("0748933953")

        inputbox = self.browser.find_element_by_id('address')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Your address'
        )
        inputbox.send_keys("Pistol Street, Number 358, Odobesti, Dambovita, Romania")

        inputbox = self.browser.find_element_by_id('linkedin')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter the link to your LinkedIn profile'
        )
        inputbox.send_keys("https://www.linkedin.com/in/catalin-t-746a4911b")

        inputbox = self.browser.find_element_by_id('summary')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Summary'
        )
        inputbox.send_keys("An enthusiast Computer Science final year student. Ready to tackle problems, especially those related to machine learning. A nerd who loves Atom, OS X and enjoys to customize his working environment. Always looking for another way of solving a given task, and learning new technologies and tools if the need arises. I am focused on improving my lifestyle by committing to a learning process that relies on hard work.")

        inputbox = self.browser.find_element_by_id('school')
        self.assertEqual(
            inputbox.get_attribute('name'),
            'school 1'
        )
        inputbox.send_keys("Univesity of Birmingham")

        inputbox = self.browser.find_element_by_id('year')
        self.assertEqual(
            inputbox.get_attribute('name'),
            'year 1'
        )
        inputbox.send_keys("2021")

        inputbox = self.browser.find_element_by_id('marks')
        self.assertEqual(
            inputbox.get_attribute('name'),
            'marks 1'
        )
        inputbox.send_keys("2.1")

        inputbox = self.browser.find_element_by_id('skills')
        self.assertEqual(
            inputbox.get_attribute('name'),
            'skills'
        )
        inputbox.send_keys("Eclipse, Java, HTML, CSS, Python, Machine Learning")

        inputbox = self.browser.find_element_by_id('experience')
        self.assertEqual(
            inputbox.get_attribute('name'),
            'experience'
        )
        inputbox.send_keys("Website Administrator - I used to post on the webiste that I administer since high-school.")

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # self.check_for_row_in_list_table('1: Buy peacock feathers')
        # self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

assert 'Django' in browser.title

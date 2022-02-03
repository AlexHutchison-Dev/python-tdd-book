from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item
        input_box = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        # She types in "By Peacock feathers" into a text box ( Edith's hobby
        # is tying fly-fishing lures)
        input_box.send_keys("Buy peacock feathers")

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item on the to-do list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id("id_list-table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(
            "1: Buy peacock feathers",
            [row.text for row in rows],
            f"New item did not appear in table. Contents were: \n {table.text}",
        )

        # There is still a text box inviting her to add another item. She enters
        # "Use peacock feathers to make a fly" (Edith is very Methodical)
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, now showing both items on her list

        table = self.browser.find_element_by_id("id_list-table")
        rows = self.browser.find_elements_by_tag_name("tr")
        self.assertIn(
            "1: Buy peacock feathers",
            [row.text for row in rows],
            f"New item did not appear in table. Contents were: \n {table.text}",
        )
        self.assertIn(
            "2: Use peacock feathers to make a fly",
            [row.text for row in rows],
            f"New item did not appear in table. Contents were: \n {table.text}",
        )
        # Edith wonders weather the site will remember her list. Then she notices
        # that the site has generated a unique URL for her -- there is some
        # explanitory text to that effect

        self.fail("Finish the tests!")
        # She visits the URL - her to-do list is still there

        # Satisfied she goes to sleep


if __name__ == "__main__":
    unittest.main()

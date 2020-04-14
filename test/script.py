import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='content-main']/div[2]/table/tbody/tr[1]/td[1]/a").click()
        time.sleep(5)
        elem = driver.find_element_by_name("cust_name")
        elem.send_keys("safi")
        elem = driver.find_element_by_name("organization")
        elem.send_keys("ISQA")
        elem = driver.find_element_by_name("role")
        elem.send_keys("student")
        elem = driver.find_element_by_name("email")
        elem.send_keys("asor@unomah.edu")
        elem = driver.find_element_by_name("bldgroom")
        elem.send_keys("100")
        elem = driver.find_element_by_name("account_number")
        elem.send_keys("100")
        elem = driver.find_element_by_name("address")
        elem.send_keys("south 68st")
        elem = driver.find_element_by_name("city")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_name("state")
        elem.send_keys("Ne")
        elem = driver.find_element_by_name("zipcode")
        elem.send_keys("77700")
        elem = driver.find_element_by_name("phone_number")
        elem.send_keys("4026148900")
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='customer_form']/div/div/input[1]").click()
        time.sleep(5)
        assert "Posted customer Entry"
        driver.get("http://127.0.0.1:8000/customer_list")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

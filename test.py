from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class FooterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        sleep(10)

    def test_footer_presence(self):
        pages = [
            "https://only.digital/",
            "https://only.digital/projects",
            "https://only.digital/company",
            "https://only.digital/job",
            "https://only.digital/contacts"
        ]

        for page in pages:
            self.driver.get(page)
            if (WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//footer"))
            )):
                print("Футер на странице:"+ page + " есть")
            else:
                print("Футер на странице:"+ page + " отсутствует")

    def test_footer_elements(self):
        self.driver.get("https://only.digital/")
        elements = [
            ("email","//a[@href='mailto:hello@only.com.ru']"),
            ("telegram","//a[@href='https://t.me/onlycreativedigitalagency']")
        ]

        for element_name, xpath in elements:
            if (WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )):
                print("Элемент " + element_name + " присутствует в футере.")
            else:
                print("Элемент "+ element_name +" отсутствует в футере.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
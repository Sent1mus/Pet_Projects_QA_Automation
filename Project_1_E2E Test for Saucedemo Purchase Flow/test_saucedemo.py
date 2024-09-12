import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class TestSaucedemo(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Запуск без графического интерфейса
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.maximize_window()

    def test_saucedemo_purchase(self):
        # Авторизация
        self.driver.get("https://www.saucedemo.com/")
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # Выбор товара
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_to_cart_button.click()

        # Переход в корзину
        cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()

        # Оформление покупки
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        last_name_input = self.driver.find_element(By.ID, "last-name")
        postal_code_input = self.driver.find_element(By.ID, "postal-code")

        first_name_input.send_keys("Ivan")
        last_name_input.send_keys("Ivanov")
        postal_code_input.send_keys("123456")

        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
        )
        finish_button.click()

        # Проверка успешного завершения покупки
        complete_header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        self.assertEqual(complete_header.text, "Thank you for your order!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

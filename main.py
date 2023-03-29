from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set the path to the downloaded driver for Brave
driver_path = "C:\\Users\\Olivier Luethy\\Downloads\\chromedriver_win32\\chromedriver.exe"

# Create a new instance of the Brave driver
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Navigate to the Clockodo website
url = "https://my.clockodo.com/"
driver.get(url)

# fill in the email and password
email_input = driver.find_element("id", 'loginForm-email')
email_input.send_keys("olivier@kauz.ch")

password_input = driver.find_element("id", 'loginForm-password')
password_input.send_keys("Passwort")

# click on the login button
login_button = driver.find_element("id", "loginForm-Login")
login_button.click()

# wait for the page to load
driver.implicitly_wait(10)

# Navigate to the calendar view
url = "https://my.clockodo.com/de/entries/"
driver.get(url)

# Find the button and click it
button = driver.find_element("id", "linkAddTimeEntry")
button.click()

# Wait for the form to load
time.sleep(1)

# Fill in the form fields
start_time_field = driver.find_element("id", "entryForm-add-time_since")
ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
start_time_field.send_keys("07:30")

# Wait for the form to load
time.sleep(1)

end_time_field = driver.find_element("id", "entryForm-add-time_until")
ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
end_time_field.send_keys("17:00")

# Wait for the form to load
time.sleep(1)

pause_start_field = driver.find_element("id", "entryForm-add-break_start")
ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
pause_start_field.send_keys("12:00")

# Wait for the form to load
time.sleep(1)

pause_duration_field = driver.find_element("id", "entryForm-add-break_minutes")
ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
pause_duration_field.send_keys("60")

# Wait for the form to load
time.sleep(1)

# Find the "Speichern" button within the form and click it
save_button = driver.find_element("xpath", '//button[contains(text(), "Speichern")]')
save_button.click()

# Close the browser
driver.quit()

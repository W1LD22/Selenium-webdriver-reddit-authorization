from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get('https://www.reddit.com/')

loginButton = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[2]/div/div[1]/a[1]')
loginButton.click()

driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

usernameField = driver.find_element_by_name('username')
usernameField.send_keys("usersdsd")

passwordField = driver.find_element_by_name('password')
passwordField.send_keys("123456789")

driver.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button').send_keys(Keys.ENTER)
driver.implicitly_wait(3)
username = driver.find_element_by_xpath('//*[@id="email-collection-tooltip-id"]/span/span[1]').text
assert username == 'usersdsd'
driver.quit()

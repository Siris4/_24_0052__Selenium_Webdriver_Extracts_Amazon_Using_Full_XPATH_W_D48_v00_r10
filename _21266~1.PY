
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

url = "https://www.python.org/events/"

# opening Chrome:
options = webdriver.ChromeOptions()

# and keeping Chrome open:
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)


# FULL XPATH:
event_data_and_time0 = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div/div/ul/li[1]/p/time")
event_url0 = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div/div/ul/li[1]/h3/a")

event_data_and_time1 = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div/div/ul/li[2]/p/time")
event_url1 = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div/div/ul/li[2]/h3/a")

event_data_and_time2 = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div/div/ul/li[3]/p/time")
event_url2 = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div/div/ul/li[3]/h3/a")

event_data_and_time3 = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div/div/ul/li[4]/p/time")
event_url3 = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div/div/ul/li[4]/h3/a")

event_data_and_time4 = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div/div/ul/li[5]/p/time")
event_url4 = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div/div/ul/li[5]/h3/a")

print(f"The event starts and is located at: Time: {event_data_and_time0.text}; and the Location: {event_url0.text}.")
print(f"The event starts and is located at: Time: {event_data_and_time1.text}; and the Location: {event_url1.text}.")
print(f"The event starts and is located at: Time: {event_data_and_time2.text}; and the Location: {event_url2.text}.")
print(f"The event starts and is located at: Time: {event_data_and_time3.text}; and the Location: {event_url3.text}.")
print(f"The event starts and is located at: Time: {event_data_and_time4.text}; and the Location: {event_url4.text}.")


# quits the entire web browser INCLUDING all of the tabs that are still OPEN (the moment it loads the webpage):
driver.quit()    # COMMENT THIS OUT TO KEEP IT OPEN!!!!

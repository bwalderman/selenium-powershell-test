from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

edge_options = Options()
edge_options.use_chromium = True
edge_options.binary_location = 'C:\\Users\\JenkinsUser\\AppData\\Local\\Microsoft\\Edge SxS\\Application\\msedge.exe'

driver = webdriver.Edge(options=edge_options, verbose=True, service_args=['--verbose'])

try:
    driver.set_window_rect(x=10,y=10, width=600, height=600)
    rect = driver.get_window_rect()
    print(rect)
    driver.maximize_window()
    rect = driver.get_window_rect()
    print(rect)
    driver.get('https://bing.com')
finally:
    driver.quit()
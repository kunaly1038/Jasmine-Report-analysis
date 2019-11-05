from selenium import webdriver
import time



driver = webdriver.Chrome(executable_path=r"D:\ACA Report analysis\chromedriver.exe")
driver.maximize_window()
driver.get("file:///D:/ACA@/ims-web-ui-testing/e2e-tests/testResult/TestResult.html")
driver.find_element_by_xpath('//*[normalize-space(text())="ALL"]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[normalize-space(text())="FAILED"]').click()

time.sleep(6)
driver.close()

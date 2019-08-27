from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import config
import time
import arrow

def create_quote():
    print("Luma QA Test Start")
    browser = webdriver.Chrome("./chromedriver")
    browser.get(config.qa_server)
    login_hover = browser.find_element_by_xpath(
        '//*[@id="loginRegisterLink"]').click()
    login_field = browser.find_element_by_xpath(
        '//*[@id = "inputUserName"]').send_keys(config.logins[0])
    password_field = browser.find_element_by_xpath(
        '//*[@id="inputPassword"]').send_keys(config.password)
    login_button = browser.find_element_by_xpath('//*[@id="loginButton"]').click()
    dont_show_again_checkbox = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-checkbox-1"]'))).click()
    confirm_dont_show_again = browser.find_element_by_xpath('//*[@id="disclaimerDialog"]/div[2]/button').click()
    creation_hub = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/main/app-dashboard/div/div[2]/a'))).click()
    new_request = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="dynamicTabPricingTool"]/li[2]/a'))).click()
    product_type = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="newrequest-productSelection"]/div/div/div/div/div/div[2]/div/span'))).click()
    product_type_registered_note = browser.find_element_by_xpath("//li[contains(text(),'Registered Note')]").click()
    structured_group = browser.find_element_by_xpath('//*[@id="newrequest-productSelection"]/div/div/div/div/div/div[3]/div/span').click()
    structured_group_digital = browser.find_element_by_xpath("//li[contains(text(),'Digital')]").click()
    time.sleep(60)
    underlying_input = WebDriverWait(browser, 60).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="customFeatuersProductSelection"]/div[1]/div[1]/span/span[1]/span/ul/li/input'))).send_keys('7203 JT Equity')
    underlying_input_selection = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'7203 JT Equity')]"))).click()
    next_step_one = WebDriverWait(browser, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="ActionPaginationNext"]'))).click()
    solve_for_months = WebDriverWait(browser, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="term1"]'))).send_keys('3')
    buffer_percentage = browser.find_element_by_xpath('//*[@id="BufferPercentageSolveFor1"]').send_keys('50')
    maximum_upside_return = browser.find_element_by_xpath('//*[@id="MaximumUpsideReturnSolveFor1"]').send_keys('50')
    time.sleep(60)
    step_two_next = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ActionPaginationNext"]'))).click()
    date_today = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="tradeDate"]'))).send_keys(arrow.now().format('MM-DD-YYYY'))
    issuer_input = WebDriverWait(browser, 60).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="customFeaturesDatesAndOther"]/div/div[1]/div[5]/div/span/span[1]/span/ul/li/input'))).send_keys('Bank of America')
    issuer_input_data = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Bank of America')]"))).click()
    request_live_price = browser.find_element_by_xpath('//*[@id="requestPriceSubmit"]').click()
    time.sleep(30)
    quote_request_id = browser.find_element_by_xpath('//*[@id="newlyCreatedRequestsTable"]/p')
    print(quote_request_id.text)
    print("Luma QA Test End")

if __name__ == '__main__':
    create_quote()
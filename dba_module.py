from selenium import webdriver

url = 'https://www.dba.dk'
browser = webdriver.Firefox()

def search(phrase):
    browser.get(url)
    browser.implicitly_wait(1)
    search_field = browser.find_element_by_id('searchField')
    search_field.send_keys(phrase)
    search_field.submit()

def search_recent(phrase):
    search(phrase)
    browser.implicitly_wait(3)
    a = browser.find_element_by_xpath("//h4[contains(text(),'Oprettet')]")    
    browser.execute_script("arguments[0].click();",a)
    browser.implicitly_wait(1)
    b = browser.find_element_by_xpath("//span[contains(text(),'Seneste 24 timer')]")
    browser.execute_script("arguments[0].click();",b)
from selenium import webdriver
url = 'https://www.dba.dk'
browser = webdriver.Firefox()

def search(phrase):
    browser.get(url)
    browser.implicitly_wait(3)
    search_field = browser.find_element_by_id('searchField')
    search_field.send_keys(phrase)
    search_field.submit()

def search_recent(phrase):
    search(phrase)
    a = browser.find_element_by_tag_name('span').text('Seneste 24 timer')
    a.click()
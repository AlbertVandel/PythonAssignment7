from selenium import webdriver
from operator import itemgetter
import bs4

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

def search_cph(phrase):
    search(phrase)
    browser.implicitly_wait(1)
    browser.find_element_by_xpath("//a[contains(text(),'København og omegn')]").click()
    return browser.page_source

def search_cph_recent(phrase):
    search(phrase)
    browser.implicitly_wait(3)
    browser.find_element_by_xpath("//a[contains(text(),'København og omegn')]").click()
    browser.implicitly_wait(3)
    a = browser.find_element_by_xpath("//h4[contains(text(),'Oprettet')]")    
    browser.execute_script("arguments[0].click();",a)
    browser.implicitly_wait(1)
    b = browser.find_element_by_xpath("//span[contains(text(),'Seneste 24 timer')]")
    browser.execute_script("arguments[0].click();",b)  
    return browser.page_source

def extract_products(source):
    soup = bs4.BeautifulSoup(source, 'html.parser')
    
    products = soup.find_all('tr',{'class': 'dbaListing'})
    
    products_list = []

    for p in products:
        description = p.select('td div a')[1].text
        price = int(''.join(filter(str.isdigit,p.select('a')[6].text)))
        image_url = p.select('td div a div')[0]
        details_url = p.select('td a')[1]
        t = (description,price,image_url,details_url)
        products_list.append(t)
    return sorted(products_list,key=itemgetter(1))
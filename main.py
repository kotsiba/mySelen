import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

proxy = ['x.xxx.xx.xx:xx']
# proxy_list = ['x.xxx.xx.xx:xx', 'x.xxx.xx.xx:xx', 'x.xxx.xx.xx:xx']
options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('extension.crx')
options_chrome.add_argument('--headless')   # or the same arg '--disable-gpu'
options_chrome.add_argument(r'user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data')   # add profile from chrome
options_chrome.add_argument('--proxy-server=%s' % proxy)

url = 'https://some.url'

# for proxy in proxy_list:

try:
    # browser = webdriver.Chrome('chromedriver.exe')
    
    s = Service(executable_path='chromedriver.exe')
    browser = webdriver.Chrome(service=s, options=options_chrome)

    browser.get(url)

    button = browser.find_element(By.ID, "id_name")
    button.click()
    browser.find_element(By.NAME, "name_name")  # attribute name 'value'
    browser.find_element(By.CLASS_NAME, "class_name").click()
    browser.find_element(By.TAG_NAME, "tag_name").send_keys('key')
    browser.find_element(By.CSS_SELECTOR, "css_rules")  # ???
    browser.find_element(By.LINK_TEXT, "exact_text")
    browser.find_element(By.PARTIAL_LINK_TEXT, "part_of_text")
    
    a = browser.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))
    
    value = browser.find_element(By.CLASS_NAME, 'class_name').text
    print(value)
    # value = browser.find_element(By.CLASS_NAME, 'class_name')
    # print(value.text)

    browser.find_element(By.XPATH, "//tag[@attribute='attr_name']")
    browser.find_element(By.XPATH, "//tag[text()='exact_text']")
    browser.find_element(By.XPATH, "//tag[contains(text(),'part_of_text')]")
    browser.find_element(By.XPATH, "//tag[@attribute='attr_name']")
    browser.find_element(By.XPATH, "//tag[text()='exact_text']")
    browser.find_element(By.XPATH, "//tag[contains(@attribute,'attribute_name')]")
    browser.find_element(By.XPATH, "//tag/*[@attribute='attr_name']")

    browser.find_element(By.XPATH, "//div[@class='text']/p[2]")

    browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    print(sum([int(x.text) for x in browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")]))

    [x.click() for x in browser.find_elements(By.CLASS_NAME, "name_class")]

    checkbox = browser.find_elements(By.CLASS_NAME, "class_name")
    for item in checkbox:
        print(item.get_attribute('name_attribute'))
        
    browser.back()
    browser.forward()
    browser.refresh()
    browser.maximize_window()
    browser.fullscreen_window()
    
    browser.implicitly_wait(10)
    
    browser.get_screenshot_as_file('file.jpg')
    browser.get_screenshot_as_base64()
    
    # scripts
    browser.execute_script("script_code")
    element = browser.find_element(By.XPATH, "//tag[@attribute='attr_name']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    
    browser.execute_script("return document.title;")    # return title of open document
    
    var = [x.tag_name for x in
           browser.execute_script("return document.anchors;")]  # return all document anchors for scrolling

    browser.execute_script("return document.getElementByClassName('name_class');")   # return all elements with 'name_class'
    browser.execute_script(
        "return document.getElementByTagName('name_tag');")  # return all elements with 'name_tag'
    
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")   # scroll to last pixel
    browser.execute_script("window.scrollBy(0,5000)"
                           
                           
    

finally:
    browser.close()
    browser.quit()




import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


proxy = ['x.xxx.xx.xx:xx']
# proxy_list = ['x.xxx.xx.xx:xx', 'x.xxx.xx.xx:xx', 'x.xxx.xx.xx:xx']
options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('extension.crx')
options_chrome.add_argument('--headless')  # or the same arg '--disable-gpu'
options_chrome.add_argument(
    r'user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data')  # add profile from chrome
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
    
    wait.until(EC.element_to_be_clickable((By.XPATH, '//tag[@attribute="name_attribute"]'))).click()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//tag[@attribute="name_attribute"]'))).click()   # from selenium.webdriver.support.ui import WebDriverWait
    

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
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)    # for element will in view space
    element.click()

    browser.execute_script("return document.title;")  # return title of open document

    var = [x.tag_name for x in
           browser.execute_script("return document.anchors;")]  # return all document anchors for scrolling

    browser.execute_script(
        "return document.getElementByClassName('name_class');")  # return all elements with 'name_class'
    browser.execute_script(
        "return document.getElementByTagName('name_tag');")  # return all elements with 'name_tag'
    
    ## scrolling
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll to last pixel
    browser.execute_script("window.scrollBy(0,5000);")
    ActionChains(browser).move_to_element(element).scroll_by_amount(1,500).perform()
    
    

    # from selenium.webdriver import Keys

    browser.find_element(By.TAG_NAME, 'name_tag').send_keys(Keys.DOWN)

    # from selenium.webdriver.common.action_chains import ActionChains

    menu = browser.find_element(By.CSS_SELECTOR, '.nav')
    hidden_submenu = browser.find_element(By.CSS_SELECTOR, '.nav #submenu1')
    ActionChains(browser).move_to_element(menu).click(hidden_submenu).perform()

    # or

    action = ActionChains(browser)
    time.sleep(1)
    action.move_to_element(menu)
    time.sleep(1)
    action.click(hidden_submenu)
    time.sleep(1)
    action.perform()

    ## or

    target = browser.find_element(By.ID, 'like')
    actions = ActionChains(browser).move_to_element(target).click().perform()

    ## or

    target = browser.find_element(By.ID, 'like')
    action = ActionChains(browser)
    time.sleep(1)
    action.move_to_element(target)
    time.sleep(1)
    action.click()
    time.sleep(1)
    action.perform()
    
    ## scroll_by_amount()
    
    ActionChains(browser).move_to_element(element).scroll_by_amount(1,500).perform()
    
    # windows and tabs
    
    browser.current_window_handle()
    browser.window_handles()
    browser.switch_to.window(window_handles[0])
    
    browser.get(url) # first tab, standart open
    browser.execute_script('window.open("https://some1.url","_blank1");') # open the next tab blank1
    browser.execute_script('window.open("https://some2.url","_blank2");') # open the next tab blank2
    
    for x in range(len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        time.sleep(1)
        print(browser.execute_script("return document.title;"), browser.window_handles[x])
    
    


finally:
    browser.close()
    browser.quit()

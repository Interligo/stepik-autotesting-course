from selenium import webdriver


browser = webdriver.Chrome()
# execute_script(javascript_code)
browser.execute_script("document.title='Script executing';alert('Robots at work');")

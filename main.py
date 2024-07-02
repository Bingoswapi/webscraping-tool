from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=google+images&sca_esv=a5295d27d6bcdf79&sca_upv=1&udm=2&biw=805&bih=607&sxsrf=ADLYWIKloWZ_g2Xj4TwWlwZv-8I41KomhA%3A1719902560993&ei=YKGDZoWnPKusxc8Pjd-0wA8&oq=goo&gs_lp=Egxnd3Mtd2l6LXNlcnAiA2dvbyoCCAAyBBAjGCcyDRAAGIAEGLEDGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigUyDRAAGIAEGLEDGEMYigUyCBAAGIAEGLEDMgsQABiABBixAxiDATIIEAAYgAQYsQMyBRAAGIAEMggQABiABBixA0iKJVCAB1jvGnACeACQAQCYAeEDoAHsCaoBBTMtMS4yuAEDyAEA-AEBmAIFoAKgCqgCCsICBxAjGCcY6gKYAwuIBgGSBwcyLjMtMS4yoAeBEg&sclient=gws-wiz-serp")
#driver.implicitly_wait(5)
search = driver.find_element(By.CLASS_NAME, "a4bIc").send_keys()

WebDriverWait(driver,10)

driver.implicitly_wait(10)
driver.quit()
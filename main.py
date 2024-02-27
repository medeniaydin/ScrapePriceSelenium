from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait # webidriver'i bekletme
from selenium.webdriver.support import expected_conditions
import time

driver = Driver(uc=True)

driver.get("https://www.trendyol.com/butik/liste/5/elektronik")

WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"V8wbcUhU")))
search_bar_by_class =  driver.find_element(By.CLASS_NAME,"V8wbcUhU")

search_bar_by_class.send_keys("Bilgisayar")
WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"cyrzo7gC")))
search_button_by_name =  driver.find_element(By.CLASS_NAME,"cyrzo7gC")

WebDriverWait(driver,4).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,"cyrzo7gC")))
search_button_by_name.click()


# Sayfanın sonuna kadar yavaşça kaydırarak tüm ürünlerin yüklenmesini sağlayalım
scroll_pause_time = 2
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Sayfayı yavaşça aşağı kaydır
    driver.execute_script("window.scrollBy(0, 1900);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "p-card-wrppr")))

# Ürünleri listeleyelim
products = driver.find_elements(By.CLASS_NAME, "p-card-wrppr")

product_price_list = []

for product in products:
    # Ürün adını bul
    product_name = product.find_element(By.CLASS_NAME, "prdct-desc-cntnr-ttl").text
    # Ürün fiyatını bul
    product_price = product.find_element(By.CLASS_NAME, "prc-box-dscntd").text
    # Ürün adı ve fiyatını listeye ekleyelim
    product_price_list.append((product_name, product_price))

# Fiyatlara göre listeyi sıralayalım
sorted_product_price_list = sorted(product_price_list, key=lambda x: float(x[1].replace('TL', '').replace('.', '').replace(',', '.')), reverse=True)

for product in sorted_product_price_list:
    print(f"Ürün Adı: {product[0]} - Fiyat: {product[1]}")

# WebDriver'ı kapat
driver.quit()
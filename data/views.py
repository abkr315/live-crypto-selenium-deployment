
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which

# Create your views here.

def index(request):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_path = "C:\\Users\\MUHAMMADABUBAKAR\\best_movies\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.get("https://www.skrill.com/en/crypto/live-cryptocurrency-prices/")
    #html = driver.page_source
    table = driver.find_elements_by_xpath('//table[@class="skrill-live-crypto"]/tbody/tr')

    live_data = []
    for data in table:
        coins = data.find_element_by_xpath('./td[1]/a/b[2]').text
        price = data.find_element_by_xpath('./td[3]').text
        market_cap = data.find_element_by_xpath('./td[6]').text
        live_data.append({'coins':coins,'price':price, 'market_cap':market_cap})

    driver.close()
    return render(request, 'data/home.html', {'live_data': live_data})

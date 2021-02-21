import time
from selenium import webdriver

# Usuário e senha para fazer login no site da Investing
username = ""
password = ""

# Será necessário o download do chrome driver
chromedriver_path = "C:\chromedriver\chromedriver.exe"

url = "https://br.investing.com/equities/magaz-luiza-on-nm-historical-data"


# Função para configurar e abrir o navegador do Google Chrome


def open_browser(chromedriver_path):
    c_options = webdriver.ChromeOptions()

    # Em "download.default_directory" é difinido o caminho onde os arquivos serão salvos
    preferences = {"download.prompt_for_download": False,
                   "download.default_directory": r"C:\Users\...",
                   "download.directory_upgrade": True,
                   "profile.default_content_settings.popups": 0,
                   "profile.default_content_settings_values.notifications": 2,
                   "profile.default_content_settings_values.automatic_download": 1
                   }

    c_options.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(executable_path=chromedriver_path,
                              options=c_options)

    return driver


driver_1 = open_browser(chromedriver_path)

# Definir os passos a serem executados com a identificação de cada elemento html


def site_login(username, password, url, driver):
    driver.get(url)
    time.sleep(15)
    driver.find_element_by_id("onetrust-accept-btn-handler").click()
    time.sleep(15)
    driver.find_element_by_xpath("//div[@class='right']/i[@class='popupCloseIcon largeBannerCloser']").click()
    time.sleep(5)
    driver.find_element_by_link_text('Login').click()
    time.sleep(5)
    driver.find_element_by_name("loginFormUser_email").send_keys(username)
    time.sleep(1)
    driver.find_element_by_id("loginForm_password").send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='signup']/a[@class='newButton orange']").click()
    time.sleep(10)

    return driver


driver_2 = site_login(username, password, url, driver_1)

# Faz o download do arquivo csv com dados


def get_csv(driver):
    driver.find_element_by_link_text('Baixar dados').click()


get_csv(driver_2)

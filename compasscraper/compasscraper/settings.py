from shutil import which

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('/home/david/Desktop/chromedriver_linux64/chromedriver')

SELENIUM_DRIVER_ARGUMENTS = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36']

#SELENIUM_DRIVER_ARGUMENTS = ['--headless','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'] #shopee

BOT_NAME = 'compasscraper'

SPIDER_MODULES = ['compasscraper.spiders']
NEWSPIDER_MODULE = 'compasscraper.spiders'


ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 0.25
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 60
COOKIES_ENABLED = False


DOWNLOADER_MIDDLEWARES = {
  'scrapy_selenium.SeleniumMiddleware': 800,
}

# ITEM_PIPELINES = {
#     "compasscraper.pipelines.CompasscraperItem": 500,
# }

# compasscraper

# How to Setup :

    # python environment
        1. git clone https://github.com/davidhadrianus89/compasscraper.git
        2. cd compassscraper
        3. python3 -m venv scraper
        4. source scraper/bin/activate
        5. pip install -r requirements.txt

    # chrome compatibility
        1. check google chrome version
        2. download driver from https://chromedriver.chromium.org/downloads and choose your driver version regarding to installed google chrome
        3. go to file settings.py inside spiders folder
        4. change value SELENIUM_DRIVER_EXECUTABLE_PATH to your driver path


# How To Run :
    
    # Orami
        1. cd compasscraper/spiders/orami.py
        2. if use linux (ubuntu) just copy paste file to source code to change the csv path file
        3. go back to folder which contains scrapy.cfg (cd ../../)
        4. type "scrapy crawl orami --nolog" & enter
        5. wait until finish or you can stop in certain time
        6. cd compasscraper/FileCrawled/Orami/ to check the result
    
    # Tokopedia
        1. nano compasscraper/spiders/orami.py
        2. if in linux (ubuntu) just copy paste file to source code to change the csv path file
        3. go back to folder which contains scrapy.cfg (cd ../../)
        4. type "scrapy crawl tokopediasukanda --nolog" & enter
        5. wait until finish or you can stop in certain time
        6. cd compasscraper/FileCrawled/Tokopedia/ to check the result
    
    # Shopee
        1. cd compasscraper/spiders/orami.py
        2. if in linux (ubuntu) just copy paste file to source code to change the csv path file
        3. go back to folder which contains scrapy.cfg (cd ../../)
        4. type "scrapy crawl shopeesukanda --nolog" & enter
        5. wait until finish or you can stop in certain time
        6. cd compasscraper/FileCrawled/Shopee/ to check the result

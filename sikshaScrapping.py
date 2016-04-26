from selenium import webdriver
from selenium.webdriver.common.keys import Keys


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
     "(KHTML, like Gecko) Chrome/15.0.87")
browser = webdriver.PhantomJS(desired_capabilities = dcap);

url = 'https://www.zomato.com/ncr/breakfast';
browser.get(url)
print 'woring'

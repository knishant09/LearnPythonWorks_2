import urllib3
import requests,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class Browserthread():

    def __init__(self,ip, user, password, batch_type):
        self._ip = ip
        self._baseurl = "https://" + ip + ":8443"
        self._username = user
        self._password = password
        self._batch_type = batch_type
        print(self._ip, self._username, self._password, self._batch_type)
        self._sessionObj = requests.session()
        self.session_info = {}
        urllib3.disable_warnings()



    def login(self, driver):

        login_url = "%s/csBatchApp/applogin.jsp" % self._baseurl
        print(login_url)

        driver.get(login_url)
        u = driver.find_element_by_id("login_UserId")
        u.send_keys(self._username)
        p = driver.find_element_by_id("login_Password")
        p.send_keys(self._password)
        driver.find_element_by_id("login_Submit").click()

    '''''
    def Action_func(func):
        print("testing")
        time.sleep(30)
        actionChains = ActionChains(driver)
    '''''

    def _nav_batch(self, driver):
        driver.find_element_by_id("scheduledropdown-1016-inputEl").click()
        driver.find_element_by_xpath("//span[contains(text(),'{}')]".format(self._batch_type)).click()
       # self._navigate_tree(driver)

        nav_tree = ["Region", "Default Region", "DataCenter", "Default DataCenter"]

        for i in range(len(nav_tree)):
            time.sleep(5)
            actionChains = ActionChains(driver)
            actionChains.double_click(driver.find_element_by_xpath("//*[contains(text(), '{}')]".format(nav_tree[i]))).perform()
            actionChains.reset_actions()

        time.sleep(30)











if __name__ == "__main__":
    test = Browserthread("192.168.33.196", "appuser", "appuser123", "Daily")
    driver = webdriver.Chrome("D:\\Python_work\\Batchrerun_stress\\chromedriver.exe")
    test.login(driver)
    test._nav_batch(driver)
    driver.quit()








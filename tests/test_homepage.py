import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pom.homepage_nav import HomepageNav
import time
import random


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.get_box_for_close().click()
        list_len = len(homepage_nav.get_nav_links())
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validating Nav Links text'
        for i in range(int(list_len)):
            homepage_nav.get_nav_links()[i].click()
            #homepage_nav.driver.delete_cookie('ak_bmsc')
            # time.sleep(random.randint(3, 6))
        # homepage_nav.get_nav_links_by_name('Shoes').click()
        # time.sleep(5)



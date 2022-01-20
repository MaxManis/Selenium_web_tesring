from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.utils import Utils


class HomepageNav(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links = '#mainNavigationFobs>li'
        self.__close_box_but = 'closeButton'
        self.NAV_LINK_TEXT = 'Women, Men, Kids & Baby, Home, Shoes, Handbags & Accessories, Jewelry, Sale'

    def get_box_for_close(self) -> WebElement:
        return self.is_visible('id', self.__close_box_but, 'Box close Button')

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Nav Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_str(nav_links_text)

    def get_nav_links_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_elemetn_by_text(elements, name)
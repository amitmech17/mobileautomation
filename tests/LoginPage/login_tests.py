from pages.loginpage.login_page import LoginPage
import unittest
import pytest
import time


@pytest.mark.usefixtures("beforeClass")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)


    # @pytest.mark.run(order=2)
    def test_t1validLogin(self):
        self.lp.login("test@test.com","password")

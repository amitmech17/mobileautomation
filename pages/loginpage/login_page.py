from base.basepage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _email_field = "com.coalshastralive.android.app:id/emailtv"
    _password_field = "com.coalshastralive.android.app:id/passtv"
    _login_button = "com.coalshastralive.android.app:id/loginll"

    def enterEmail(self, email):
        self.sendText(email, self._email_field, "id")

    def enterPassword(self, password):
        self.sendText(password, self._password_field, "id")

    def clickLoginButton(self):
        self.clickElement(self._login_button, "id")

    def login(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

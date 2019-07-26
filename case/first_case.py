
# coding = utf-8
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
class FirstCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_email_error(self):
        email_error = self.login.login_email_error("34","user1111","1111111","test1")
        if email_error == True:
            print("注册成功，此条case执行失败")


    def test_login_username_error(self):
        username_error = self.login.login_name_error("1223@qq.com",'ss','1111111','text1')
        if username_error == True:
            print("注册成功，此条case执行失败")

    def test_login_code_error(self):
        code_error = self.login.login_code_error("1231211@qq.com", 'ssssss', '1111111', 'text1')
        if code_error == True:
            print("注册成功，此条case执行失败")

    def test_login_password_error(self):
        password_error = self.login.login_password_error("1123121@qq.com", 'sssss', '111', 'text1')
        if password_error == True:
            print("注册成功，此条case执行失败")

    def test_login_success(self):
        success = self.login.user_base("121311@qq.com", 'ssssss', '1111111', 'text1')
        if self.login.register_success()==True:
            print("注册成功")

# def main():
#     first = FirstCase()
#     first.test_login_code_error()
#     first.test_login_email_error()
#     first.test_login_password_error()
#     first.test_login_username_error()
#     first.test_login_success()

if __name__ == '__main__':
    unittest.main()


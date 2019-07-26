
# coding = utf-8
from handle.register_handle import RegisterHandle
class RegisterBusiness():

    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self,email,name,password,code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()
        self.register_h.get_register_text()

    def register_success(self):
        if self.register_h.get_register_text()==None:
            return True
        else:
            False

    # 执行操作
    def login_email_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('email_error',"请输入有效的邮箱地址") ==None:
            print("邮箱检验不成功")
            return True
        else:
            return False

    # name 错误
    def login_name_error(self,email,name,password,code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('user_name_error',"字符长度必须大于4，一个中文算2个字符") == None:
            print("用户名检验不成功")
            return True
        else:
            return False

    # 密码错误
    def login_password_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('password_error',"最少需要输入5个字符") == None:
            print("密码检验不成功")
            return True
        else:
            return False

#         验证码错误
    def login_code_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('code_text_error', "验证码错误") == None:
            print("验证码检验不成功")
            return True
        else:
            return False


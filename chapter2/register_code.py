# 注册页面封装
# coding = utf-8

from selenium import webdriver
import time
import random
from PIL import Image
from chapter2.ShowapiRequest import ShowapiRequest
driver = webdriver.Chrome()

# 浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)

#   获取元素信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefgh', 5))
    return user_info

# 获取图片

def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id('getcode_num')
    # 打印出验证码地址（元素坐标）
    # print(code_element.location)
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    # 调用保存图片
    im = Image.open(file_name)
    # 裁剪图片
    img = im.crop((left, top, right, height))
    img.save(file_name)


    # 解析图片获取验证码

def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-5", "100157", "c58c05e4469d48788594d9ae7063da63")
    r.addBodyPara("img_base64", "file_name")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    text = res.json()['showapi_res_body']['Result']
    return text # 返回信息

# 运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+ "@qq.com"
    file_name = "D:/python tupian/imooc.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    driver.close()

run_main()





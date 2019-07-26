# coding = utf-8

from selenium import webdriver
import  time
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
from PIL import Image
from chapter2.ShowapiRequest import ShowapiRequest
driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register"
           )
driver.maximize_window()
time.sleep(3)
print(EC.title_contains("注册"))

# # 随机生成用户名、邮箱
# email_element = driver.find_element_by_id("register_email")
# for i in range(5):
#     # 随机取5个数
#     # user_email = (random.sample('0123456789',5))
#     # 将列表转换为str
#     user_email =''.jion(random.sample('1234567890',5))+"@qq.com"
#     print(user_email)


#     验证码提取(引入Image包）
driver.save_screenshot("D:/python tupian/imooc.png")
code_element=driver.find_element_by_id('getcode_num')
# 打印出验证码地址（元素坐标）
print(code_element.location)
left=code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
# 调用保存图片
im = Image.open("D:/python tupian/imooc.png")
# 裁剪图片
img = im.crop((left,top,right,height))
img.save("D:/python tupian/imooc1.png")

# 调用showapirequest识别验证码
r = ShowapiRequest("http://route.showapi.com/184-5","100157","c58c05e4469d48788594d9ae7063da63" )
r.addBodyPara("img_base64", "D:/python tupian/imooc1.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
# 获取识别的验证码
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
# 输入验证码
driver.find_element_by_id('captcha_code').send_keys(text)


# # 判断元素是否可见
# # element = driver.find_element_by_class_name("controls")
# locator = (By.CLASS_NAME,"controls")
# EC.visibility_of_any_elements_located(locator)
# # 设置等待时间
# WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located(locator))


# # 获取用户信息属性值
#
# # 打印出email对话框的提示信息
# email_element = driver.find_element_by_id("register_email")
# print(email_element.get_attribute("placeholder"))
# # 打印出我输入的值
# email_element.send_keys("457381382@qq.com")
# print(email_element.get_attribute("value"))





# 元素定位
# driver.find_element_by_id("register_email").send_keys("457381382@qq.com")
# driver.find_element_by_xpath("//*[@id='register_nickname']").send_keys("豆腐的花瓣")
# driver.find_element_by_name("password").send_keys("0903shily")
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("11111")

driver.close()
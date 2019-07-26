
# python自带库文字识别，只能识别规范验证码无干扰项
# coding = utf-8
import pytesseract
from PIL import Image
from chapter2.ShowapiRequest import ShowapiRequest



# image = Image.open("D:/python tupian/imooc1.png")
# text = pytesseract.image_to_string(image)
# print(text)

# 如果有干扰项的验证码（找ShowapiRequest)
r = ShowapiRequest("http://route.showapi.com/184-5","100157","c58c05e4469d48788594d9ae7063da63" )
r.addBodyPara("img_base64", "D:/python tupian/imooc1.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()

print(res.text) # 返回信息

import requests
url = "http://yiban.turbosnail.cc/notice/apps/hncst-epidemic-prevention/backend/controllers/info_add_do.php"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0Accept: application/json, text/plain, */*"
}
data = {
    "name": "姓名",
    "stu_sno": "2020123213", #学号
    "college_name": "%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%AD%A6%E9%99%A2%EF%BC%88%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E5%AD%A6%E9%99%A2%EF%BC%89",   #学院 #中文都要URL编码
    "class_name": "21软件技术301(JAVAEE)",
    "health_item_id[0]": "1",  
    "temperature": "36.2"      #每天温度
}
body = requests.post(url, headers=header, data=data)
#print(body.text)
if "OK" in body.text:
    print("成功添加")
else:
    print("添加失败")

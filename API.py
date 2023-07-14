import requests
import time

URL = "http://192.168.3.120:8000/inference_lpr_api"
data = open("C:\\Users\\kimsh-dt01\\Downloads\\test.jpg", "rb")
t1 = time.time()
res = requests.post(URL, files={"file": data})
t2 = time.time()
print(t2 - t1, "s")
data.close()
print(res.text)

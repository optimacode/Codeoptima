import requests
import time
class Api:
    def __init__(self, api_key):
        self.api_url = 'https://medyabayim.com/api/v2'
        self.api_key = api_key

    def order(self, data):
        post = {'key': self.api_key, 'action': 'add'}
        post.update(data)
        return self.connect(post)

    def status(self, order_id):
        post = {'key': self.api_key, 'action': 'status', 'order': order_id}
        return self.connect(post)

    def multiStatus(self, order_ids):
        post = {'key': self.api_key, 'action': 'status', 'orders': ','.join(order_ids)}
        return self.connect(post)

    def services(self):
        post = {'key': self.api_key, 'action': 'services'}
        return self.connect(post)

    def balance(self):
        post = {'key': self.api_key, 'action': 'balance'}
        return self.connect(post)

    def connect(self, post):
        result = requests.post(self.api_url, data=post, headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'}, verify=True).text
        return result

api = Api(api_key='API KEY')

# Return all services
services = api.services()

# Return user balance
balance = api.balance()

# Add order
while True:
    order = api.order({'service':4441, 'link': 'sipariş linki buraya', 'quantity': 1000, 'runs': 1, 'interval': 300})
    print(f"bakiyeni {balance} ve sipariş {order}")
    time.sleep(500)
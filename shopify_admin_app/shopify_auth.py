import os
import shopify
import requests
import binascii

API_KEY = os.environ['SHOPIFY_API_KEY']
PASSWORD = os.environ['SHOPIFY_SECRET']
SHOP_NAME = os.environ['SHOPIFY_SHOP_NAME']
API_VERSION = '2023-01'

shopify.Session.setup(api_key=os.environ['SHOPIFY_API_KEY'], secret=os.environ['SHOPIFY_SECRET'])



def create_shopify_auth():
    # GET request for access token
    shop_url = "%s.myshopify.com" % (SHOP_NAME)
    state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
    redirect_uri = "http://127.0.0.1:/auth-shopify-callback"
    response = requests.get(shop_url, )




shop = shopify.Shop.current

product = shopify.Product.find("embed-your-candle")
print(product.errors)

print(product)


shopify.ShopifyResource.clear_session()

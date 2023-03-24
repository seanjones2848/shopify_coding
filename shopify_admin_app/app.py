import os
import shopify

API_KEY = os.environ['SHOPIFY_API_KEY']
PASSWORD = os.environ['SHOPIFY_SECRET']

shop_url = "https://%s:%s@SHOP_NAME.myshopify.com/admin" % (API_KEY, PASSWORD)

shopify.ShopifyResource.set_site(shop_url)



#shopify.Session.setup(api_key=os.environ['SHOPIFY_API_KEY'], secret=os.environ['SHOPIFY_SECRET'])


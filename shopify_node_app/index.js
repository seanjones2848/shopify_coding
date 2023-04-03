import '@shopify/shopify-api/adapters/node';
import { shopifyApi, ApiVersion } from '@shopify/shopify-api';
import { restResources } from '@shopify/shopify-api/rest/admin/2023-01';
import { env } from 'node:process';
import express from 'express';
import ngrok from 'ngrok';

const port = 3000
const ngrok_url = await ngrok.connect(port)

const shopify = shopifyApi({
    apiKey: env.SHOPIFY_API_KEY,
    apiSecretKey: env.SHOPIFY_SECRET,
    scopes: [
        "write_products", "read_products",
        "write_files", "read_files",
        "write_inventory", "read_inventory",
        "write_product_listings", "read_product_listings",
        "write_product_feeds", "read_product_feeds"
    ],
    hostName: ngrok_url,
    restResources
})

const app = express()

app.get('/', (req, res) => {
    res.send('Home')
})

app.listen(port, () => {
    console.log(`Listening on port ${port}`)
})

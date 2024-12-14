from odoo import models, fields, api
import requests

class BitcoinPrice(models.Model):
    _name = 'bitcoin.price'
    _description = 'Bitcoin Price'

    date = fields.Datetime(string='Date', required=True)
    price_usd = fields.Float(string='Price in USD', required=True)

    @api.model
    def fetch_bitcoin_data(self):
        """Fetch Bitcoin prices from an API and store them in the database."""
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            price_usd = data['bpi']['USD']['rate_float']
            self.create({'date': fields.Datetime.now(), 'price_usd': price_usd})

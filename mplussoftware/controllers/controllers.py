from odoo import http
from odoo.http import request
import json

class BitcoinPriceController(http.Controller):

    @http.route('/api/bitcoin/prices', auth='public', type='json')
    def get_bitcoin_prices(self):
        # Fetch Bitcoin prices from the model
        records = request.env['bitcoin.price'].search([], limit=30, order='date desc')
        data = [{
            'date': record.date.strftime('%Y-%m-%d %H:%M:%S'),
            'price_usd': record.price_usd
        } for record in records]
        return json.dumps(data)

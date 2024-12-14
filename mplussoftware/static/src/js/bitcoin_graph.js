odoo.define('bitcoin_price.graph_snippet', function (require) {
    "use strict";

    const { Component } = require('owl');
    const { useState, useEffect } = require('owl.hooks');
    const axios = require('axios');

    class BitcoinGraph extends Component {
        constructor() {
            super(...arguments);
            this.state = useState({
                labels: [],
                data: []
            });
        }

        async fetchBitcoinData() {
            try {
                const response = await axios.get('/api/bitcoin/prices'); // You will need to create an API endpoint
                const prices = response.data;
                this.state.labels = prices.map(price => price.date);
                this.state.data = prices.map(price => price.price_usd);
            } catch (error) {
                console.error('Error fetching Bitcoin data:', error);
            }
        }

        mounted() {
            this.fetchBitcoinData();
        }

        static template = 'bitcoin_price.graph_template';
    }

    return BitcoinGraph;
});

# -*- coding: utf-8 -*-
{
    'name': "mplussoftware",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web', 'website', 'hr_recruitment'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/bitcoin_graph_snippet.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'mplussoftware/static/src/js/bitcoin_graph.js',
            'mplussoftware/static/css/bitcoin_graph.scss',
            'mplussoftware/static/src/scss/random_jobs.scss',
        ],
    },
    # only loaded in demonstration mode
}


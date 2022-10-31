# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Agreement - Stock',
    'summary': 'Link picking to an agreement',
    'version': '11.0.1.0.1',
    'category': 'Contract',
    'author': 'Open Source Integrators, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/rosenvladimirov/contract',
    'depends': [
        'agreement_serviceprofile',
        'stock',
    ],
    'data': [
        'views/agreement_view.xml',
        'views/stock_view.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}

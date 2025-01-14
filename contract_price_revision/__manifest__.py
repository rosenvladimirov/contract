# Copyright 2019 Tecnativa - Vicent Cubells
# Copyright 2019 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Contract Price Revision',
    'summary': 'Easy revision of contract prices',
    'version': '11.0.1.0.1',
    'category': 'Contract',
    'author': 'Tecnativa, '
              'Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'website': 'https://github.com/rosenvladimirov/contract',
    'depends': [
        'contract',
    ],
    'data': [
        'views/contract_line.xml',
        'wizards/contract_price_revision_views.xml',
    ],
    'installable': True,
}

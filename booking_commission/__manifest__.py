# -*- coding: utf-8 -*-
{
    'name': "Booking Commission",

    'summary': """
        Booking Commission""",

    'description': """
        - Apply a field in Sales, Purchase and Invoice module to calculate discount after the order lines are inserted.
        - Discount values can be given in two types:
           
           - In Percent
           - In Amount

        - Can be enabled from (**Note** : Charts of Accounts must be installed).
             
             Settings -> general settings -> invoice 
        
        - Maintains the global tax entries in accounts specified by you (**Note** : To see journal entries in Invoicing: (in debug mode) 
             
             Settings -> users -> select user -> Check "Show Full Accounting Features")
        
        - Maintains the global discount entries in accounts specified by you.
        - Label given to you will be used as name given to discount field.
        - Also update the report PDF printout with global discount value.
    """,

    'author': "Usman",
    'website': "cargotracker",
    'images': ['static/description/main.png'],
    'license': 'LGPL-3',
    'category': 'Purchase Management',
    'version': '1.2.0',

    'depends': ['base', 'cargo_tracker',],

    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_commission.xml',
        'views/booking_commission.xml',

    ],

}

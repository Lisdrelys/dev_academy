# -*- coding: utf-8 -*-

{ 
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage training""",
    
    'description': """Academy Module to manage training:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '1.0',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
    ],
    
    'demo': [
        'demo/academy_demo.xml',
    ],   
    
}
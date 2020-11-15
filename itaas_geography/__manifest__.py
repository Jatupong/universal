# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Thailand Geography',
    'version' : '13.0.1.0',
    'depends' : ["base", "mail", "contacts"],
    'author' : 'ITAAS',
    'category': 'ITAAS',
    'description': """
Feature: 
Thailand Geography
    """,
    'website': 'http://www.itaas.co.th',
    'depends': ['itaas_partner_detail_address','base'],
    'data': [

        'data/province_data.xml',
        'data/district_data.xml',
        'data/sub_district_data.xml',
        'security/security.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

{
    "name" : "Real Estate",
    "version": "1.0",
    "autor": "Walt28",
    "description": """
        Real estate module to show available properties
    """,
    "category": "",
    "data": [
        #SECURITY
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        #VIEWS
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        #MENU
    ],
    "demo": [
        'demo/demo.xml',
    ],
    "depends" : ["base"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

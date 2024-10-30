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

        # DATAS Files
        'data/property_type_datas.xml',
        'data/estate.property.type.csv'
    ],

    "demo": [
        'demo/property_demos.xml',
        'demo/property_tag_demos.xml',
    ],

    "assets" : {
        "web.assets_backend": [
            'estate/static/src/css/style.css',
        ],
    },

    "depends" : ["base", "mail"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

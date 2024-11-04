{
    "name" : "Real Estate",
    "version": "1.0",
    "autor": "Walt28",
    "description": """
        Real estate module to show available properties
    """,
    "category": "",

    "data": [
        # SECURITY
        'security/res_groups.xml',
        'security/model_access.xml',
        'security/ir.model.access.csv',
        # VIEWS
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        # TEMPLATE
        'views/property_web_template.xml',
        # MENU

        # DATAS Files
        'data/property_type_datas.xml',
        'data/estate.property.type.csv',
        'data/mail_template.xml',
        
        # Reports
        'report/report_template.xml',
        'report/property_report.xml',
    ],

    "demo": [
        'demo/property_demos.xml',
        'demo/property_tag_demos.xml',
    ],

    "assets" : {
        "web.assets_backend": [
            'estate/static/src/css/style.css',
            'estate/static/src/js/my_custom_tag.js',
            'estate/static/src/xml/my_custom_tag.xml',
        ],
    },

    "depends" : ["base", "mail"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

{
    "name" : "Real Estate",
    "version": "1.0",
    "autor": "Walt28",
    "description": """
        Real estate module to show available properties
    """,
    "category": "",
    "data": [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/menu_items.xml',
    ],
    "demo": [
        'demo/demo.xml',
    ],
    "depends" : ["base"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
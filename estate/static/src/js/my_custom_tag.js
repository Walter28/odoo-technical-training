/** @odoo-module **/    // first tell odoo this is an odoo module file and we wan use owl
import { registry } from '@web/core/registry';
import { Component } from '@odoo/owl'; // this is for odoo 17

//ALL OF THIS IS FOR ODOO 16.0

//odoo.define('estate.CustomAction', function (require) {
//    "use strict"
//
//    var AbstractAction = require('web.AbstractAction')
//    var core = require('web.core')
//
//    var CustomAction = AbstractAction.extend({
//        template: "CustomActions",
//        start: function () {
//            console.log('Action')
//        }
//    })
//
//    core.action_registry.add("custom_client_action", CustomAction)
//
//
//})


//HERE DOWN SAME VERSION FOR ODOO 17.0

class MyCustomAction extends Component {}
MyCustomAction.template = "CustomActions";

registry.category('actions').add(
    "custom_client_action",
    MyCustomAction
);

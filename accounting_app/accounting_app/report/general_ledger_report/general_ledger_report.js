// Copyright (c) 2016, Mrunmay D and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["General Ledger Report"] = {
	"filters": [
		{
            "fieldname":"party",
            "label": __("Party"),
            "fieldtype": "Link",
            "options": "Party",
            "default": frappe.defaults.get_user_default("Party")
        },
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
			"reqd": 1,
			"width": "60px"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1,
			"width": "60px"
		},
	]
};

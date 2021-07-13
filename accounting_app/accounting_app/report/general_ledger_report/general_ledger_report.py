# Copyright (c) 2013, Mrunmay D and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _, _dict
from frappe.utils import getdate, flt
import frappe
from frappe.utils import datetime

def execute(filters=None):
    if not filters:
        return ([], [])

      # validations starts here

    if filters.from_date > filters.to_date:
        frappe.throw(_('From Date must be before To Date'))

      # validations ends here   

    columns = get_columns()
    data = get_data(filters)

    return (columns, data)


def get_data(filters):
    if (filters.get('party') or filters.get('to_date') or filters.get('from_date')):        
        query1 = 'select * from `tabParty` {} order by date desc'.format(conditions(filters))

        data = frappe.db.sql(query1, filters, as_dict=1)
        return data
    else:        
        query1 = 'select * from `tabParty` order by date desc'
        data = frappe.db.sql(query1, as_dict=1)

    return data

def conditions(filters):    
    party = filters.get('party')
    from_date = filters.get('from_date')
    to_date = filters.get('to_date')
    conditions = []

    if not (to_date and from_date):
        from_date = datetime.MINYEAR
        to_date = datetime.datetime.today()
    else:
        conditions += ["date >= '{}' and date <= '{}'".format(from_date, to_date)]       
    
    if filters.get('party'):
        conditions += ["party_name = '{}'".format(party)]

    where_conditions = 'where {}'.format(' and '.join(conditions))    
    return where_conditions

def get_columns():
    columns = [
        {
        'label': 'Party',
        'fieldname': 'party_name',
        'fieldtype': 'Link',
        'options': 'Party',
        },{
        'label': 'Balance',
        'fieldname': 'account_balance',
        'fieldtype': 'Data',
        'options': 'Balance',
        }]

    return columns



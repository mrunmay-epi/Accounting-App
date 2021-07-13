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

    columns = get_columns()
    data = get_data(filters)

    return (columns, data)


def get_data(filters):
    if (filters.get('party_account') or filters.get('to_date') or filters.get('from_date')):        
        query = 'select * from `tabPayment Entry` {} order by date desc'.format(conditions(filters))
        data = frappe.db.sql(query, filters, as_dict=1)
        return data
    else:        
        query = 'select * from `tabPayment Entry` order by date desc'
        data = frappe.db.sql(query, as_dict=1)

    return data    


def conditions(filters):    
    account = filters.get('party_account')
    from_date = filters.get('from_date')
    to_date = filters.get('to_date')

    conditions = []

    if not (to_date and from_date):
        from_date = datetime.MINYEAR
        to_date = datetime.datetime.today()
    else:
        conditions += ["date >= '{}' and date <= '{}'".format(from_date, to_date)]       
    
    if filters.get('party_account'):
        conditions += ["account_details = '{}'".format(account)]


    where_conditions = 'where {}'.format(' and '.join(conditions))    
    return where_conditions


def get_columns():
    columns = [
        {
        'label': 'Account',
        'fieldname': 'party_account',
        'fieldtype': 'Link',
        'options': 'Party Account',
        'width': 180,
        }, {
        'label': 'Balance',
        'fieldname': 'balance',
        'fieldtype': 'Data',
        'options': 'Balance',
        },{
        'label': 'Transaction Date',
        'fieldname': 'date',
        'fieldtype': 'Transaction Date',
        }]

    return columns




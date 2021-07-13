# -*- coding: utf-8 -*-
# Copyright (c) 2021, Mrunmay D and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document



class PurchaseInvoice(Document):
    def on_submit(self):
        exists = frappe.db.exists('Item',
                                  {'quantity': ('<', self.quantity)})
        
        if exists:
            frappe.throw('No item available')        
        Payment_entry = frappe.new_doc('Payment Entry')
        Payment_entry.date = self.date
        Payment_entry.paid_from = self.credit_to
        Payment_entry.payment_amount = self.total_amount
        Payment_entry.payment_transaction_id = self.purchase_invoice_id
        Payment_entry.save()
        Payment_entry.submit()


from odoo import models
from datetime import datetime


class EstateProperty(models.Model):
    _inherit = "estate.property"
    def Sold_action(self):
        for prop in self:
            print(" reached================================================================= ")
            self.env["account.move"].create(
                {
                    "name" : prop.name,
                    "partner_id" : prop.partner_id.id,
                    "move_type" : "out_invoice",
                    "invoice_date" : datetime.now(),
                    "invoice_line_ids" : [
                        (
                            0,
                            0,
                            {
                                'name' : prop.name,
                                'quantity' :  1.0,
                                'price_unit' : prop.selling_price * 60.0 / 100.0,
                            },
                        ),
                        (
                            0,
                            0,
                            {
                                'name' : "Administrator fees",
                                'quantity' : 1.0,
                                'price_unit' : 100.0,
                            },
                        ),

                    ],
                }
            )
        return super().Sold_action()
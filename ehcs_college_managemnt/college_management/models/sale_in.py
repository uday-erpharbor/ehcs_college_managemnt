from odoo import models,fields,api


class Saleinheritefin(models.Model):
    _inherit = "sale.order"


    amount = fields.Float("Amount")
    total_amount = fields.Float("Total Amount",compute="compute_onto")
    config = fields.Boolean("Con")



    @api.depends("amount")
    def compute_onto(self):
        fieldname = self.env['ir.config_parameter'].sudo().get_param('college_management.is_teacher')
        fieldname2 = self.env['ir.config_parameter'].sudo().get_param('college_management.amount')
        self.config = fieldname
        print("---------------------",fieldname,fieldname2,self.config)
        if fieldname:
            self.total_amount = self.amount * float(fieldname2)
        else:
            self.total_amount = self.amount
        
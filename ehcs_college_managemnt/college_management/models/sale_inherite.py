from odoo import models,fields,api


class Saleinheritefi(models.TransientModel):
    _inherit = "res.config.settings"


    is_teacher = fields.Boolean("Teacher",config_parameter="college_management.is_teacher")
    amount = fields.Float("Amount",config_parameter="college_management.amount")
    
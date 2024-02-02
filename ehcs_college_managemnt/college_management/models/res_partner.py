from odoo import models,fields


class Contacts(models.Model):
	_inherit = "res.partner"


	is_teacher = fields.Boolean("Is Teacher")
	is_student = fields.Boolean("Is Student")
	uday = fields.Char("Uday")






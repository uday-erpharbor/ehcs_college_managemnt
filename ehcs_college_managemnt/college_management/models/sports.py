from odoo import models,fields

class Sports(models.Model):
	_name = "sport.sport"
	_description = "College Sports department"


	name= fields.Char("game")
	form_ids = fields.One2many(
		comodel_name="sport.form",
		inverse_name="sport_info_id",
		string="Form"
		)
	







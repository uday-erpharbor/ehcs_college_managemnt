from odoo import models,fields

class Sports(models.Model):
	_name = "sport.sport"
	_description = "College Sports department"


	name= fields.Char(string="game")
	form_ids = fields.One2many(
		comodel_name="sport.form",
		inverse_name="sport_info_id",
		string="Form"
		)

	def action_create_student(self):
		self.write({'form_ids':
			[
			(
				0, 0, {
				'name' : 'Bhavin',
				'city' : 'Ahemedabad'
				}				
				),
			(
				0, 0, {
				'name' : 'Hiyesh',
				'city' : 'Ahemedabad'
				}				
				),
			]

			})
	







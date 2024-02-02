from odoo import models,fields,api

class teacher(models.Model):
	_name = "teacher.information"
	_description = "Teacher's information"
	_inherit = ['mail.thread', 'mail.activity.mixin']



	name = fields.Char("Teacher Name",tracking=True)
	student_ids = fields.One2many("college.student","t_id",string="students")
	gender = fields.Selection([('male', 'Male'),('female', 'Female'),("other","Other"),], 
		string='Gender',)
	subject_id = fields.Many2many(comodel_name="college.subject",
		relation="teacher_subject",
		column1="s_t",
		column2="t_s",
		string="Subject")
	# age = fields.Integer("Age")
	partner = fields.Char("Partner name")
	master = fields.Integer("How many % master in your subject")
	progress = fields.Integer(" master in my subject")

	@api.onchange("master")
	def _onchange_master(self):
		self.progress = self.master

	phd = fields.Boolean("PHD in Subject",tracking=True)
	year = fields.Char("Which Year")




	

	
	



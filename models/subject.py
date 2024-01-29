from odoo import models,fields


class Subject(models.Model):
	_name="college.subject"
	_description="College Subjects"


	name = fields.Char("Subject name")
	mark = fields.Integer("Mark")
	




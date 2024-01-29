# from odoo import models,fields,api,_
# from datetime import datetime,date



# class Exam(models.Model):
# 	_name = "exam.exam"
# 	_description = "Exam Information"



# 	student_id = fields.Many2one("college.student","Student Name")
# 	data = fields.Date("Date")






# class Exam(models.Model):
# 	_name = "exam.exam.line"
# 	_description = "Exam Information"



# 	subject_id = fields.Many2one("college.subject","Student Name")
# 	mark = fields.Float("Mark")



# 	@api.onchange("subject_id")
# 	def onchange_mark(self):
# 		for mmarks
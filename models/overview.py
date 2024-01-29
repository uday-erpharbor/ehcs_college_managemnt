from odoo import models,fields


class Information(models.Model):
	_name ="about.college"
	_description ="Subject in college"


	name = fields.Char("Name",default='Shree P.K.M College',readonly=True,width="200")
	since = fields.Char("Since",default="1985",readonly=True)
	city = fields.Char("City",default="Junagadh",readonly=True)
	uni = fields.Char("Univercity",default="B.K.N.M.U",readonly=True)
	



from odoo import models,fields,api





class SubjectWizard(models.TransientModel):
    _name = "subject.wizard"
    _description = "subject wizard"


    name = fields.Char("Subject")
    t_id = fields.Many2one("teacher.information"
                            ,string="Realated Teacher")

   






    def print_excel_report(self):
        print("hello")


    
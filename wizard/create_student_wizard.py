from odoo import models,fields,api





class SubjectWizard(models.TransientModel):
    _name = "student.wizard"
    _description = "Student wizard"



    student_id = fields.Many2one('college.student',"Student")




    def print_excel_report(self):
        pass


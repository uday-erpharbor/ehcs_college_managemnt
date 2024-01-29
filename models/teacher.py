from odoo import models,fields,api

class teacher(models.Model):
    _name = "teacher.information"
    _description = "Teacher's information"
    


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
    email = fields.Char()

    @api.onchange("master")
    def _onchange_master(self):
        self.progress = self.master

    phd = fields.Boolean("PHD in Subject",tracking=True)
    year = fields.Char("Which Year")
    student_count = fields.Integer("Student",compute="count_student")

    def count_student(self):
        for record in self:
            a = self.env['college.student'].search_count([("t_id",'=',record.name)])
            print("-----------------------------------",a)
            record.student_count = a



    def create_subject(self):
        res = {
            'name': 'Subject',
            'type': 'ir.actions.act_window',
            'res_model': 'subject.wizard',
            'view_id': self.env.ref('college_management.subject_wizard').id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',       
            'context': {
              'default_name': self.name,
            } 
        }
        print("\n\n\n\nresLLLLLLLLLLLLLLLLLLLLLL",res)
        return res


    def student_smart_button(self):
        return{
        'type':'ir.actions.act_window',
        'name':'student',
        'res_model':'college.student',
        'view_mode':'tree,form',
        'domain':[('t_id','=',self.name)],
        'target':'current',

        }

#not for use only for reading purpose
    def demo_1(self):
        a = self.env['res.partner'].search([])
        print("------------------------",a.mapped('name'))
        print("------------------------",a.sorted('email'))
        print("------------------------",a.filtered('is_teacher'))
        






    

    
    



from odoo import models,fields


class Contacts(models.Model):
    _inherit = "res.partner"


    is_teacher = fields.Boolean(string="Is Teacher")
    is_student = fields.Boolean("Is Student")
    subject_ids = fields.Many2many(comodel_name="college.subject",string="Subject")


    # def action_update_subject(self):
    #     print("hello uday")





    def action_update_subject(self):
        subj_obj = self.env['college.subject']
        subjs = subj_obj.search([('name', 'ilike', 'java')])
        print ("\n\n.subjssubjs    ", subjs)
        for partner in self:
            for subj in subjs:
                partner.write({'subject_ids': [(1, subj.id, {'mark': '123'})]})
        return True


    def action_remove_subject_database(self):
        subj_obj = self.env['college.subject']
        subjs = subj_obj.search([('name','ilike','python')])
        print("fsjfjf",subjs)
        for partner in self:
            for subj in subjs:
                partner.write({'subject_ids': [(2,subj.id)]})
        return True

    def action_remove_subject(self):
        subj_obj = self.env['college.subject']
        subjs = subj_obj.search([('name', 'ilike', 'java')])
        print ("\n\n.subjssubjs    ", subjs)
        for partner in self:
            for subj in subjs:
                partner.write({'subject_ids': [(3, subj.id)]})
        return True

    def action_add_subject(self):
        subj_obj = self.env['college.subject']

        subjs = subj_obj.search([('name', 'ilike', 'python')])
        print ("\n\n.subjssubjs    ", subjs)
        for partner in self:
            for subj in subjs:
                partner.write({'subject_ids': [(4, subj.id)]})
        return True

    def action_remove_all_subject(self):
        for partner in self:
            partner.write({'subject_ids': [(5, 0, 0)]})
        return True

    def action_replace_subject(self):
        subj_obj = self.env['college.subject']
        subjs = subj_obj.search([('name', 'ilike', 'python')])
        print ("\n\n.subjssubjs    ", subjs)
        for partner in self:
            partner.write({'subject_ids': [(6, 0, subjs.ids)]})
        return True
    





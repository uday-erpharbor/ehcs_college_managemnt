from datetime import datetime, timedelta
from odoo import models, fields, api


class Salary(models.Model):
    _name = "salary.salary"
    _description = "Teacher Salary"
    _order = "salary desc"
    

    name = fields.Many2one(comodel_name="teacher.information",string="Teacher Name")
    # salary = fields.Integer(string="Salary",default="1000")
    come_date = fields.Date(string='Come Date', required=True)
    go_date = fields.Date(string='Go Date')

    @api.depends('come_date', 'go_date','leave')
    def _compute_work_duration(self):
        self.work_duration = 0
        for worker in self:
            if worker.come_date and worker.go_date:
                delta = worker.go_date - worker.come_date
                print("=============",type(delta))
                worker.work_duration = delta.days - worker.leave

    work_duration = fields.Integer(string='Work Duration (days)', compute='_compute_work_duration')

    @api.depends('work_duration')
    def _compute_salary(self):
        for worker in self:
            worker.salary = worker.work_duration  * 350 

    salary = fields.Float(string='Salary', compute='_compute_salary', store=True)
    leave = fields.Integer(string="Your Leave Days",required=True)
   





    




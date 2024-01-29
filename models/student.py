from odoo import models,fields,api,_
from datetime import datetime,date
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


class students(models.Model):
    _name = "college.student"
    _description = "student information"


    name = fields.Char(string="Student Name",help="Enter the Name")
    reference = fields.Char(string= "Order Reference",required=True,copy=False,readonly=True,default=lambda self: ('New'))
    mark = fields.Float(string="Mark")
    roll_number = fields.Integer(string="Roll Number",default=0,)
    birth_date = fields.Date(string="Date of Birth",required=True,default=datetime.now())
    photo = fields.Image(string="Student Image")
    fees = fields.Integer(string="fees")
    field = fields.Selection([("f.y","F.Y "),("s.y","S.Y "),("t.y","T.Y")],string="Year",required="1")
    course = fields.Many2one(comodel_name="course.course",string="Course")
    t_id = fields.Many2one("teacher.information",string="Realated Teacher")
    subject_ids = fields.Many2many(comodel_name="college.subject",
        relation="stu_sub_rel",
        column1="stud_id",
        column2="sub_id",
        string="subject",)

    email= fields.Char("Student e-mail")
    student = fields.Boolean()
    add = fields.Text("Addres")
    scholrship = fields.Char("Scholrship")
    bsc = fields.Char()
    # --------------------------------------------------
    spuid = fields.Integer("Spu Id")
    grno = fields.Integer("GR NUMBER")
    password = fields.Char("Id Password")
    admission = fields.Integer("Admission Number")
    state = fields.Selection([
    ('andhra_pradesh', 'Andhra Pradesh'),
    ('west_bengal', 'West Bengal')
], string='State')
# ----------------------------------------------------------------
    gender = fields.Selection([('male', 'Male'),('female', 'Female'),("other","Other")], string='Gender',compute="onchange_t_id")
    pg = fields.Boolean("You are living in Pg or Hostel")
    rent = fields.Integer("Rent")
    job = fields.Boolean("Part Time job")
    salary = fields.Integer("Your Salary")
    state = fields.Selection([("draft","Draft"),("confirm","Confirm"),("done","Mark as Done"),("cancel","Cancel")],default="draft")


    @api.onchange("gender") 
    def _api_onchange(self):
        if self.gender == "female":
            self.pg = True
        else:
            self.pg = False


    @api.onchange("mark")
    def _onchange_mark(self):
        if self.mark > 100:
            print("---=++++++++")
            raise ValidationError("please enter valid marks")

    _sql_constraints=[
    ("roll_number_unique","unique(roll_number)","oh sorry")
    ]


    internship = fields.Char("Intersnhip")



    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = date.today()
                delta = relativedelta(today, record.birth_date)
                record.age = delta.years
          

    def cancel_button(self):
        self.state = "cancel"

    def coferm_button(self):
        self.state = "confirm"


    def mark_as_done(self):
        self.state = "done"

    def set_to_draft(self):
        self.state = "draft"



    @api.onchange('t_id')
    def onchange_t_id(self):
        self.gender = self.t_id.gender



    # @api.model
    # def create(self,vals):
    #     if vals.get('reference',_('New')) == _('New'):
    #         vals['reference'] = self.env['ir.sequence'].next_by_code('college.student') or _('New')
    #     res = super(students, self).create(vals)
    #     return res


    # def write(self,vals):
    #     print("/n/n/n/n/nself::::::::",self)
    #     print("/n/n/n/n/vals::::::::",vals)
    #     if vals.get('state') == ('confirm'):
    #         vals['t_id'] = False
    #     else:
    #         vals['t_id'] = 14 

    #     res = super(students, self).write(vals)
    #     return res



    # def copy(self, default=None):
    #     print("\n\nCopy is called.........")
    #     name = super(students, self).copy(default={'name': self.name+"(copy)"})
    #     print("new_fees......    ", name)
    #     return name
        

    # @api.onchange("t_id",)
    # def t_id_search(self):
    #     for record in self:
    #         b = record.name
    #         a = self.env['teacher.information'].search_count([('name',)])
    #         print("----------------------",a,b)



    def sport_form_create_on_button(self):
        self.env["sport.form"].create(
        {
            'name':self.name,
        
        })


    def mail_leave(self):
        template = self.env.ref('college_management.send_leave_mail')
        print("-----------",template.name)
        for student in self:
            template.send_mail(student.id,force_send=True)
        return True




    

   



    

    


    







        
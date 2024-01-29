from odoo import models,fields,api,_
from odoo.exceptions import UserError


class Personalinfo(models.Model):
    _name="sport.form"
    _description="personal info"


    name = fields.Char("Name")
    ref = fields.Char(string="refernce",required=True,readonly=True,copy=False,default=lambda self:("New"))
    height= fields.Float("Height")
    gender = fields.Selection([("male","Male"),("female","Famale")])
    city = fields.Char("City")
    handicap = fields.Boolean("Handicap")
    dob = fields.Date("Birth Date")
    sport_info_id = fields.Many2one("sport.sport","Sport information")
    runing = fields.Selection([('5km','5 km/hour'),('10km','10 km/hour'),('more',"More Than 10 km/hour")],string="Runing Capacity")
    government_assistance = fields.Boolean()
    assistance = fields.Char(string="Assistance")
    nationality = fields.Selection([("indian","INDIAN"),("other","OTHER COUNTRY")])
    which_country = fields.Char("Which country")
    passport = fields.Integer("Passport Number")
    visa = fields.Char("Your Visa Id")
    state = fields.Selection([("done","Done"),("edit","Edit")])
    mobile = fields.Char("Mobile Number")
    count= fields.Integer()



    @api.model
    def create(self,vals):
        if vals.get('ref',_('New')) == _('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('sport.form') or _('New')
        res = super(Personalinfo, self).create(vals)
        return res


    def write(self,vals):
        if vals.get("gender") == ("female"):
            vals['runing'] = '5km'

        res = super(Personalinfo, self).write(vals)
        return res

   
    def unlink(self):
        print("\n\nwrite is called.........    ", self)
        for student in self:
            if student.runing == '10km':
                raise UserError('Record can not be deleted')
        return super(Personalinfo, self).unlink()


    def done_button_in_tree(self):
        self.state = "done"

    def edit_button_in_tree(self):
        self.state = "edit"



    def name_get(self):
        result = []
        for account in self:
            name = account.ref + ' ' + account.name
            result.append((account.id, name))
        return result


    def excel_report(self):
        data = {
            'model_id' : self.id,
            'date' : self.dob,
            'student' : self.name,
        }
        return {
        'type' : 'ir.actions.report',
        'data' :{
            'model' : 'sport.form',
            'output_format' :'xlsx',
            'report_name' : 'Sport Report',
            'report_type' : 'xlsx',
            }
        }

    








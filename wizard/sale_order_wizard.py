from odoo import models,fields,api





class Saleorderwizard(models.TransientModel):
    _name = "sale.wizard"
    _description = "Sale Wizard"


    template_id = fields.Many2one(comodel_name="product.template",string="Template")
    attribute_id = fields.Many2one(comodel_name="product.attribute",string="Attribute")
    value_ids = fields.Many2many(comodel_name="product.attribute.value",string="Value", domain="[('attribute_id', '=', attribute_id)]")


    # @api.onchange('attribute_id')
    # def update_many2many_domain(self):
    #     domain = [('attribute_id', '=', self.attribute_id.id)]
    #     print("----------------",self.attribute_id.id)
    #     return {'domain': {'value_ids': domain}}


    def done_button(self): 
        filtered_records = self.template_id.attribute_line_ids.filtered(lambda l : l.attribute_id.id == self.attribute_id.id)
        print("\n\n\n\n\nfilterred_recird:::::",filtered_records)
        if filtered_records:
            filtered_records.write({'value_ids': [(4, self.value_ids.id)]})
        else:
            self.template_id.write({
            'attribute_line_ids': [
            (0, 0, {
                'attribute_id': self.attribute_id.id,
                'value_ids': self.value_ids.ids
                })]
            })
        






    

                
              

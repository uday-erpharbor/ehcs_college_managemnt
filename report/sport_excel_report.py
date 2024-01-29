from odoo import models

class PartnerXlsx(models.AbstractModel):
    _name = 'report.college_management.sport_excel_report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        report_name = ""
        # sheet = workbook.add_worksheet(report_name[:31])
        bold = workbook.add_format({'bold': True, 'align': 'center'})
        format_1 = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': 'yellow'})
        sheet = workbook.add_worksheet(partners.name)
        sheet.merge_range(4,7,4,7+2 ,'ID CARD', format_1)
        row=5
        col=7
        sheet.write(row, col, 'Name', bold)
        sheet.write(row, col+1, 'City', bold)
        sheet.write(row, col+2, 'Nationality', bold)
        row+=2
        sheet.set_column('J:J',15)      #this field is set a by default size of cell in excel report
        for obj in partners:
            print("-----------",obj)
            for excel in obj.form_ids:
                print("\n\n\n\nexcel::::",excel)
                sheet.write(row,col,excel.name)
                sheet.write(row,col+1,excel.city)
                sheet.write(row,col+2,excel.nationality)
                row += 1



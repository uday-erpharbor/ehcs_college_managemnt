from odoo import models
import base64
import io


class Studentcard(models.AbstractModel):
    _name = 'report.college_management.student_excel'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, students):
        print("---------------",students)
        sheet = workbook.add_worksheet('Excel Report')
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold':True,'align':'center','bg_color':'yellow'})
        row=1
        col=1
        sheet.set_column('B:B',25)      #this field is set a by default size of cell in excel report
        for obj in students:
            for excel in obj:
                row+=1
                sheet.merge_range(row, col,row,col+1 ,'ID CARD', format_1)

                row+=1
                if excel.photo:
                    student_image = io.BytesIO(base64.b64decode(excel.photo))
                    sheet.insert_image(row,col,'image.png',{'image_data':student_image,'x_scale':0.5,'y_scale':0.5})

                    row+=9

                row+=1
                sheet.write(row, col, 'Name', bold)
                sheet.write(row, col + 1, excel.name)
                row+=1
                sheet.write(row, col , 'Roll Num', bold)
                sheet.write(row, col + 1, excel.roll_number)
                row+=1
                sheet.write(row, col , 'Teacher', bold)
                sheet.write(row, col + 1, excel.t_id.name)

                row+=2



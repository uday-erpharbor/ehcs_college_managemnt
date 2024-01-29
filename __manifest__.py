{
    "name" : "College management",
    "author" : "Erpharbor",
    "version" : "1.2",
    "summary" : "Student Information",
    "website" : "erpharbor.com",
    "description" : "college student information",
    'depends': ['report_xlsx', 'crm','sale_management'],
    "category" : "Edution",
    "data" : [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/email_template_dataa.xml",
        "data/demo_data.xml",
        "wizard/create_subject_wizard.xml",
        "wizard/create_student_wizard.xml",
        "wizard/sale_order_wizard.xml",
        "views/overview.xml",       
        "views/student_info.xml", 
        "views/teacher_info.xml",
        "views/sports.xml",
        "views/sport_form.xml",
        "views/teacher_salary.xml",
        "views/course.xml",
        "views/subject.xml",
        "views/menu_view.xml",
        "views/res_partner_view.xml",
        'report/student_id_card_report.xml',
        'report/sport_form_report.xml',
        'report/teacher_salary.xml',
        'report/report.xml', 
        # "views/exam.xml",
       
       
        
    ],
    "demo" :[

    ],
    "license" : "LGPL-3",
    
}
{
    "name" : "College management",
    "author" : "Erpharbor",
    "version" : "17.0.1.0.0",
    "summary" : "Student Information",
    "website" : "erpharbor.com",
    "description" : "college student information",
    'depends': ['contacts','sale_management'],
    "category" : "Edution",
    "data" : [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/demo_data.xml",
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
        "views/sale_in.xml",
        "views/sale_inherite.xml",
        "report/student_id_card_report.xml",
        "report/report.xml",
    ],
    "demo" :[

    ],
    "license" : "LGPL-3",
    
}
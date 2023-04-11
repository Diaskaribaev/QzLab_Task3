from odoo import api, fields, models

class UniversityStudent(models.Model):
    _name = "university.student"
    _description = "University Students"


    student_name = fields.Char(string= 'Name')
    university_name_id = fields.Many2one('university.organization',string='University Name')
    speciality_name  = fields.Many2one('university.speciality',string = 'Speciality name')
    year_of_birth = fields.Integer(string= 'birth year')


from odoo import api, fields, models

class UniversityOrganization(models.Model):

    _name = "university.organization"
    _description = "University Organization"


    name = fields.Char(string= 'Name')
    found_year = fields.Integer(string= 'foundation year')
    # specialities = fields.One2many('university.speciality','university_name_id',string = 'specialities ')
    students = fields.One2many('university.student','university_name_id',string = 'students ')


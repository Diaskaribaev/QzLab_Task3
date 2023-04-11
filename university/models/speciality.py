from odoo import api, fields, models

class UniversityOrganization(models.Model):
    _name = "university.speciality"
    _description = "University's specialities"


    name = fields.Char(string= 'Speciality name')



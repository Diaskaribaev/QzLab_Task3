from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal


class University(http.Controller):
    @http.route('/university/universities', auth='public',website= True)
    def display_university(self, **kw):
        organizations = http.request.env['university.organization'].search([])
        return http.request.render('university.organizationsss',{
            'organizations' : organizations,
        })

    @http.route('/university/<model("university.organization"):organization>/', auth='public',website= True)
    def display_name(self,**kw):
        student = http.request.env['university.student'].search([])
        return http.request.render('university.university-detail',{'students': student})


    @http.route('/university/my', auth='public',website= True)
    def UniversityListView(self,**kw):
        university_obj = http.request.env['university.organization'].search([])
        return http.request.render("university.university_list_view",{
            'organizations': university_obj
        })



# -*- coding: utf-8 -*-
import datetime

from openerp import http
from openerp.exceptions import AccessError
from openerp.http import request
import base64
import werkzeug
from openerp.addons.tour_operator.booking import  BookingTariff


class activity(http.Controller):
    @http.route(['/activity'], type='http', csrf=False, auth='user', website=True)
    def my_controller_method(self, id, pricelist, redirect=None, **post):
        partner = request.env.user.partner_id
        res_company = request.env.user.company_id
        res_activity = request.env['product.product'].search([
            ('active','=','TRUE'),
            ('id','=',id)

        ])
        res_pricelist = request.env['booking.tariff'].search([
            ('active','=','TRUE'),
            ('partner_ids.id','=',partner.id),
            ('activity_tariff_line_ids.id','=',pricelist)

        ])
        if res_activity:
            filterActivity = res_activity
            filterPricelist = res_pricelist
            if partner.user_id:
                sales_rep = partner.user_id
            else:
                sales_rep = False
            values = {
                'sales_rep': sales_rep,
                'company': request.website.company_id,
                'user': request.env.user,
                'date': datetime.date.today().strftime('%Y-%m-%d'),
                'filterActivity': filterActivity,
                'filterPricelist':filterPricelist,
                'pricelist_id':pricelist,
                'res_company': res_company
            }
            return request.website.render("pricelist_web.activity_view", values)
        else:
            return request.render('website.404')

class pricelist_filter(http.Controller):
    @http.route(['/search_pricelist'], type='http', csrf=False, auth='public', website=True)
    def my_controller_method(self, date1, date2, redirect=None, **post):
        partner = request.env.user.partner_id
        res_company = request.env.user.company_id
        res_pricelist = request.env['booking.tariff'].search([
            ('active','=','TRUE'),
            ('partner_ids.id','=',partner.id),
            ('date_start','<',date2),
            ('date_end','>',date1)

        ])
        filterPricelist = res_pricelist
        lodging_field = False
        if 'lodging_pricelist_ids' in request.env['booking.tariff']._fields:
            lodging_field = True


        if partner.user_id:
            sales_rep = partner.user_id
        else:
            sales_rep = False
        values = {
            'sales_rep': sales_rep,
            'company': request.website.company_id,
            'user': request.env.user,
            'date': datetime.date.today().strftime('%Y-%m-%d'),
            'filterPricelist': filterPricelist,
            'date1': date1,
            'date2':date2,
            'lodging_field':lodging_field,
            'res_company': res_company
        }
        return request.website.render("pricelist_web.pricelist_filtered", values)
        #lodging controller
class lodging(http.Controller):
    @http.route(['/lodging'], type='http', csrf=False, auth='user', website=True)
    def my_controller_method(self, pricelist, redirect=None, **post):
        partner = request.env.user.partner_id
        res_company = request.env.user.company_id
        res_pricelist = request.env['booking.lodging.pricelist'].search([
            ('id','=',pricelist)

        ])
        filterPricelist = res_pricelist
        if partner.user_id:
            sales_rep = partner.user_id
        else:
            sales_rep = False
            values = {
                'sales_rep': sales_rep,
                'company': request.website.company_id,
                'user': request.env.user,
                'date': datetime.date.today().strftime('%Y-%m-%d'),
                'filterPricelist':filterPricelist,
                'res_company': res_company
            }
            return request.website.render("pricelist_web.lodging_view", values)

        

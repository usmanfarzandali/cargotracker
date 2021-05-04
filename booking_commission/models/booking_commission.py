# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class BookingMain(models.Model):
    _inherit = "booking.main"

    # ks_global_discount_type = fields.Selection([('percent', 'Percentage'), ('amount', 'Amount')],
    #                                            string='Universal Discount type', readonly=True,
    #                                            states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
    #                                            default='percent')

    
    sales_person_id = fields.Many2one('res.users', string='Sales Person')
    commission_type = fields.Selection([('percent', 'Percentage'), ('amount', 'Amount')],
                                               string='Commission Type',
                                               default='percent')
    commission_rate = fields.Float('Commission Percentage/Amount')


    has_commission = fields.Boolean('Any Commission')

    @api.multi
    @api.onchange('has_commission')
    def _onchange_has_commission(self):
        for rec in self:
            if not rec.has_commission:
                rec.sales_person_id = False
                rec.commission_rate = False
                rec.commission_type = False



class ResPartner(models.Model):
    _inherit = "res.partner"
    res_partner_commission_ids = fields.One2many('res.partner.commission', 'res_partner_id', 'Partner Commission IDs')


class ResPartnerCommission(models.Model):
    _name = "res.partner.commission"

    

    res_partner_id =  fields.Many2one('res.partner', string="Res Partner ID")


    commission_type = fields.Selection([('percent', 'Percentage'), ('amount', 'Amount')],
                                               string='Commission Type',
                                               default='percent')
    commission_rate = fields.Float('Commission Percentage/Amount')

    province = fields.Selection([('balochistan', 'Balochistan'),('federal', 'Federal'),
                                ('kpk', 'Khyber Pakhtunkhwa'),('punjab', 'Punjab'),
                                ('sindh', 'Sindh')],default="punjab", )

    

    
   

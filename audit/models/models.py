# -*- coding: utf-8 -*-

from odoo import models, fields, api



class audit(models.Model):
    _name = 'pao.auditorias'
    _description = 'Modulo Auditoria'
    _order = 'audit_num'
    _rec_name = 'audit_num'

    audit_num = fields.Char(string="Numero de auditoria",required=True)
    client_id = fields.Many2one('res.partner', string="Cliente",required=True)
    country_id = fields.Many2one('res.country', string="Pais de auditoria",required=True)
    state_id = fields.Many2one('res.country.state',string="Estado de auditoria",required=True)
    city_id = fields.Many2one('res.city',string="Ciudad de auditoria",required=True)

    _sql_constraints = [
        ('audit_num_unique','unique(audit_num)','Este numero de auditoria ya esta asignado')
    ]


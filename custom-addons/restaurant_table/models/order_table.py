from email.policy import default

from odoo import api, fields, models
from datetime import date

class RestaurantTable(models.Model):
    _name = 'restaurant.table'
    _description = 'Table management'

    active = fields.Boolean(default=True)

    name = fields.Char(
        string=' Số bàn',
        required=True,
        copy=False,
        readonly=True,
        default='New'
    )

    so_luong = fields.Integer(
        string=' Số lượng',
        required=True,
    )

    status = fields.Selection(
        selection=[
            ('draft', 'Nháp'),
            ('confirmed', 'đã xác nhận'),
            ('done', 'xong'),
            ('cancel', 'Hủy'),
        ],
        default='draft',
        string='Trạng thái',
        required=True
    )


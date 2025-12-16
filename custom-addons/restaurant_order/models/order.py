from odoo import api, fields, models
from datetime import date

class RestaurantOrder(models.Model):
    _name = 'restaurant.order'
    _description = 'Order'

    active = fields.Boolean(default=True)

    name = fields.Char(
        string='Mã đơn',
        required=True,
        copy=False,
        readonly=True,
        default='New'
    )

    partner_id = fields.Many2one(
        'res.partner',
        string='Khách hàng',
        required=True
    )

    order_date = fields.Date(
        string='Ngày đặt',
        default=date.today
    )

    state = fields.Selection(
        [
            ('draft', 'Nháp'),
            ('confirmed', 'Đã xác nhận'),
            ('done', 'Xong'),
            ('cancel', 'Hủy'),
        ],
        default='draft',
        string='Trạng thái',
        required=True
    )

    order_line_ids = fields.One2many(
        'restaurant.order.line',
        'order_id',
        string='Chi tiết món'
    )

    total_amount = fields.Float(
        string='Tổng tiền',
        compute='_compute_total_amount',
        store=True
    )

    @api.depends('order_line_ids.subtotal')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(order.order_line_ids.mapped('subtotal'))

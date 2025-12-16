from odoo import api, fields, models

class RestaurantOrderLine(models.Model):
    _name = 'restaurant.order.line'
    _description = 'Order Line'

    order_id = fields.Many2one(
        'restaurant.order',
        string='Đơn hàng',
        ondelete='cascade',
        required=True
    )

    item_id = fields.Many2one(
        'restaurant.menu.item',
        string='Món ăn',
        required=True
    )

    quantity = fields.Integer(default=1)

    subtotal = fields.Float(
        string='Thành tiền',
        compute='_compute_subtotal',
        store=True
    )

    @api.depends('quantity', 'item_id.price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = (line.quantity or 0) * (line.item_id.price or 0)

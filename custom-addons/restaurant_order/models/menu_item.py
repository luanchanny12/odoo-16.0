from odoo import fields, models

class MenuItem(models.Model):
    _name = 'restaurant.menu.item'
    _description = 'Menu item'

    name = fields.Char(string='Tên món', required=True)
    price = fields.Float(string='Giá tiền')

    category = fields.Selection(
        [
            ('food', 'Đồ ăn'),
            ('drink', 'Đồ uống')
        ],
        string='Loại',
        default='food',
        required=True
    )

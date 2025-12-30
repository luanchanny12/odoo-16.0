from odoo import api, fields, models

class RestaurantTable(models.Model):
    _name = 'table.management'
    _description = 'Table management'

    name = fields.Char(
        string='Số bàn',
        required=True,
        copy=False,

    )

    so_luong = fields.Integer(
        string='Số lượng',
        required=True,
    )

    status = fields.Selection(
        selection=[
            ('draft', 'Nháp'),
            ('confirmed', 'Đã xác nhận'),
            ('done', 'Xong'),
            ('cancel', 'Hủy'),
        ],
        default='draft',
        string='Trạng thái',
        required=True
    )

    @api.model
    def create(self, vals):
        # Nếu chưa có name, tự động đặt số bàn tăng dần
        if not vals.get('name'):
            # Lấy số bàn lớn nhất hiện có
            last_table = self.search([], order='name desc', limit=1)
            if last_table:
                vals['name'] = str(int(last_table.name) + 1)
            else:
                vals['name'] = '1'  # nếu chưa có bàn nào
        return super(RestaurantTable, self).create(vals)

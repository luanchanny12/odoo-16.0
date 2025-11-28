# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryStockMove(models.Model):
    _name = 'library.stock.move'
    _description = 'Phiếu Di chuyển Kho'
    _order = 'date desc'  # Sắp xếp ngày mới nhất lên đầu

    name = fields.Char(string='Mã phiếu', required=True, default='New')
    date = fields.Date(string='Ngày', default=fields.Date.today)

    # Liên kết tới Sách
    book_id = fields.Many2one('library.book', string='Sách', required=True)

    # Số lượng (+ là Nhập, - là Xuất)
    qty = fields.Integer(string='Số lượng (+/-)', required=True, default=1)

    state = fields.Selection([
        ('draft', 'Nháp'),
        ('done', 'Hoàn thành'),
    ], string='Trạng thái', default='draft')

    # --- 1. HÀM KIỂM TRA LOGIC (Ràng buộc) ---
    @api.constrains('qty')
    def _check_qty(self):
        for rec in self:
            if rec.qty == 0:
                raise ValidationError("Số lượng thay đổi phải khác 0!")

    # --- 2. HÀM KIỂM TRA TỒN KHO TRƯỚC KHI XUẤT ---
    def check_availability(self):
        # Chỉ kiểm tra khi Xuất kho (số âm)
        if self.qty < 0:
            # Lưu ý: Trường 'qty_on_hand' sẽ được tạo ở bước kế tiếp (bên model Sách)
            # Odoo đủ thông minh để đọc nó nếu nó tồn tại
            current_stock = self.book_id.qty_on_hand

            # Nếu Tồn hiện tại + Số xuất (âm) < 0 --> Lỗi
            if current_stock + self.qty < 0:
                raise ValidationError(
                    f"Không đủ hàng để xuất! Tồn kho hiện tại: {current_stock}, Yêu cầu xuất: {abs(self.qty)}")

    # --- 3. HÀM NÚT BẤM (ACTIONS) ---
    def action_confirm(self):
        # Gọi hàm kiểm tra trước khi xác nhận
        self.check_availability()
        self.write({'state': 'done'})

    def action_draft(self):
        self.write({'state': 'draft'})

    # --- 4. HÀM BẢO VỆ: CẤM XÓA KHI ĐÃ XONG ---
    def unlink(self):
        for rec in self:
            if rec.state == 'done':
                raise ValidationError("Không được phép xóa phiếu kho đã Hoàn thành! Hãy tạo phiếu ngược lại để bù trừ.")
        return super(LibraryStockMove, self).unlink()

    # --- 5. HÀM HIỂN THỊ TÊN ĐẸP ---
    # Giúp hiển thị tên dạng: "[Mã] Tên Sách (Số lượng)" ở các chỗ khác
    def name_get(self):
        result = []
        for rec in self:
            name = f"[{rec.name}] {rec.book_id.name} ({rec.qty})"
            result.append((rec.id, name))
        return result
from odoo import api, fields, models
from odoo.exceptions import ValidationError #sẽ sử dụng cho onchange
# thư viện này là thư viện kiều ghi ra lỗi í
import logging #thư viện để in ra log (debug)
#logging này nó sẽ in thông tin ra terminal

# tạo ra một logger cho file này
_logger = logging.getLogger(__name__)
#kiểu nó là quyển sổ ý khi mình kêu mở ra và ghi cho tôi th nó sẽ ghi thời gian ngày giờ và màu sắc

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do Task'

    name = fields.Char(string='Tên công việc', required=True)
    description = fields.Text(string='Mô tả')

    date_start = fields.Datetime(string='Ngày bắt đầu', default=fields.Datetime.now)
    date_end = fields.Datetime(string='Ngày kết thúc')

    is_done = fields.Boolean(string='Hoàn thành?',default=False)

    # bắt đầu logic tính toán
    #1. trường tính toán (COMPUTED FIELD)
    duration = fields.Float(
        string='Thời lượng (giờ)',
        compute='_compute_duration', #tên hàm python sẽ tính toán
        readonly=True, #Trường này không cho phép người dùng tự nhập
    )

    #2. Hàm Tính Toán (gắn với decorator @api.depends)
    #odoo sẽ tự ộng gọi hàm này mỗi khi 'date_start' hoặc 'date_end' thay đổi
    @api.depends('date_start', 'date_end')
    def _compute_duration(self):
        #in ra log để debug (bạn có thể xem log trong terminal)
        _logger.info('>>> Đang tính toán thời lượng...')

        #self ở đây là một tập hợp các bản ghi (records)
        for task in self:
            # Kiểm tra xem có đủ 2 ngày không
            if task.date_start and task.date_end:
                #trừ hai đối tượng Datetime
                delta = task.date_end - task.date_start
                # chuyển đổi sang giờ (total_seconds() / 3600)
                task.duration = delta.total_seconds() / 3600
            else:
                task.duration = 0.0

    # 3. hàm OnChange (gắn với decorator @api.onchange)
    # Odoo sẽ gọi hàm này khi NGƯỜI DÙNG ĐANG GÕ VÀO FORM (giao diện)
    @api.onchange('date_start', 'date_end')
    def _onchange_date_start(self):
        _logger.info(">>> Đang chạy Onchange ngày...")

        # Kiểm tra nếu có 2 ngày Và ngày kết thúc < ngày bắt đầu
        if self.date_start and self.date_end and self.date_end < self.date_start:
            # Gán lại ngày kết thúc = ngaỳ bắt đầu
            self.date_end = self.date_start

            # (Nâng cao) Trả về 1 cảnh báo (warning) cho người dùng
            return {
                'warning': {
                    'title': 'Giá trị không hợp lệ',
                    'message': 'Ngày kết thúc không thể nhỏ hơn ngày bắt đầu.Đã tự động sửa lại.'
                }
            }
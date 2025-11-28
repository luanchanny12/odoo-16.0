# -*- coding: utf-8 -*-

# 1. Nạp các model "cha" (không phụ thuộc ai)
from . import library_author
from . import library_book_category
from . import library_publisher
from . import library_borrow

# 2. Nạp model "con" (library.book) sau cùng
# (Vì nó phụ thuộc vào 3 model ở trên)
from . import library_book
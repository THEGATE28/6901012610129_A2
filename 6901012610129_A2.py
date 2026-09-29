# ==============================================================================
# โครงงาน: ระบบจัดการคลังสินค้าเบื้องต้น (Inventory Management System)
# ครอบคลุมเนื้อหา:
# 1. ตัวแปร, ชนิดข้อมูล, การรับ/แสดงผลข้อมูล, เงื่อนไข (if-elif-else), ลูป (while, for)
# 2. ฟังก์ชัน (Functions)
# 3. แถวลำดับ 2 มิติ (2D Array / Nested Lists)
# 4. คลาสและอ็อบเจกต์ (Class & Object - OOP)
# 5. การจัดการไฟล์ (File I/O: Read & Write)
# 6. การดักจับข้อผิดพลาด (Exception Handling: try-except)
# ==============================================================================

DATA_FILE = "inventory_data.txt"


# ------------------------------------------------------------------------------
# 4. เรื่องของ Class และ Object
# ------------------------------------------------------------------------------
class Product:
    """คลาสสำหรับจำลองข้อมูลสินค้าแต่ละรายการ"""

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        # 1. เรื่องพื้นฐาน: กำหนดตัวแปรและประเภทข้อมูล (String, Float, Integer)
        self.product_id = str(product_id)
        self.name = str(name)
        self.price = float(price)
        self.stock = int(stock)

    def to_row(self) -> list:
        """แปลงข้อมูล Object ให้เป็นแถวข้อมูล (1D List) เพื่อนำไปรวมเป็น 2D Array"""
        return [self.product_id, self.name, self.price, self.stock]


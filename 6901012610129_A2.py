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


class InventoryManager:
    """คลาสสำหรับบริหารจัดการสินค้าในคลัง"""

    def __init__(self):
        # เก็บรายการ Object ของ Product
        self.products: list[Product] = []

    # --------------------------------------------------------------------------
    # 3. เรื่องของ 2D Array (Nested List)
    # --------------------------------------------------------------------------
    def get_inventory_matrix(self) -> list[list]:
        """แปลงรายการสินค้าทั้งหมดให้อยู่ในรูป 2D Array [แถว][คอลัมน์]"""
        matrix = []
        for p in self.products:
            matrix.append(p.to_row())  # แถวละ 1 สินค้า [id, name, price, stock]
        return matrix

    # --------------------------------------------------------------------------
    # 5. เรื่องของ Open File (Write & Read) และ 6. Try & Except
    # --------------------------------------------------------------------------
    def save_to_file(self, filename: str = DATA_FILE) -> None:
        """บันทึกข้อมูลคลังสินค้าลงไฟล์ (Write Mode)"""
        try:
            matrix = self.get_inventory_matrix()
            with open(filename, mode="w", encoding="utf-8") as file:
                for row in matrix:
                    # แปลงสมาชิกใน 2D Array แต่ละแถวให้เป็นข้อความคั่นด้วยจุลภาค
                    line = f"{row[0]},{row[1]},{row[2]},{row[3]}\n"
                    file.write(line)
            print("[ระบบ] บันทึกข้อมูลลงไฟล์สำเร็จ")
        except IOError as e:
            print(f"[ข้อผิดพลาด] ไม่สามารถเขียนไฟล์ได้: {e}")

    def load_from_file(self, filename: str = DATA_FILE) -> None:
        """อ่านข้อมูลจากไฟล์ขึ้นมาเก็บในระบบ (Read Mode)"""
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                self.products.clear()
                for line in file:
                    line = line.strip()
                    if line:
                        p_id, name, price_str, stock_str = line.split(",")
                        # แปลงข้อมูลและสร้าง Object Product เพิ่มลงในคลัง
                        product = Product(p_id, name, float(price_str), int(stock_str))
                        self.products.append(product)
                print(f"[ระบบ] โหลดข้อมูลสำเร็จ พบสินค้า {len(self.products)} รายการ")
        except FileNotFoundError:
            print("[แจ้งเตือน] ไม่พบไฟล์ข้อมูลเดิม เริ่มต้นด้วยคลังสินค้าว่าง")
        except ValueError as e:
            print(f"[ข้อผิดพลาด] รูปแบบข้อมูลในไฟล์ไม่ถูกต้อง: {e}")

    # --------------------------------------------------------------------------
    # 2. เรื่องของฟังก์ชันการทำงานระบบคลังสินค้า
    # --------------------------------------------------------------------------
    def add_product(self, product_id: str, name: str, price: float, stock: int) -> bool:
        """ฟังก์ชันเพิ่มสินค้าใหม่เข้าคลัง"""
        if self.find_product(product_id) is not None:
            return False  # รหัสสินค้าซ้ำ
        new_prod = Product(product_id, name, price, stock)
        self.products.append(new_prod)
        return True

    def find_product(self, product_id: str) -> Product | None:
        """ค้นหาสินค้าจากรหัส (Linear Search)"""
        for p in self.products:
            if p.product_id == product_id:
                return p
        return None

    def display_matrix(self, matrix: list[list]) -> None:
        """แสดงผลข้อมูลแบบตารางด้วยการวนลูป 2 มิติ (Nested Loops)"""
        if not matrix:
            print("- ไม่มีข้อมูลสินค้าในระบบ -")
            return

        print("-" * 55)
        print(f"{'รหัส':<10}{'ชื่อสินค้า':<20}{'ราคา':>10}{'คงเหลือ':>15}")
        print("-" * 55)

        # การวนลูปเข้าถึงสมาชิกใน 2D Array: เข้าถึงแถว (Row)
        for row in matrix:
            # เข้าถึงข้อมูลแต่ละคอลัมน์ในแถวนั้น
            p_id = row[0]
            name = row[1]
            price = f"{row[2]:,.2f}"
            stock = f"{row[3]:,}"
            print(f"{p_id:<10}{name:<20}{price:>10}{stock:>15}")
        print("-" * 55)

    def stock_in(self, product_id: str, amount: int) -> bool:
        """ฟังก์ชันรับสินค้าเข้าคลัง"""
        p = self.find_product(product_id)
        if p and amount > 0:
            p.stock += amount
            return True
        return False

    def stock_out(self, product_id: str, amount: int) -> tuple[bool, float, int]:
        """ฟังก์ชันตัดสต็อกและคำนวณยอดเงินขาย"""
        p = self.find_product(product_id)
        if not p:
            return False, 0.0, 0
        if amount <= p.stock:
            p.stock -= amount
            total_price = amount * p.price
            return True, total_price, p.stock
        return False, -1.0, p.stock

    def get_low_stock_matrix(self, threshold: int = 5) -> list[list]:
        """ดึงรายการสินค้าใกล้หมดสต็อกในรูปแบบ 2D Array"""
        low_matrix = []
        for p in self.products:
            if p.stock <= threshold:
                low_matrix.append(p.to_row())
        return low_matrix

